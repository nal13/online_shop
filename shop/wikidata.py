from wikidata.client import Client
import requests
from lxml import etree
from pprint import pprint

available_countries = ( ('Portugal','wd:Q41806065'), ('Espanha','wd:Q162620'), ('Itália','wd:Q15089') )

p_logo_image = 'P154'
p_official_name = 'P1705'
p_country = 'P17'
p_population = 'P1082'
p_coordinate_location = 'P625'

def get_wikidata():

    query = wikidata_capitals( 'Portugal' )

    for e in query:
        pprint( e )
        # entity = Client().get( e )
        # property = Client().get( 'P17' )
        #
        # file = entity[ property ]
        # #
        # # url = file.image_url
        #
        # pprint(file)


def wikidata_query():
    #
    query = """
        SELECT ?modelLabel (SUM(?revenue) AS ?revenue)
        WHERE {
          ?model wdt:P31 wd:Q4830453 ,
                         wd:Q6881511 ;
                 wdt:P452 ?industry ;
                 wdt:P2139 ?revenue .
          FILTER(?industry IN (wd:Q56598901, wd:Q25245117, wd:Q5358497))
          SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]". }
        }
        GROUP BY ?modelLabel
        ORDER BY DESC(?revenue)
        LIMIT 10

    """
    return select_query( query )

def wikidata_capitals( country ):
    # capitals ordered by the most population

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
    return select_query( query )


def select_query( query ):
    query_result = requests.get("https://query.wikidata.org/bigdata/namespace/wdq/sparql?query=" + query).text

    root = etree.fromstring(query_result.encode('utf-8'))


    prefix = '{http://www.w3.org/2005/sparql-results#}'
    results = root.findall( './/' + prefix + 'result' )

    entities = []
    for r in results:
        result = r.findall( prefix + 'binding' )

        for e in result:
            # if we fetch the item identifier, we get a uri
            # if we fetch the label, we get the identifier as string, that's what we want
            entities.append(e.find( prefix + 'literal').text)

    return entities
