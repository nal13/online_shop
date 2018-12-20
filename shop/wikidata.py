from wikidata.client import Client
import requests
from lxml import etree
from pprint import pprint

available_countries = ( ('Portugal','wd:Q41806065'), ('Espanha','wd:Q162620'), ('Itália','wd:Q15089') )
available_modelos = (
    ('computador', 'wd:Q3962'),
    ('telemovel', 'wd:Q22645'),
    ('tablet', 'wd:Q155972'),
    ('camara', 'wd:Q15328'),
    ('drone', 'wd:Q484000'),
    ('tv', 'wd:Q564635'),
    ('leitor_blueray', 'wd:Q3783103'),
    ('maquina_cafe', 'wd:Q211841'),
    ('microondas', 'wd:Q127956'),
    ('maquina_lavar_roupa','wd:Q124441') ,
    ('maquina_secar_roupa','wd:Q496334') ,
    ('aspirador','wd:Q101674'),
    ('gaming_pc','wd:Q3962'),
    ('consola','wd:Q8076'),
    ('jogo','wd:Q7889'),
)


def wikidata_capitals( country ):
    # names of country region's capitals

    # countries allowed
    for e in available_countries:
        if country == e[0]:
            districts_of = e[1]

    query = """
        SELECT ?label_pt
        WHERE
        {
          ?district wdt:P31 """+districts_of+""" ;
                    wdt:P36 ?capital .
          ?capital rdfs:label ?label_pt .

          filter(lang(?label_pt) = 'pt')
          SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]". }
        }
        ORDER BY (?label_pt)
    """
    query_result = select_query( query )

    # new list with only the values from query result, names are not needed in this case
    result = []
    for e in query_result:
        result.append( e[1] )

    return result


def wikidata_modelo_info( modelo ):
    # modelos that have an image and if exists, their use label and image
    # returns dict to avoid repeated properties

    # modelos allowed
    for e in available_modelos:
        if modelo == e[0]:
            modelo = e[1]

    query = """
        SELECT  ?label_pt ?modeloDescription ?use_label ?use_image ?image
        WHERE
        {
          {
            ?modelo    rdfs:label  ?label_pt ;
                       wdt:P18     ?image filter (lang(?label_pt) = "pt") .
            }
          UNION
          {
            ?modelo    wdt:P366    ?use .
            ?use       rdfs:label  ?use_label ;
                       wdt:P18    ?use_image filter (lang(?use_label) = "pt") .
          }
          BIND( """+modelo+""" AS ?modelo )
          SERVICE wikibase:label { bd:serviceParam wikibase:language "pt". }
        }
    """
    query_result = select_query( query )

    result = {}
    for e in query_result:
        result.update( {e[0]: e[1]} )

    return result


def select_query( query ):
    # processes the query and returns a list of lists with the result of the query

    query_result = requests.get("https://query.wikidata.org/bigdata/namespace/wdq/sparql?query=" + query).text
    # print( str( query_result ) + '\n\n\n')

    root = etree.fromstring(query_result.encode('utf-8'))


    prefix = '{http://www.w3.org/2005/sparql-results#}'
    results = root.findall( './/' + prefix + 'result' )

    entities = []
    for result in results:
        binding = result.findall( prefix + 'binding' )

        for e in binding:

            name = e.attrib['name']

            entity = e.find( prefix + 'literal')
            if entity is not None:
                entities.append( [name, entity.text] )
            else:
                entity = e.find( prefix + 'uri')
                if entity is not None:
                    entities.append( [name, entity.text] )

    return entities
