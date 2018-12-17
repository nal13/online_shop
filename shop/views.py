from django.shortcuts import render, redirect
import os
from lxml import etree
from pprint import pprint

from .constants import *
from .forms import ModeloForm, LojaForm
from .forms_validation import *


def home(request):
    return render(request, 'shop/index.html')


def store(request):
    return render(request, 'shop/store.html')


def product(request):
    return render(request, 'shop/product.html')


def list_modelo(request):

    modelos = {}
    query = g.list_modelo_uri_nome()

    for e in query['results']['bindings']:
        uri = e['uri']['value'].split('/')[-1]
        nome = e['nome']['value']
        modelos.update({uri: nome})

    return render(request, 'shop/list_modelo.html', {'modelos': modelos})

def get_modelo(request, id):

    modelo = {}
    pairs = {}
    em_lojas = {}   # dict of dicts, ex: {'12' : {'nome':'Loja Aveiro', 'unidades':'3'}}
    query_regular = g.get_modelo_regular(id)
    query_em_loja = g.list_modelo_em_loja(id)

    for e in query_regular['results']['bindings']:
        pred = e['pred']['value'].split('/')[-1]
        obj = e['obj']['value']
        modelo.update({pred: obj})

    for e in query_em_loja['results']['bindings']:
        nome = e['nome']['value']
        pairs.update({'nome': nome})

        pred = e['pred']['value'].split('/')[-1]
        obj = e['obj']['value']
        pairs.update({pred: obj})

        loja_uri = e['loja_uri']['value'].split('/')[-1]
        em_lojas.update({loja_uri: pairs})
        pairs = {}

    # session variable stored on the server --- used in edit_modelo
    # append both dictionaries
    request.session[ 'get_modelo_data' ] = modelo #{**modelo, **em_lojas}

    return render(request, 'shop/get_modelo.html', {'modelo': modelo, 'em_lojas': em_lojas, 'id': id})

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
    return render(request, 'shop/add_modelo.html', {'form': form})

def remove_modelo(request, id):
    # called in get_modelo.html, don't have a web page

    g.remove_modelo( id )

    return redirect('list_modelo')

def edit_modelo(request, id):

    # get type of modelo with id
    query = g.get_modelo_a(id)
    for e in query['results']['bindings']:
        type = e['type']['value'].split('/')[-2]

    if request.method == 'POST':
        form = ModeloForm(type, request.POST)
        if form.is_valid():

            # modify modelo with id in DB
            g.remove_modelo( id )     #TODO use known fields to improve query
            g.add_modelo( id=id, fields=form.cleaned_data, type=form.type )

            return redirect('list_modelo')
    else:
        form = ModeloForm(type)

        initial_fields = request.session.get('get_modelo_data')
        form.set_initial_values( initial_fields, id )

    return render(request, 'shop/add_loja.html', {'form': form})


def get_loja(request, id):

    loja = {}
    pairs = {}
    query_regular = g.get_loja_regular(id)
    query_morada = g.get_loja_morada(id)
    query_contacto = g.get_loja_contacto(id)

    # get regular pred and obj
    for e in query_regular['results']['bindings']:
        pred = e['pred']['value'].split('/')[-1]
        obj = e['obj']['value']
        loja.update({pred: obj})

    # get morada pred and obj
    for e in query_morada['results']['bindings']:
        pred = e['pred']['value'].split('/')[-1]
        obj = e['obj']['value']
        pairs.update({pred: obj})
    loja.update( {'morada':pairs} )
    pairs = {}

    # get contacto pred and obj
    for e in query_contacto['results']['bindings']:
        pred = e['pred']['value'].split('/')[-1]
        obj = e['obj']['value']
        pairs.update({pred: obj})
    loja.update( {'contacto':pairs} )

    # session variable stored on the server --- used in edit_loja
    request.session[ 'get_loja_data' ] = loja

    return render(request, 'shop/get_loja.html', {'loja': loja, 'id': id})

def add_loja(request):

    if request.method == 'POST':
        form = LojaForm(request.POST)
        if form.is_valid() and validate_loja(form):

            new_id = g.get_next_id( 'loja' )

            # insert loja with the new highest id in DB
            g.add_loja( id=new_id, fields=form.cleaned_data )

            return redirect('list_modelo')
    else:
        form = LojaForm()
    return render(request, 'shop/add_loja.html', {'form': form})

def remove_loja(request, id):
    # called in get_loja.html, don't have a web page

    g.remove_loja( id )
    g.remove_loja_links( id )

    return redirect('list_modelo')

def edit_loja(request, id):

    if request.method == 'POST':
        form = LojaForm(request.POST)
        if form.is_valid():

            # modify loja with id in DB
            g.remove_loja( id )     #TODO use known fields to improve query
            g.add_loja( id=id, fields=form.cleaned_data )

            return redirect('list_modelo')
    else:
        form = LojaForm()

        initial_fields = request.session.get('get_loja_data')
        form.set_initial_values( initial_fields )

    return render(request, 'shop/add_loja.html', {'form': form})

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
with open(path + 'dataset.nt', 'w', encoding='utf-8') as file:
    file.write(rdf_asString)

#
#           start GraphDBapi
#
# initialized in: from .constants import *
