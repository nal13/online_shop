from django.shortcuts import render, redirect
import os
from lxml import etree
from pprint import pprint

from .constants import *
from .forms import ModeloForm, LojaForm, OrderForm, SearchForm
from .forms_validation import *
from .wikidata import test_wikidata, wikidata_modelo_info


#
#
#           GENERAL VIEWS
#
#
def home(request):

    # search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

    # test_wikidata()

    # list up to 10 random modelos
    query = g.list_modelo_random('10')['results']['bindings']
    random_modelos = []
    for e in query:
        modelo_id = e['modelo_uri']['value'].split('/')[-1]
        nome = e['nome']['value']
        categoria = e['categoria']['value']
        preco = e['preco']['value']
        random_modelos.append( (modelo_id, nome, categoria, preco) )

    return render(request, 'shop/home.html', {'random_modelos': random_modelos, 'search': search, })

def search_box(request):
    # this is not a view
    # operates search box accross the app

    if request.method == 'POST' and 'search' in request.POST:
        form = SearchForm(request.POST)

        if form.is_valid():
            search_box = form.cleaned_data['search_box']
            search_type = form.cleaned_data['search_type']

            if search_box:
                query = g.get_modelo_loja_uri( search_box, search_type )['results']['bindings']

                # return id if any
                if query != []:
                    return ( 'get_'+search_type, query[0]['uri']['value'].split('/')[-1] )
    else:
        form = SearchForm()

    return form

#
#
#           MODELO VIEWS
#
#
def list_categoria(request, categoria):

    # search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

    # order select
    order = 'valiosos'
    if request.method == 'POST' and 'order' in request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.cleaned_data.get('order')
    else:
        form = OrderForm()

    query = g.list_modelo_with_categoria( categoria, order )['results']['bindings']

    modelos = []
    for e in query:
        uri = e['uri']['value'].split('/')[-1]
        nome = e['nome']['value']
        preco = e['preco']['value']
        modelos.append( (uri, nome, categoria, preco) )

    pprint( modelos )

    return render(request, 'shop/list_categoria.html', {'form': form, 'modelos': modelos, 'search': search, })

def list_modelo(request):

    modelos = []
    query = g.list_modelo_uri_nome()['results']['bindings']

    for e in query:
        uri = e['uri']['value'].split('/')[-1]
        nome = e['nome']['value']
        modelos.append( (uri, nome) )

    return render(request, 'shop/list_modelo.html', {'modelos': modelos})

def get_modelo(request, id):

    # search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

    # get up to 4 modelos with the same type
    query = g.list_modelo_by_a(id)['results']['bindings']
    type_modelos = []
    for e in query:
        modelo_id = e['modelo_uri']['value'].split('/')[-1]
        nome = e['nome']['value']
        categoria = e['categoria']['value']
        preco = e['preco']['value']
        type_modelos.append( (modelo_id, nome, categoria, preco) )

    # get wikidata for modelo
    type = g.get_modelo_a( id )['results']['bindings'][0]['type']['value'].split('/')[-2]
    wiki_modelo = wikidata_modelo_info( type )

    # get all modelo data from DB
    query_regular = g.get_modelo_regular(id)['results']['bindings']
    query_em_loja = g.list_modelo_em_loja(id)['results']['bindings']

    modelo = []
    esta_loja = []
    em_lojas = {}   # dict of lists
    for e in query_regular:
        pred = e['pred']['value'].split('/')[-1]
        obj = e['obj']['value']
        modelo.append( (pred, obj) )

    for e in query_em_loja:
        loja_id = e['loja_uri']['value'].split('/')[-1]

        nome = e['nome']['value']
        esta_loja.append( ('nome', nome) )

        pred = e['pred']['value'].split('/')[-1]
        obj = e['obj']['value']
        esta_loja.append( (pred, obj) )

        em_lojas.update( { loja_id: esta_loja} )
        esta_loja = []

    # session variable stored on the server --- used in edit_modelo
    request.session[ 'get_modelo_data' ] = modelo

    return render(request, 'shop/get_modelo.html', {'modelo': modelo, 'type_modelos': type_modelos, 'em_lojas': em_lojas, 'id': id, 'search': search, 'wiki_modelo': wiki_modelo})

# import shutil
def add_modelo(request, type):

    # search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

    if request.method == 'POST':
        form = ModeloForm(type, request.POST)
        if form.is_valid() and validate_modelo(form):

            new_id = g.get_next_id( 'modelo' )

            # insert modelo with the new highest id in DB
            g.add_modelo( id=new_id, fields=form.cleaned_data, type=form.type )

            # # copy default image and name it with this modelo name
            # shutil.copy("/static/shop/img/modelos/{{ e.1 }}.jpg","/static/shop/img/modelos/{{ e.1 }}.jpg")

            return redirect( 'get_modelo', new_id )
    else:
        form = ModeloForm(type)
    return render(request, 'shop/forms_modelo.html', {'form': form, 'search': search, })

def remove_modelo(request, id):
    # called in get_modelo.html, don't have a web page

    g.remove_modelo( id )

    return redirect('home')

def edit_modelo(request, id):

    # search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

    # get type of modelo from DB with id
    type = g.get_modelo_a(id)['results']['bindings']
    pprint( type )

    type = g.get_modelo_a(id)['results']['bindings'][0]['type']['value'].split('/')[-2]


    if request.method == 'POST':
        form = ModeloForm(type, request.POST)
        if form.is_valid():

            # modify modelo with id in DB
            g.remove_modelo( id )     #TODO use known fields to improve query
            g.add_modelo( id=id, fields=form.cleaned_data, type=form.type )

            return redirect( 'get_modelo', id )
    else:
        form = ModeloForm(type)

        # load values from get_modelo view to set them as initial values in edit_modelo view
        form.set_initial_values( request.session.get('get_modelo_data'), id )

    return render(request, 'shop/forms_modelo.html', {'form': form, 'search': search, })

#
#
#           LOJA VIEWS
#
#
def get_loja(request, id):

    # search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

    # get up to 4 modelos in this loja
    query = g.list_modelo_in_loja( id )['results']['bindings']
    modelos = []
    for e in query:
        modelo_id = e['modelo_uri']['value'].split('/')[-1]
        nome = e['nome']['value']
        categoria = e['categoria']['value']
        preco = e['preco']['value']
        modelos.append( (modelo_id, nome, categoria, preco) )

    # get loja from DB
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

    return render(request, 'shop/get_loja.html', {'loja': loja, 'modelos': modelos, 'id': id, 'search': search, })

def add_loja(request):

    # search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

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

            return redirect( 'get_loja', new_id )
    else:
        # IF submited already: get picked country in previous
        # ELSE use default country
        form = LojaForm( load=request.session.get('chose_country') )

    return render(request, 'shop/forms_loja.html', {'form': form, 'search': search, })

def remove_loja(request, id):
    # called in get_loja.html, don't have a web page

    g.remove_loja( id )
    g.remove_loja_links( id )

    return redirect('home')

def edit_loja(request, id):

    # search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )


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

            return redirect( 'get_loja', id )
    else:
        # IF submited already: get picked country in previous
        # ELSE use default country
        form = LojaForm( load=request.session.get('chose_country') )

        # load values from get_loja view to set them as initial values in edit_loja view
        form.set_initial_values( request.session.get('get_loja_data') )

    return render(request, 'shop/forms_loja.html', {'form': form, 'search': search, })

#
#
#           INITIAL SETUP
#
#

# XSLT transformation to N3 triples
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
with open(path + 'dataset.nt', 'w', encoding='utf-8') as file:
    file.write(rdf_asString)

# start GraphDBapi
# initialized in: from .constants import *
