from django.shortcuts import render, redirect
import os
from lxml import etree
from pprint import pprint

from .constants import *
from .forms import AddModeloForm, AddLojaForm
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

    return render(request, 'shop/get_modelo.html', {'modelo': modelo, 'em_lojas': em_lojas})

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
        form = AddModeloForm(type, request.POST)
        if form.is_valid() and validate_modelo(form):

            # insert modelo with the new highest id in DB
            g.add_modelo( form.type, form.cleaned_data )

            # pprint(form.cleaned_data)
            # print('\n')
            # pprint(form.data)
            return redirect('list_modelo')
    else:
        form = AddModeloForm(type)
    return render(request, 'shop/add_modelo.html', {'form': form})


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

    return render(request, 'shop/get_loja.html', {'loja': loja})

def add_loja(request):

    if request.method == 'POST':
        form = AddLojaForm(request.POST)
        if form.is_valid() and validate_loja(form):

            # insert loja with the new highest id in DB
            g.add_loja( form.cleaned_data )

            pprint( form.cleaned_data )
            return redirect('list_modelo')
    else:
        form = AddLojaForm()
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
with open(path + 'dataset.n3', 'w', encoding='utf-8') as file:
    file.write(rdf_asString)

#
#           start GraphDBapi
#
# initialized in: from .constants import *
