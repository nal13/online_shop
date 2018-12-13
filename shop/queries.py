
import json
from s4api.graphdb_api import GraphDBApi
from s4api.swagger import ApiClient

class GraphDB:

    # upload rdf file to repository
    def __init__(self):
        endpoint = "http://localhost:7200"
        self.repo_name = "shop"
        client = ApiClient(endpoint=endpoint)
        self.accessor = GraphDBApi(client)

    def list_modelo_nome(self):
        query = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            SELECT ?nome ?id
            WHERE {
                ?id modelo:nome ?nome .
            }
            """
        return self.run_query( query )

    def get_modelo(self, id):
        # all pred and obj of a given modelo, except if pred=a or pred=loja
        query = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            SELECT ?pred ?obj
            WHERE {
                modelo:"""+id+""" ?pred ?obj .
                MINUS {
                    modelo:"""+id+""" a ?obj
                }
                MINUS {
                    modelo:"""+id+""" modelo:loja ?obj
                }
            }
            """
        return self.run_query( query )

    #
    #not used atm
    #
    def get_modelo_a(self, id):
        # type of a given modelo
        query = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            SELECT DISTINCT ?type
            WHERE {
                modelo:"""+id+""" a ?type .
            }
            """
        return self.run_query( query )

    #
    #not used atm
    #
    def list_modelo_marca(self):
        # marca of all modelo
        query = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            SELECT DISTINCT ?marca
            WHERE {
                ?sub modelo:categoria ?marca .
            }
            """
        return self.run_query( query )

    def list_modelo_a(self):
        # type of all modelo
        query = """
            SELECT DISTINCT ?type
            WHERE {
                ?sub a ?type .
                FILTER ( regex(str(?sub), "http://www.shop.pt/modelo/[0-9]+") )
            }
            """
        return self.run_query( query )

    def list_modelo_em_loja(self, id):
        query = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            PREFIX loja: <http://www.shop.pt/loja/>
            PREFIX modelo_em_loja: <http://www.shop.pt/modelo/loja/>
            SELECT ?nome
            WHERE {
                modelo:"""+id+""" modelo:loja ?modelo_em_loja .
                ?modelo_em_loja modelo_em_loja:LojaID ?loja_id .
                ?loja_id loja:nome ?nome .
            }
            """
        return self.run_query( query )

    #
    #not used atm
    #
    def list_loja_nome(self):
        query = """
            PREFIX loja: <http://www.shop.pt/loja/>
            SELECT ?nome ?id
            WHERE {
                ?id loja:nome ?nome .
            }
            """
        return self.run_query( query )


    def run_query( self, query ):
        payload_query = {"query": query}
        res = self.accessor.sparql_select(body=payload_query, repo_name=self.repo_name)
        res = json.loads(res)
        # result = []

        # for e in res['results']['bindings']:
        #     for ee in e:
        #         print({ee:e[ee]['value']})
        #         # result.append({ee:e[ee]['value']})
        # print('\n\n')
        return res
