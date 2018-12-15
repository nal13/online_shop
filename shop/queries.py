
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


    def list_modelo_uri_nome(self):
        # uri and nome of all modelo
        query = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            SELECT ?uri ?nome
            WHERE {
                ?uri modelo:nome ?nome .
            }
            """
        return self.select_query( query )

    def list_modelo_a(self):
        # type of all modelo
        query = """
            SELECT DISTINCT ?type
            WHERE {
                ?s a ?type .
                FILTER ( regex(str(?s), "http://www.shop.pt/modelo/[0-9]+") )
            }
            """
        return self.select_query( query )

    def get_modelo_regular(self, id):
        # regular pred and obj of a given modelo, except if pred=[a, loja]
        query = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            SELECT ?pred ?obj
            WHERE {
                modelo:"""+id+""" ?pred ?obj .
                MINUS { ?s a ?obj }
                MINUS { ?s modelo:loja ?obj }
            }
            """
        return self.select_query( query )

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
        return self.select_query( query )

    #
    #not used atm
    #
    def list_modelo_marca(self):
        # marca of all modelo
        query = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            SELECT DISTINCT ?marca
            WHERE {
                ?s modelo:categoria ?marca .
            }
            """
        return self.select_query( query )

    def list_modelo_em_loja(self, id):
        # loja_uri, pred, obj and nome of all modelo_em_loja of a given modelo, LojaID is saved in loja_uri, not in obj
        query = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            PREFIX loja: <http://www.shop.pt/loja/>
            PREFIX modelo_em_loja: <http://www.shop.pt/modelo/loja/>
            SELECT ?loja_uri ?pred ?obj ?nome
            WHERE {
                modelo:"""+id+"""       modelo:loja                 ?modelo_em_loja_uri .
                ?modelo_em_loja_uri     modelo_em_loja:LojaID       ?loja_uri ;
                                        ?pred                       ?obj .
                ?loja_uri               loja:nome                   ?nome .

                MINUS { ?s modelo_em_loja:LojaID ?obj }
            }
            """
        return self.select_query( query )

    #
    #not used atm
    #
    def list_loja_uri_nome(self):
        # id and nome of all loja
        query = """
            PREFIX loja: <http://www.shop.pt/loja/>
            SELECT ?uri ?nome
            WHERE {
                ?uri loja:nome ?nome .
            }
            """
        return self.select_query( query )

    def get_loja_regular(self, id):
        # regular pred and obj of a given loja, except if pred=[a, morada, contacto]
        query = """
            PREFIX loja: <http://www.shop.pt/loja/>
            SELECT ?obj ?pred
            WHERE {
                loja:"""+id+""" ?pred ?obj .

                MINUS { ?s a ?obj }
                MINUS { ?s loja:morada ?obj }
                MINUS { ?s loja:contacto ?obj }
            }
            """
        return self.select_query( query )

    def get_loja_morada(self, id):
        # pred and obj of morada a given loja
        query = """
            PREFIX loja: <http://www.shop.pt/loja/>
            PREFIX morada: <http://www.shop.pt/morada/>
            SELECT ?obj ?pred
            WHERE {
                    loja:"""+id+""" loja:morada ?morada_uri .
                    ?morada_uri ?pred ?obj .

                    MINUS { ?s a ?obj }
            }
            """
        return self.select_query( query )

    def get_loja_contacto(self, id):
        # pred and obj of contacto a given loja
        query = """
            PREFIX loja: <http://www.shop.pt/loja/>
            PREFIX contacto: <http://www.shop.pt/contacto/>
            SELECT ?obj ?pred
            WHERE {
                    loja:"""+id+""" loja:contacto ?contacto_uri .
                    ?contacto_uri ?pred ?obj .

                    MINUS { ?s a ?obj }
            }
            """
        return self.select_query( query )

    #
    #not used atm
    #
    def get_loja_uri_max(self):
        # higher uri from all loja
        query = """
            PREFIX loja: <http://www.shop.pt/loja/>
            SELECT (max(?uri) as ?uri_max)
            WHERE {
                ?uri loja:nome ?o .
            }
            """
        return self.select_query( query )

    #
    #not used atm
    #
    def exists_loja_name(self, nome):
        # boolean exists_nome if any loja has nome==arg
        query = """
            PREFIX loja: <http://www.shop.pt/loja/>
            SELECT ?exists_nome
            WHERE {
                ?s loja:nome ?o .

                BIND( (?o = '"""+nome+"""' ) AS ?exists_nome )
            }
            """
        return self.select_query( query )

    #
    #not used atm
    #
    def add_loja(self, id, fields):

        nome = fields['nome']
        grupo = fields['grupo']
        detalhes = fields['detalhes']
        rua = fields['rua']
        codigopostal = fields['codigopostal']
        distrito = fields['distrito']
        pais = fields['pais']
        telefone = fields['telefone']
        fax = fields['fax']
        email = fields['email']
        website = fields['website']

        update = """
            PREFIX loja: <http://www.shop.pt/loja/>
            PREFIX morada: <http://www.shop.pt/morada/>
            PREFIX contacto: <http://www.shop.pt/contacto/>
            INSERT DATA {
                    loja:"""+id+"""     a                   loja: ;
                                        loja:nome           '"""+nome+"""' ;
                                        loja:grupo          '"""+grupo+"""' ;
                                        loja:morada         morada:"""+id+""" ;
                                        loja:contacto       contacto:"""+id+""" .
                    morada:"""+id+"""   a                   morada: ;
                                        morada:detalhes     '"""+detalhes+"""' ;
                                        morada:rua          '"""+rua+"""' ;
                                        morada:codigopostal '"""+codigopostal+"""' ;
                                        morada:distrito     '"""+distrito+"""' ;
                                        morada:pais         '"""+pais+"""' .
                    contacto:"""+id+""" a                   contacto: ;
                                        contacto:telefone   '"""+telefone+"""' ;
                                        contacto:fax        '"""+fax+"""' ;
                                        contacto:email      '"""+email+"""' ;
                                        contacto:website    '"""+website+"""' .
            }
            """
        return self.update_query( update )

    # def get_loja_morada_contacto(self, id):
    #     # all pred and obj of a given morada and contacto, except pred=a that is saved in ?m_type and c_type
    #     query = """
    #         PREFIX loja: <http://www.shop.pt/loja/>
    #         PREFIX morada: <http://www.shop.pt/morada/>
    #         PREFIX contacto: <http://www.shop.pt/contacto/>
    #         SELECT ?obj ?pred ?m_pred ?m_obj ?m_type ?c_pred ?c_obj ?c_type
    #         WHERE {
    #             {
    #                 loja:"""+id+""" loja:morada ?morada_id .
    #                 ?morada_id ?m_pred ?m_obj .
    #                 MINUS {
    #                     ?s a ?m_obj
    #                 }
    #                 ?morada_id a ?m_type .
    #             }
    #             UNION
    #             {
    #                 loja:"""+id+""" loja:contacto ?contacto_id .
    #                 ?contacto_id ?c_pred ?c_obj .
    #                 MINUS {
    #                     ?s a ?c_obj
    #                 }
    #                 ?contacto_id a ?c_type .
    #             }
    #         }
    #         """
    #     return self.select_query( query )

    def select_query( self, query ):
        payload_query = {"query": query}
        res = self.accessor.sparql_select(body=payload_query, repo_name=self.repo_name)

        return json.loads(res)

    def update_query( self, update ):
        payload_query = {"update": update}
        res = self.accessor.sparql_update(body=payload_query, repo_name=self.repo_name)

        # return json.loads(res)
