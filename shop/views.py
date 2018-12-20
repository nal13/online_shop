from django.shortcuts import render, redirect
import os
import sys
from lxml import etree
from pprint import pprint

from .constants import g
from .forms import ModeloForm, LojaForm, OrderForm, SearchForm
from .forms_validation import *
from .wikidata import wikidata_modelo_info


#
#
#           GENERAL VIEWS
#
#
def home(request):

    # list up to 10 random modelos
    query = g.list_modelo_random('10')['results']['bindings']
    random_modelos = []
    for e in query:
        modelo_id = e['modelo_uri']['value'].split('/')[-1]
        nome = e['nome']['value']
        categoria = e['categoria']['value']
        preco = e['preco']['value']
        # get discount based on availiable units across all loja
        (preco_discount, discount) = get_discount( modelo_id, preco )
        random_modelos.append( (modelo_id, nome, categoria, preco, preco_discount, discount) )

    # search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

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

def get_discount(id, price):
    sum = int( g.get_modelo_em_loja_unidades_count( id )['results']['bindings'][0]['sum']['value'] )

    discount = 0
    if sum < 11:
        if sum in range(8,10):
            discount = 20
        elif sum in range(5,7):
            discount = 45
        elif sum in range(2,4):
            discount = 60
        else:
            discount = 75
    discount_price = round( float(price) * (1 - discount/100), 2 )

    return (discount_price, discount)

#
#
#           MODELO VIEWS
#
#
def list_categoria(request, categoria):

    # order select
    order = 'a-z'
    if request.method == 'POST' and 'order' in request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.cleaned_data.get('order')
    else:
        form = OrderForm()

    # list modelos with the given categoria
    query = g.list_modelo_by_categoria( categoria, order )['results']['bindings']

    # if no modelos, go home
    if ( not(query) ):
        return redirect( 'home' )

    modelos = []
    for e in query:
        modelo_id = e['uri']['value'].split('/')[-1]
        nome = e['nome']['value']
        preco = e['preco']['value']
        # get discount based on availiable units across all loja
        (preco_discount, discount) = get_discount( modelo_id, preco )
        modelos.append( (modelo_id, nome, categoria, preco, preco_discount, discount) )

    # search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

    return render(request, 'shop/list_categoria.html', {'form': form, 'modelos': modelos, 'search': search, })

def get_modelo(request, id):

    # get all modelo data from DB
    query_regular = g.get_modelo_regular(id)['results']['bindings']

    # if modelo doesn't exist, go home
    if ( not(query_regular) ):
        return redirect( 'home' )

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

    # get wikidata for modelo
    type = g.get_modelo_a( id )['results']['bindings'][0]['type']['value'].split('/')[-2]
    wiki_modelo = wikidata_modelo_info( type )

    # get up to 4 modelos with the same type
    query = g.list_modelo_by_a(id)['results']['bindings']
    type_modelos = []
    for e in query:
        modelo_id = e['modelo_uri']['value'].split('/')[-1]
        nome = e['nome']['value']
        categoria = e['categoria']['value']
        preco = e['preco']['value']
        # get discount based on availiable units across all loja
        (preco_discount, discount) = get_discount( modelo_id, preco )
        type_modelos.append( (modelo_id, nome, categoria, preco, preco_discount, discount) )

    # save discount without risking damaging other structured variables
    (preco_discount, discount) = get_discount( id, preco )
    modelo_discount = (preco_discount, discount)

    # search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

    return render(request, 'shop/get_modelo.html', {'modelo': modelo, 'modelo_discount':modelo_discount, 'type_modelos': type_modelos, 'em_lojas': em_lojas, 'id': id, 'search': search, 'wiki_modelo': wiki_modelo})

def add_modelo(request, type):

    if request.method == 'POST':
        form = ModeloForm(type, request.POST)
        if form.is_valid() and validate_modelo(form):

            new_id = g.get_next_id( 'modelo' )

            # insert modelo with the new highest id in DB
            g.add_modelo( id=new_id, fields=form.cleaned_data, type=form.type )

            return redirect( 'get_modelo', new_id )
    else:
        form = ModeloForm(type)

    # search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

    return render(request, 'shop/forms_modelo.html', {'form': form, 'search': search, })

def remove_modelo(request, id):
    # called in get_modelo.html, don't have a web page

    g.remove_modelo( id )

    return redirect('home')

def edit_modelo(request, id):

    # get type of modelo to call the right type of form
    type = g.get_modelo_a(id)['results']['bindings'][0]['type']['value'].split('/')[-2]

    # if modelo doesn't exist, go home
    if ( not(type) ):
        return redirect( 'home' )

    if request.method == 'POST':
        form = ModeloForm(type, request.POST)
        if form.is_valid():

            # modify modelo with id in DB
            g.remove_modelo( id )
            g.add_modelo( id=id, fields=form.cleaned_data, type=form.type )

            return redirect( 'get_modelo', id )
    else:
        form = ModeloForm(type)

        # load values from get_modelo view to set them as initial values in edit_modelo view
        form.set_initial_values( request.session.get('get_modelo_data'), id )

    # search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

    return render(request, 'shop/forms_modelo.html', {'form': form, 'search': search, })

#
#
#           LOJA VIEWS
#
#
def get_loja(request, id):

    # get loja from DB
    query = g.get_loja_regular(id)['results']['bindings']

    # if loja doesn't exist, go home
    if ( not(query) ):
        return redirect( 'home' )

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

    # get up to 4 modelos in this loja
    query = g.list_modelo_in_loja( id )['results']['bindings']
    modelos = []
    for e in query:
        modelo_id = e['modelo_uri']['value'].split('/')[-1]
        nome = e['nome']['value']
        categoria = e['categoria']['value']
        preco = e['preco']['value']
        # get discount based on availiable units across all loja
        (preco_discount, discount) = get_discount( modelo_id, preco )
        modelos.append( (modelo_id, nome, categoria, preco, preco_discount, discount) )

    # search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

    return render(request, 'shop/get_loja.html', {'loja': loja, 'modelos': modelos, 'id': id, 'search': search, })

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

            return redirect( 'get_loja', new_id )
    else:
        # IF submited already: get picked country in previous
        # ELSE use default country
        form = LojaForm( load=request.session.get('chose_country') )

    # search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

    return render(request, 'shop/forms_loja.html', {'form': form, 'search': search, })

def remove_loja(request, id):
    # called in get_loja.html, don't have a web page

    g.remove_loja( id )
    # remove all tiples that have this loja as object
    g.remove_loja_links( id )

    return redirect('home')

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
            g.remove_loja( id )
            g.add_loja( id=id, fields=form.cleaned_data )

            return redirect( 'get_loja', id )
    else:
        # IF submited already: get picked country in previous
        # ELSE use default country
        form = LojaForm( load=request.session.get('chose_country') )

        # load values from get_loja view to set them as initial values in edit_loja view
        form.set_initial_values( request.session.get('get_loja_data') )

    # search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

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
with open(path + 'dataset.n3', 'w', encoding='utf-8') as file:
    file.write(rdf_asString)

# start GraphDBapi
# initialized in: from .constants import g
