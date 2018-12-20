import json
from s4api.graphdb_api import GraphDBApi
from s4api.swagger import ApiClient
from pprint import pprint

class GraphDB:

    # start GraphDB
    def __init__(self):
        endpoint = "http://localhost:7200"
        self.repo_name = "shop"
        client = ApiClient(endpoint=endpoint)
        self.accessor = GraphDBApi(client)


#
#
#           GENERAL QUERIES
#
#
    def get_next_id(self, type):
        # get the highest uri of the type
        # allowed type: loja, modelo
        query = """
            PREFIX loja: <http://www.shop.pt/loja/>
            PREFIX modelo: <http://www.shop.pt/modelo/>
            SELECT (max(?uri) as ?uri_max)
            WHERE {
                ?uri    """+type+""":nome   ?o .
            }
            """
        query_result = self.select_query( query )

        for e in query_result['results']['bindings']:
            id_max = e['uri_max']['value'].split('/')[-1]

        return str( int(id_max)+1 )

#
#
#           MODELO QUERIES
#
#
    def list_modelo_random(self, limit):
        # list up to limit random modelos
        query = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            SELECT ?modelo_uri ?nome ?categoria ?preco
            WHERE {
                ?modelo_uri     modelo:nome         ?nome ;
                                modelo:categoria    ?categoria ;
                                modelo:preco        ?preco .
            }
            ORDER BY RAND() LIMIT """+limit+"""
            """
        return self.select_query( query )

    def list_modelo_uri_nome(self):
        # list uri and nome of all modelo
        query = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            SELECT ?uri ?nome
            WHERE {
                ?uri    modelo:nome  ?nome .
            }
            """
        return self.select_query( query )

    def list_modelo_by_categoria(self, categoria, order):
        # list all modelo of a given categoria by a given order

        if order == 'valiosos':
            order = 'ORDER BY DESC(xsd:decimal(?preco))'
        elif order == 'baratos':
            order = 'ORDER BY xsd:decimal(?preco)'

        query = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            SELECT ?uri ?nome ?preco
            WHERE {
                ?uri    modelo:categoria    '"""+categoria+"""' ;
                        modelo:nome         ?nome ;
                        modelo:preco        ?preco .
            }
            """+order
        return self.select_query( query )

    def list_modelo_a(self):
        # list type of all modelo
        query = """
            SELECT DISTINCT ?type
            WHERE {
                ?s  a   ?type .

                FILTER ( regex(str(?s), "http://www.shop.pt/modelo/[0-9]+") )
            }
            """
        return self.select_query( query )

    def get_modelo_regular(self, id):
        # get not nested pred and obj of a given modelo, except if pred=[a, loja]
        query = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            SELECT ?pred ?obj
            WHERE {
                modelo:"""+id+"""   ?pred   ?obj .

                MINUS { ?s a ?obj }
                MINUS { ?s modelo:loja ?obj }
            }
            """
        return self.select_query( query )

    def get_modelo_a(self, id):
        # get type of a given modelo
        query = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            SELECT ?type
            WHERE {
                modelo:"""+id+"""   a   ?type .
            }
            """
        return self.select_query( query )

    def get_modelo_loja_uri(self, nome, type):
        # get uri of a given modelo by its name
        query = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            PREFIX loja: <http://www.shop.pt/loja/>
            SELECT ?uri
            WHERE {
                ?uri    """+type+""":nome     '"""+nome+"""' .
            }
            """
        return self.select_query( query )

    def get_modelo_categoria(self, id):
        # get categoria of a given modelo
        query = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            SELECT ?categoria
            WHERE {
                modelo:"""+id+"""   modelo:categoria   ?categoria .
            }
            """
        return self.select_query( query )

    def list_modelo_em_loja(self, id):
        # list loja_uri, pred, obj and nome of all modelo_em_loja of a given modelo, LojaID is saved in loja_uri, not in obj
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

    def list_modelo_em_loja_unidades(self, id):
        # list loja_uri and units of a given loja
        query = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            PREFIX loja: <http://www.shop.pt/loja/>
            PREFIX modelo_em_loja: <http://www.shop.pt/modelo/loja/>
            SELECT ?loja_uri ?unidades
            WHERE {
                modelo:"""+id+"""       modelo:loja                 ?modelo_em_loja_uri .
                ?modelo_em_loja_uri     modelo_em_loja:LojaID       ?loja_uri ;
                                        modelo_em_loja:unidades     ?unidades .
            }
            """
        return self.select_query( query )

    def list_modelo_in_loja(self, id):
        # list up to 4 modelo from a given loja
        query = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            PREFIX modelo_em_loja: <http://www.shop.pt/modelo/loja/>
            PREFIX loja: <http://www.shop.pt/loja/>
            SELECT ?modelo_uri ?nome ?categoria ?preco
            WHERE {
                ?modelo_em_loja_uri     modelo_em_loja:LojaID       loja:"""+id+""" .
                ?modelo_uri             modelo:loja                 ?modelo_em_loja_uri ;
                                        modelo:nome                 ?nome ;
                                        modelo:categoria            ?categoria ;
                                        modelo:preco                ?preco .
            }
            ORDER BY RAND() LIMIT 4
            """
        return self.select_query( query )

    def list_modelo_by_a(self, id):
        # list up to 4 modelo with the same type as the given modelo
        query = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            SELECT ?modelo_uri ?nome ?categoria ?preco
            WHERE {
                modelo:"""+id+"""       a                   ?type .
                ?modelo_uri             a                   ?type ;
                                        modelo:nome         ?nome ;
                                        modelo:categoria    ?categoria ;
                                        modelo:preco        ?preco .
            }
            ORDER BY RAND() LIMIT 4
            """
        return self.select_query( query )

    def exists_modelo_name(self, nome):
        # get boolean that indicates if given modelo name exists in DB
        query = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            SELECT ?exists_nome
            WHERE {
                ?s  modelo:nome   ?o .

                BIND( (?o = '"""+nome+"""' ) AS ?exists_nome )
            }
            """
        return self.select_query( query )

    def add_modelo(self, id, fields, type):
        # insert modelo with the new highest id in DB
        nome = fields['nome']
        marca = fields['marca']
        categoria = fields['categoria']
        preco = str( fields['preco'] )

        if type == 'computador':
            type_characteristics = """
                modelo:ram                 '"""+fields['ram']+"""' ;
            	modelo:processador         '"""+fields['processador']+"""' ;
            	modelo:capacidadedisco     '"""+fields['capacidadedisco']+"""' ;
            	modelo:grafica             '"""+fields['grafica']+"""' ;
            	modelo:tamanhoecra         """+str( fields['tamanhoecra'] )+""" ;
            """
        elif type == 'telemovel':
            type_characteristics = """
            	modelo:ram                 '"""+fields['ram']+"""' ;
            	modelo:processador         '"""+fields['processador']+"""' ;
            	modelo:capacidadememoria   '"""+fields['capacidadememoria']+"""' ;
            	modelo:camara              '"""+fields['camara']+"""' ;
            	modelo:tamanhoecra         """+str( fields['tamanhoecra'] )+""" ;
            """
        elif type == 'tablet':
            type_characteristics = """
            	modelo:ram                 '"""+fields['ram']+"""' ;
            	modelo:processador         '"""+fields['processador']+"""' ;
            	modelo:capacidadememoria   '"""+fields['capacidadememoria']+"""' ;
            	modelo:camara              '"""+fields['camara']+"""' ;
            	modelo:tamanhoecra         """+str( fields['tamanhoecra'] )+""" ;
            """
        elif type == 'camara':
            type_characteristics = """
            	modelo:resolucaovideo      '"""+fields['resolucaovideo']+"""' ;
            	modelo:wireless            '"""+fields['wireless']+"""' ;
            	modelo:resolucaofoto       '"""+fields['resolucaofoto']+"""' ;
            """
        elif type == 'drone':
            type_characteristics = """
            	modelo:autonomia           '"""+fields['autonomia']+"""' ;
            	modelo:raio                '"""+fields['raio']+"""' ;
            	modelo:camaraimb           '"""+fields['camaraimb']+"""' ;
            """
        elif type == 'tv':
            type_characteristics = """
            	modelo:tamanhoecra         '"""+str( fields['tamanhoecra'] )+"""' ;
            	modelo:qualidadeimagem     '"""+fields['qualidadeimagem']+"""' ;
            	modelo:frequencia          '"""+fields['frequencia']+"""' ;
            """
        elif type == 'leitor_blueray':
            type_characteristics = """
            	modelo:formatosreproducao  '"""+fields['formatosreproducao']+"""' ;
            	modelo:resolucao           '"""+fields['resolucao']+"""' ;
            """
        elif type == 'maquina_cafe':
            type_characteristics = """
            	modelo:cor                 '"""+fields['cor']+"""' ;
            	modelo:agua                '"""+fields['agua']+"""' ;
            	modelo:potencia            '"""+fields['potencia']+"""' ;
            """
        elif type == 'microondas':
            type_characteristics = """
            	modelo:grill               '"""+fields['grill']+"""' ;
            	modelo:volumemax           '"""+fields['volumemax']+"""' ;
            	modelo:potenciamax         '"""+fields['potenciamax']+"""' ;
            """
        elif type == 'maquina_lavar_roupa':
            type_characteristics = """
            	modelo:eficiencia          '"""+fields['eficiencia']+"""' ;
            	modelo:capacidade          '"""+fields['capacidade']+"""' ;
            	modelo:velocidadecen       '"""+fields['velocidadecen']+"""' ;
            """
        elif type == 'maquina_secar_roupa':
            type_characteristics = """
            	modelo:eficiencia          '"""+fields['eficiencia']+"""' ;
            	modelo:capacidade          '"""+fields['capacidade']+"""' ;
            	modelo:consumo             '"""+fields['consumo']+"""' ;
            """
        elif type == 'aspirador':
            type_characteristics = """
            	modelo:potenciamax         '"""+fields['potenciamax']+"""' ;
            	modelo:volumemaxdep        '"""+fields['volumemaxdep']+"""' ;
            """
        elif type == 'gaming_pc':
            type_characteristics = """
            	modelo:ram                 '"""+fields['ram']+"""' ;
            	modelo:processador         '"""+fields['processador']+"""' ;
            	modelo:capacidadedisco     '"""+fields['capacidadedisco']+"""' ;
            	modelo:grafica             '"""+fields['grafica']+"""' ;
            	modelo:tamanhoecra         """+str( fields['tamanhoecra'] )+""" ;
            """
        elif type == 'consola':
            type_characteristics = """
            	modelo:capacidadedisco     '"""+fields['capacidadedisco']+"""' ;
            	modelo:cor                 '"""+fields['cor']+"""' ;
            	modelo:jogoincluido        '"""+fields['jogoincluido']+"""' ;
            """
        elif type == 'jogo':
            type_characteristics = ''

        # produces triples for each modelo_em_loja
        query = self.list_loja_uri_nome()

        modelo_em_loja = []
        for e in query['results']['bindings']:
            loja_id = e['uri']['value'].split('/')[-1]
            unidades = 'unidades_'+loja_id

            em_loja_id = id + loja_id

            if fields[unidades]>0 :
                modelo_em_loja.append("""
                    modelo:"""+id+"""                   modelo:loja                 modelo_em_loja:"""+em_loja_id+""" .
                    modelo_em_loja:"""+em_loja_id+"""   modelo_em_loja:LojaID       loja:"""+loja_id+""" ;
                                                        modelo_em_loja:unidades     '"""+str( fields[unidades] )+"""' .
                """)

        update = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            PREFIX modelo_em_loja: <http://www.shop.pt/modelo/loja/>
            PREFIX loja: <http://www.shop.pt/loja/>
            PREFIX computador: <http://www.shop.pt/computador/>
            PREFIX telemovel: <http://www.shop.pt/telemovel/>
            PREFIX tablet: <http://www.shop.pt/tablet/>
            PREFIX camara: <http://www.shop.pt/camara/>
            PREFIX drone: <http://www.shop.pt/drone/>
            PREFIX tv: <http://www.shop.pt/tv/>
            PREFIX leitor_blueray: <http://www.shop.pt/leitor_blueray/>
            PREFIX maquina_cafe: <http://www.shop.pt/maquina_cafe/>
            PREFIX microondas: <http://www.shop.pt/microondas/>
            PREFIX maquina_lavar_roupa: <http://www.shop.pt/maquina_lavar_roupa/>
            PREFIX maquina_secar_roupa: <http://www.shop.pt/maquina_secar_roupa/>
            PREFIX aspirador: <http://www.shop.pt/aspirador/>
            PREFIX gaming_pc: <http://www.shop.pt/gaming_pc/>
            PREFIX consola: <http://www.shop.pt/consola/>
            PREFIX jogo: <http://www.shop.pt/jogo/>
            INSERT DATA {
                    modelo:"""+id+"""   a                   """+type+""": ;
                                        modelo:nome         '"""+nome+"""' ;
                                        modelo:marca        '"""+marca+"""' ;
                                        modelo:categoria    '"""+categoria+"""' ;
                                        """+type_characteristics+"""
                                        modelo:preco        '"""+preco+"""' .
                                        """+''.join(modelo_em_loja)+"""
            }
            """
        self.update_query( update )

    def remove_modelo(self, id):
        # delete modelo with id from DB
        update = """
            PREFIX modelo: <http://www.shop.pt/modelo/>
            PREFIX modelo_em_loja: <http://www.shop.pt/modelo/loja/>
            DELETE WHERE {
                            modelo:"""+id+"""       modelo:loja     ?modelo_em_loja_uri .
                            ?modelo_em_loja_uri     ?p              ?o .
            } ;
            DELETE WHERE {  modelo:"""+id+"""       ?p              ?o . }
            """
        self.update_query( update )


#
#
#           MODELO QUERIES
#
#
    def list_loja_uri_nome(self):
        # list id and nome of all loja
        query = """
            PREFIX loja: <http://www.shop.pt/loja/>
            SELECT ?uri ?nome
            WHERE {
                ?uri    loja:nome   ?nome .
            }
            """
        return self.select_query( query )

    def get_loja_regular(self, id):
        # get not nested pred and obj of a given loja, except if pred=[a, morada, contacto]
        query = """
            PREFIX loja: <http://www.shop.pt/loja/>
            SELECT ?obj ?pred
            WHERE {
                loja:"""+id+""" ?pred   ?obj .

                MINUS { ?s a ?obj }
                MINUS { ?s loja:morada ?obj }
                MINUS { ?s loja:contacto ?obj }
            }
            """
        return self.select_query( query )

    def get_loja_morada(self, id):
        # get pred and obj of morada a given loja
        query = """
            PREFIX loja: <http://www.shop.pt/loja/>
            PREFIX morada: <http://www.shop.pt/morada/>
            SELECT ?obj ?pred
            WHERE {
                    loja:"""+id+""" loja:morada ?morada_uri .
                    ?morada_uri     ?pred       ?obj .

                    MINUS { ?s a ?obj }
            }
            """
        return self.select_query( query )

    def get_loja_contacto(self, id):
        # get pred and obj of contacto a given loja
        query = """
            PREFIX loja: <http://www.shop.pt/loja/>
            PREFIX contacto: <http://www.shop.pt/contacto/>
            SELECT ?obj ?pred
            WHERE {
                    loja:"""+id+""" loja:contacto   ?contacto_uri .
                    ?contacto_uri   ?pred           ?obj .

                    MINUS { ?s a ?obj }
            }
            """
        return self.select_query( query )

    def exists_loja_name(self, nome):
        # get boolean that indicates if given loja name exists in DB
        query = """
            PREFIX loja: <http://www.shop.pt/loja/>
            SELECT ?exists_nome
            WHERE {
                ?s  loja:nome   ?o .

                BIND( (?o = '"""+nome+"""' ) AS ?exists_nome )
            }
            """
        return self.select_query( query )

    def add_loja(self, id, fields):
        # insert loja with the new highest id in DB
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
        self.update_query( update )

    def remove_loja(self, id):
        # delete loja with id from DB
        update = """
            PREFIX loja: <http://www.shop.pt/loja/>
            PREFIX morada: <http://www.shop.pt/morada/>
            PREFIX contacto: <http://www.shop.pt/contacto/>
            DELETE WHERE {     loja:"""+id+"""        ?p          ?o . } ;
            DELETE WHERE {     morada:"""+id+"""      ?p          ?o . } ;
            DELETE WHERE {     contacto:"""+id+"""    ?p          ?o . } ;
            """
        self.update_query( update )

    def remove_loja_links(self, id):
        # delete all modelo_em_loja that linked to a given loja
        update = """
            PREFIX loja: <http://www.shop.pt/loja/>
            PREFIX modelo: <http://www.shop.pt/modelo/>
            PREFIX modelo_em_loja: <http://www.shop.pt/modelo/loja/>
            DELETE WHERE {
                ?s      modelo_em_loja:LojaID   loja:"""+id+""" ;
                        ?p                      ?o .
                ?s2     modelo:loja             ?s .
            } ;
            """
        self.update_query( update )


    # query processing
    def select_query( self, query ):
        payload_query = {"query": query}
        res = self.accessor.sparql_select(body=payload_query, repo_name=self.repo_name)

        if res.__contains__('Exception') or res.__contains__('MALFORMED'):
            pprint(res)

        return json.loads(res)

    def update_query( self, update ):
        payload_query = {"update": update}
        res = str( self.accessor.sparql_update(body=payload_query, repo_name=self.repo_name) )

        if res.__contains__('Exception') or res.__contains__('MALFORMED'):
            pprint(res)
