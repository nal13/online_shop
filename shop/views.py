from django.shortcuts import render, redirect
import os
from lxml import etree
import pprint

from .queries import GraphDB
from .forms import AddModeloForm, AddLojaForm


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

    modelos = []
    query = g.list_modelo_a()

    for e in query['results']['bindings']:
        type = e['type']['value'].split('/')[-2]
        modelos.append(type)
    loja_type = 'loja'

    ## for tests
    ##
    # query = g.list_modelo_marca()
    # marcas = []
    # # print(query)
    # for e in query['results']['bindings']:
    #     marca = e['marca']['value']
    #     marcas.append((marca,marca))
    # print(marcas)

    query = g.exists_loja_name('Media Markt Aveiro')
    pprint.pprint(query)

    return render(request, 'shop/add_buttons.html', {'modelos': modelos, 'loja_type': loja_type})

def add_modelo(request, type):

    if request.method == 'POST':
        form = AddModeloForm(type, request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            nome = clean.get('nome')
            marca = clean.get('marca')
            categoria = clean.get('categoria')
            preco = clean.get('preco')
            pprint.pprint(clean)
            print('\n')
            pprint.pprint(form.data)
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
    # pprint.pprint(query_morada)
    # pprint.pprint(query_regular)
    # pprint.pprint(query_contacto)

    for e in query_regular['results']['bindings']:
        pred = e['pred']['value'].split('/')[-1]
        obj = e['obj']['value']
        loja.update({pred: obj})

    for e in query_morada['results']['bindings']:
        pred = e['pred']['value'].split('/')[-1]
        obj = e['obj']['value']
        pairs.update({pred: obj})
    loja.update( {'morada':pairs} )
    pairs = {}

    for e in query_contacto['results']['bindings']:
        pred = e['pred']['value'].split('/')[-1]
        obj = e['obj']['value']
        pairs.update({pred: obj})
    loja.update( {'contacto':pairs} )

    return render(request, 'shop/get_loja.html', {'loja': loja})

def add_loja(request):

    if request.method == 'POST':
        form = AddLojaForm(type, request.POST)
        if form.is_valid():

            query = g.get_loja_uri_max()
            for e in query['results']['bindings']:
                id_max = e['uri_max']['value'].split('/')[-1]
            pprint.pprint(id_max)

            next_id = str(int(id_max)+1)
            query = g.add_loja( next_id, form.cleaned_data )
            pprint.pprint(query)


            pprint.pprint( form.cleaned_data )
            return redirect('list_modelo')
    else:
        form = AddLojaForm(type)
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
g = GraphDB()
