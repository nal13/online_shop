from django.shortcuts import render, redirect
import os
from lxml import etree
from pprint import pprint

from .constants import *
from .forms import ModeloForm, LojaForm
from .forms_validation import *
from .wikidata import get_wikidata


def home(request):

    get_wikidata()

    return render(request, 'shop/index.html')


def store(request):
    return render(request, 'shop/store.html')


def product(request):
    return render(request, 'shop/product.html')


def add_buttons(request):

    modelos_types = []
    query = g.list_modelo_a()

    for e in query['results']['bindings']:
        type = e['type']['value'].split('/')[-2]
        modelos_types.append(type)

    ## for tests
    ##
    # query = g.list_modelo_marca()
    # marcas = []
    # # print(query)
    # for e in query['results']['bindings']:
    #     marca = e['marca']['value']
    #     marcas.append((marca,marca))
    # print(marcas)

    return render(request, 'shop/add_buttons.html', {'modelos_types': modelos_types, 'loja_type': 'loja'})

def list_modelo(request):

    modelos = {}
    query = g.list_modelo_uri_nome()

    for e in query['results']['bindings']:
        uri = e['uri']['value'].split('/')[-1]
        nome = e['nome']['value']
        modelos.update({uri: nome})

    return render(request, 'shop/list_modelo.html', {'modelos': modelos})

def get_modelo(request, id):

    query_regular = g.get_modelo_regular(id)['results']['bindings']
    query_em_loja = g.list_modelo_em_loja(id)['results']['bindings']

    modelo = []
    esta_loja = []
    em_lojas = []   # list of lists
    for e in query_regular:
        pred = e['pred']['value'].split('/')[-1]
        obj = e['obj']['value']
        modelo.append( (pred, obj) )

    for e in query_em_loja:
        nome = e['nome']['value']
        esta_loja.append( ('nome', nome) )

        pred = e['pred']['value'].split('/')[-1]
        obj = e['obj']['value']
        esta_loja.append( (pred, obj) )

        em_lojas.append( esta_loja )
        esta_loja = []

        # atempt to save loja_id --- commented cuz I think it's not necessary anywhere (yet)
        # loja_uri = e['loja_uri']['value'].split('/')[-1]
        # em_lojas.append( [loja_uri, esta_loja] )
        # esta_loja = []

    # session variable stored on the server --- used in edit_modelo
    request.session[ 'get_modelo_data' ] = modelo #{**modelo, **em_lojas}

    return render(request, 'shop/get_modelo.html', {'modelo': modelo, 'em_lojas': em_lojas, 'id': id})

def add_modelo(request, type):

    if request.method == 'POST':
        form = ModeloForm(type, request.POST)
        if form.is_valid() and validate_modelo(form):

            new_id = g.get_next_id( 'modelo' )

            # insert modelo with the new highest id in DB
            g.add_modelo( id=new_id, fields=form.cleaned_data, type=form.type )

            return redirect('list_modelo')
    else:
        form = ModeloForm(type)
    return render(request, 'shop/forms_modelo.html', {'form': form})

def remove_modelo(request, id):
    # called in get_modelo.html, don't have a web page

    g.remove_modelo( id )

    return redirect('list_modelo')

def edit_modelo(request, id):

    # get type of modelo from DB with id
    type = g.get_modelo_a(id)['results']['bindings'][0]['type']['value'].split('/')[-2]

    if request.method == 'POST':
        form = ModeloForm(type, request.POST)
        if form.is_valid():

            # modify modelo with id in DB
            g.remove_modelo( id )     #TODO use known fields to improve query
            g.add_modelo( id=id, fields=form.cleaned_data, type=form.type )

            return redirect('list_modelo')
    else:
        form = ModeloForm(type)

        # load values from get_modelo view to set them as initial values in edit_modelo view
        form.set_initial_values( request.session.get('get_modelo_data'), id )

    return render(request, 'shop/forms_modelo.html', {'form': form})


def get_loja(request, id):

    # get from DB
    query = g.get_loja_regular(id)['results']['bindings']
    query += g.get_loja_morada(id)['results']['bindings']
    query += g.get_loja_contacto(id)['results']['bindings']

    # get query result as tuples: ( pred, obj )
    loja = []
    for e in query:
        pred = e['pred']['value'].split('/')[-1]
        obj = e['obj']['value']
        loja.append( (pred, obj) )

    # session save to be used in edit_loja view
    request.session[ 'get_loja_data' ] = loja

    return render(request, 'shop/get_loja.html', {'loja': loja, 'id': id})

def add_loja(request):

    if request.method == 'POST':
        # get picked country in previous submit
        chose_country = request.POST.get('pais')
        request.session[ 'chose_country' ] = chose_country

        form = LojaForm(request.POST, load=chose_country )
        if form.is_valid() and validate_loja(form):
            # loja created => delete picked country in session
            del request.session['chose_country']

            new_id = g.get_next_id( 'loja' )

            # insert loja with the new highest id in DB
            g.add_loja( id=new_id, fields=form.cleaned_data )

            return redirect('list_modelo')
    else:
        # IF submited already: get picked country in previous
        # ELSE use default country
        form = LojaForm( load=request.session.get('chose_country') )

    return render(request, 'shop/forms_loja.html', {'form': form})

def remove_loja(request, id):
    # called in get_loja.html, don't have a web page

    g.remove_loja( id )
    g.remove_loja_links( id )

    return redirect('list_modelo')

def edit_loja(request, id):

    if request.method == 'POST':
        # get picked country in previous submit
        chose_country = request.POST.get('pais')
        request.session[ 'chose_country' ] = chose_country

        form = LojaForm(request.POST, load=chose_country )
        if form.is_valid():
            # loja created => delete picked country in session
            del request.session['chose_country']

            # modify loja with id in DB
            g.remove_loja( id )     #TODO use known fields to improve query
            g.add_loja( id=id, fields=form.cleaned_data )

            return redirect('list_modelo')
    else:
        # IF submited already: get picked country in previous
        # ELSE use default country
        form = LojaForm( load=request.session.get('chose_country') )

        # load values from get_loja view to set them as initial values in edit_loja view
        form.set_initial_values( request.session.get('get_loja_data') )

    return render(request, 'shop/forms_loja.html', {'form': form})

#
#           XSLT transformation to N3 triples
#
path = os.getcwd() + "/shop_resources/"

xml_path = path + "dataset.xml"
xml_root = etree.parse(xml_path)

xslt_path = path + "transform.xsl"
xslt_root = etree.parse(xslt_path)

transform = etree.XSLT(xslt_root)
rdf = transform(xml_root)

# remove xml header by lxml
rdf_asString = str(rdf).replace('<?xml version=\"1.0\"?>\n', '')

# save rdf as a .n3 file
with open(path + 'dataset.n3', 'w', encoding='utf-8') as file:
    file.write(rdf_asString)

#
#           start GraphDBapi
#
# initialized in: from .constants import *
