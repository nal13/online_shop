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

    # --- list up to 10 random modelos from DB as LIST of DICT
    query = g.list_modelo_random('10')
    random_modelos = []
    for e in query:
        modelo_id = g.get_value( e, 'modelo_uri' )
        nome = g.get_value( e, 'nome' )
        categoria = g.get_value( e, 'categoria' )
        preco = g.get_value( e, 'preco' )
        # get discount based on availiable units across all loja
        (discount_price, discount_percentage) = get_discount( modelo_id, preco )
        random_modelos.append( {'modelo_id':modelo_id, 'nome':nome, 'categoria':categoria, 'preco':preco, 'discount_price':discount_price, 'discount_percentage':discount_percentage} )

    # --- search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

    return render(request, 'shop/home.html', {'random_modelos': random_modelos, 'search': search, })

def search_box(request):
    # this is not a view
    # operates search box accross the app

    # --- handles forms
    if request.method == 'POST' and 'search' in request.POST:
        form = SearchForm(request.POST)

        if form.is_valid():
            search_box = form.cleaned_data['search_box']
            search_type = form.cleaned_data['search_type']

            if search_box:
                query = g.get_modelo_loja_uri( search_box, search_type )

                # return id if any
                if query != []:
                    return ( 'get_'+search_type, g.get_value( query[0], 'uri' ) )
    else:
        form = SearchForm()

    return form

def get_discount(id, price):
    query = g.get_modelo_em_loja_unidades_count( id )
    sum = int( g.get_value(query[0], 'sum') )

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

    # --- order select
    order = 'a-z'
    if request.method == 'POST' and 'order' in request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.cleaned_data.get('order')
    else:
        form = OrderForm()

    # --- get modelo with the given categoria from DB as LIST of DICT
    query = g.list_modelo_by_categoria( categoria, order )

    # if no modelos, go home
    if ( not(query) ):
        return redirect( 'home' )

    modelos = []
    for e in query:
        modelo_id = g.get_value(e, 'uri')
        nome = g.get_value(e, 'nome')
        preco = g.get_value(e, 'preco')
        # get discount based on availiable units across all loja
        (discount_price, discount_percentage) = get_discount( modelo_id, preco )
        modelos.append( {'modelo_id':modelo_id, 'nome':nome, 'categoria':categoria, 'preco':preco, 'discount_price':discount_price, 'discount_percentage':discount_percentage} )

    # --- search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

    return render(request, 'shop/list_categoria.html', {'form': form, 'modelos': modelos, 'search': search, })

def get_modelo(request, id):

    # --- get modelo from DB as DICT and as LIST of DICT
    query_regular = g.get_modelo_regular(id)

    # if modelo doesn't exist, go home
    if ( not(query_regular) ):
        return redirect( 'home' )

    query_em_loja = g.list_modelo_em_loja(id)

    modelo = {}
    for e in query_regular:
        pred = g.get_value(e, 'pred')
        obj = g.get_value(e, 'obj')
        modelo.update( {pred:obj} )

    em_loja = []
    for e in query_em_loja:
        loja_id = g.get_value(e, 'loja_uri')
        nome = g.get_value(e, 'nome')
        unidades = g.get_value(e, 'unidades')
        em_loja.append( {'loja_id': loja_id, 'nome': nome, 'unidades': unidades} )

    # --- compute discount for this modelo to DICT
    (discount_price, discount_percentage) = get_discount( id, modelo.get('preco') )
    discount = {'price':discount_price, 'percentage':discount_percentage}

    # --- get modelo from wikidata as DICT
    query = g.get_modelo_a( id )
    type = g.get_value(query[0], 'type')
    query_wiki = wikidata_modelo_info( type )
    pprint( query_wiki )
    wiki_modelo = {}
    for e in query_wiki:
        wiki_modelo.update( {e[0]:e[1]} )

    # --- get up to 4 modelos with the same type from DB as LIST of DICT
    query = g.list_modelo_by_a(id)
    type_modelos = []
    for e in query:
        modelo_id = g.get_value(e, 'modelo_uri')
        nome = g.get_value(e, 'nome')
        categoria = g.get_value(e, 'categoria')
        preco = g.get_value(e, 'preco')
        # get discount based on availiable units across all loja
        (discount_price, discount_percentage) = get_discount( modelo_id, preco )
        type_modelos.append( {'modelo_id':modelo_id, 'nome':nome, 'categoria':categoria, 'preco':preco, 'discount_price':discount_price, 'discount_percentage':discount_percentage} )

    # --- search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

    return render(request, 'shop/get_modelo.html', {'id': id, 'modelo': modelo, 'discount':discount, 'wiki_modelo': wiki_modelo, 'em_loja': em_loja, 'type_modelos': type_modelos, 'search': search})

def add_modelo(request, type):

    # --- handle forms
    if request.method == 'POST':
        form = ModeloForm(type, request.POST)
        if form.is_valid() and validate_modelo(form):

            new_id = g.get_next_id( 'modelo' )

            # insert modelo with the new highest id in DB
            g.add_modelo( id=new_id, fields=form.cleaned_data, type=form.type )

            return redirect( 'get_modelo', new_id )
    else:
        form = ModeloForm(type)

    # --- search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

    return render(request, 'shop/forms_modelo.html', {'form': form, 'search': search, })

def remove_modelo(request, id):
    # called in get_modelo.html, don't have a web page

    g.remove_modelo( id )

    return redirect('home')

def edit_modelo(request, id):

    # --- handle forms
    # get type of modelo to call the right type of form
    query = g.get_modelo_a(id)
    type = g.get_value(query[0], 'type')

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

        # --- get modelo from DB as DICT to set forms' initial values
        query_regular = g.get_modelo_regular(id)

        modelo = {}
        for e in query_regular:
            pred = g.get_value(e, 'pred')
            obj = g.get_value(e, 'obj')
            modelo.update( {pred:obj} )

        form.set_initial_values( modelo, id )

    # --- search box
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

    # --- get loja from DB as DICT
    query = g.get_loja_regular(id)

    # if loja doesn't exist, go home
    if ( not(query) ):
        return redirect( 'home' )

    query += g.get_loja_morada(id)
    query += g.get_loja_contacto(id)

    loja = {}
    for e in query:
        pred = g.get_value( e, 'pred' )
        obj = g.get_value( e, 'obj' )
        loja.update( {pred:obj} )

    # --- get up to 4 modelos in this loja from DB as LIST of DICT
    query = g.list_modelo_in_loja( id )
    modelos = []
    for e in query:
        modelo_id = g.get_value( e, 'modelo_uri' )
        nome = g.get_value( e, 'nome' )
        categoria = g.get_value( e, 'categoria' )
        preco = g.get_value( e, 'preco' )
        # get discount based on availiable units across all loja
        (discount_price, discount_percentage) = get_discount( modelo_id, preco )
        modelos.append( {'modelo_id':modelo_id, 'nome':nome, 'categoria':categoria, 'preco':preco, 'discount_price':discount_price, 'discount_percentage':discount_percentage} )

    # --- search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

    return render(request, 'shop/get_loja.html', {'id': id, 'loja': loja, 'modelos': modelos, 'search': search, })

def add_loja(request):

    # --- handle forms
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

    # --- search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

    return render(request, 'shop/forms_loja.html', {'form': form, 'search': search, })

def remove_loja(request, id):
    # doesn't have a HTML page

    # --- remove this loja and all triples that have this loja as object
    g.remove_loja( id )
    g.remove_loja_links( id )

    return redirect('home')

def edit_loja(request, id):

    # --- handle forms
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

        # --- get loja from DB as DICT to set forms' initial values
        query = g.get_loja_regular(id)
        query += g.get_loja_morada(id)
        query += g.get_loja_contacto(id)

        loja = {}
        for e in query:
            pred = g.get_value( e, 'pred' )
            obj = g.get_value( e, 'obj' )
            loja.update( {pred:obj} )

        form.set_initial_values( loja )

    # --- search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

    return render(request, 'shop/forms_loja.html', {'form': form, 'search': search, })

#
#
#           CLIENTE VIEWS
#
#
def get_cliente(request, id):

    # --- get cliente from DB as DICT
    query = g.get_cliente_regular(id)

    # if cliente doesn't exist, go home
    if ( not(query) ):
        return redirect( 'home' )

    query += g.get_morada('cliente', id)
    query += g.get_contacto('cliente', id)

    cliente = {}
    for e in query:
        pred = g.get_value( e, 'pred' )
        obj = g.get_value( e, 'obj' )
        cliente.update( {pred:obj} )

    # --- search box
    search = search_box(request)

    if isinstance(search, tuple):
        return redirect( search[0], id=search[1] )

    return render(request, 'shop/get_cliente.html', {'id': id, 'cliente': cliente, 'search': search, })

def add_cliente( signup_forms ):
    # this is not a view
    # a cliente is added when creating a new user

    new_id = g.get_next_id( 'cliente' )

    # insert cliente with the new highest id in DB
    g.add_cliente( id=new_id, fields=signup_forms )
    return new_id

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
# initialized in: from .constants import g
