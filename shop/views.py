from django.shortcuts import render, redirect
import os
from lxml import etree

from .queries import GraphDB
from .forms import AddModelForm


def home(request):
    return render(request, 'shop/index.html')


def store(request):
    return render(request, 'shop/store.html')


def product(request):
    return render(request, 'shop/product.html')


def list_modelo(request):
    query = g.list_modelo_nome()
    modelos = {}

    for e in query['results']['bindings']:
        id = e['id']['value'].split('/')[-1]
        nome = e['nome']['value']
        modelos.update({id: nome})

    return render(request, 'shop/list_modelo.html', {'modelos': modelos})

def list_modelo(request):
    query = g.list_modelo_nome()
    modelos = {}

    for e in query['results']['bindings']:
        id = e['id']['value'].split('/')[-1]
        nome = e['nome']['value']
        modelos.update({id: nome})

    return render(request, 'shop/list_modelo.html', {'modelos': modelos})


def get_modelo(request, id):
    query = g.get_modelo(id)
    modelo = {}

    for e in query['results']['bindings']:
        pred = e['pred']['value'].split('/')[-1]
        obj = e['obj']['value']
        modelo.update({pred: obj})

    query = g.list_modelo_em_loja(id)
    print(query)
    # modelo = {}
    #
    # for e in query['results']['bindings']:
    #     pred = e['pred']['value'].split('/')[-1]
    #     obj = e['obj']['value']
    #     modelo.update({pred: obj})

    return render(request, 'shop/get_modelo.html', {'modelo': modelo})


def add_modelo_buttons(request):
    query = g.list_modelo_a()
    modelos = []

    for e in query['results']['bindings']:
        type = e['type']['value'].split('/')[-2]
        modelos.append(type)

    ## for tests
    ##
    # query = g.list_modelo_marca()
    # marcas = []
    # # print(query)
    # for e in query['results']['bindings']:
    #     marca = e['marca']['value']
    #     marcas.append((marca,marca))
    # print(marcas)

    return render(request, 'shop/add_modelo_buttons.html', {'modelos': modelos})


def add_modelo(request, type):

    if request.method == 'POST':
        form = AddModelForm(type, request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            nome = clean.get('nome')
            marca = clean.get('marca')
            categoria = clean.get('categoria')
            preco = clean.get('preco')
            return redirect('list_modelo')
    else:
        form = AddModelForm(type)
    return render(request, 'shop/add_modelo.html', {'form': form})


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
