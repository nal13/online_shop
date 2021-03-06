from django import forms
from pprint import pprint
import re

from .constants import g
from .wikidata import available_countries, wikidata_capitals


class SearchForm(forms.Form):
    search_type = forms.ChoiceField(
        required=True,
        choices=[
        ('modelo','Modelo'),
        ('loja','Loja'), ],
        widget=forms.Select(attrs={'class':'input-select'})
    )
    search_box = forms.CharField(
        required=False,
        min_length=4,
        max_length=40,
        widget=forms.TextInput(attrs={'class':'input', 'placeholder': 'Pesquise por um modelo ou loja'})
    )


class OrderForm(forms.Form):
    order = forms.ChoiceField(
        label='Ordenar por',
        required=True,
        choices=[
        ('a-z','A-Z'),
        ('z-a','Z-A'),
        ('valiosos','Valiosos'),
        ('baratos','Baratos'),
        # ('Recomendados','Recomendados'),
        # ('Novos Produtos','Novos Produtos'),
        # ('Ultimas Unidades','Ultimas Unidades'),
        ],
        widget=forms.Select(attrs={'class':'input-select', 'onchange':'this.form.submit()'})
    )


class LojaForm(forms.Form):

    def __init__(self, *args, **kwargs):

        # if bool(kwargs):
            # kwargs not empty
        country = kwargs.pop('load')

        super(LojaForm, self).__init__(*args, **kwargs)

        self.populate_choices( country )

        self.fields['nome'] = forms.CharField(
            label='Nome',
            required=True,
            initial='Nova Loja',
            min_length=4,
            max_length=40,
            widget=forms.TextInput(attrs={'class':'input'})
        )
        self.fields['grupo'] = forms.ChoiceField(
            label='Grupo',
            required=True,
            choices=Lvars().grupo,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['detalhes'] = forms.CharField(
            label='Detalhes',
            required=True,
            initial='Novos Detalhes',
            min_length=4,
            max_length=40,
            widget=forms.TextInput(attrs={'class':'input'})
        )
        self.fields['rua'] = forms.CharField(
            label='Rua',
            required=True,
            initial='Nova Rua',
            min_length=4,
            max_length=40,
            widget=forms.TextInput(attrs={'class':'input'})
        )
        self.fields['codigopostal'] = forms.CharField(
            label='Codigo Postal',
            required=True,
            initial='9999-999',
            min_length=8,
            max_length=8,
            widget=forms.TextInput(attrs={'class':'input'})
        )
        self.fields['pais'] = forms.ChoiceField(
            label='País',
            required=True,
            choices=Lvars().pais,
            widget=forms.Select(attrs={'class':'input', 'onchange':'this.form.submit()'})
        )
        self.fields['distrito'] = forms.ChoiceField(
            label='Distrito',
            required=True,
            choices=Lvars().distrito,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['telefone'] = forms.CharField(
            label='Telefone',
            required=True,
            initial='+351 000 000 000',
            min_length=9,
            max_length=16,
            widget=forms.TextInput(attrs={'class':'input'})
        )
        self.fields['fax'] = forms.CharField(
            label='Fax',
            required=False,
            min_length=9,
            max_length=16,
            widget=forms.TextInput(attrs={'class':'input'})
        )
        self.fields['email'] = forms.EmailField(
            label='Email',
            required=True,
            initial='shop@mail.com',
            min_length=4,
            max_length=40,
            widget=forms.EmailInput(attrs={'class':'input'})
        )
        self.fields['website'] = forms.CharField(
            label='Website',
            required=False,
            min_length=4,
            max_length=40,
            widget=forms.TextInput(attrs={'class':'input'})
        )


    def populate_choices(self, country):

        # populate distrito
        if country is None:
            country = 'Portugal'
        capitals = wikidata_capitals( country )

        Lvars.distrito.clear()
        for e in capitals:
            Lvars().distrito.append( (e,e) )

        # populate pais
        Lvars.pais.clear()
        for e in available_countries:
            e_country = e[0]
            tuple = (e_country, e_country)

            if e_country == country:
                Lvars().pais.insert( 0, tuple )
            else:
                Lvars().pais.append( tuple )


    def set_initial_values(self, initial_fields):
        # populate forms with initial_fields

        for field in self.fields:

            initial_value = initial_fields.get( field )
            field_type = self.fields[field].__class__.__name__

            # the regular way to set 'initial' doesn't seem to work to ChoiceField,
            # so here a way a around it
            if field_type is 'ChoiceField':

                if field == 'distrito':
                    capitals_list = wikidata_capitals( self.fields['pais'].choices[0][0] )
                    capitals = []
                    for e in capitals_list:
                        capitals.append( (e, e) )

                    self.fields[field].choices =  capitals

                initial_choice = (initial_value, initial_value)
                self.fields[field].choices.remove( initial_choice )
                self.fields[field].choices = [initial_choice] + self.fields[field].choices

            elif field_type is 'DecimalField':
                self.fields[field].initial = float(initial_value)

            elif field_type is 'IntegerField':
                self.fields[field].initial = int(initial_value)

            elif field_type is 'CharField' or field_type is 'EmailField':
                self.fields[field].initial = initial_value

            else:
                print('\n\n\nSET THIS INITIAL FIELD DATA\n\n\n')


class Lvars:
    # loja form constants
    grupo = [('Media Markt','Media Markt'), ]
    pais = []
    distrito = []


class ModeloForm(forms.Form):

    def __init__(self, type, *args, **kwargs):
        super(ModeloForm, self).__init__(*args, **kwargs)

        self.type = type

        self.fields['nome'] = forms.CharField(
            label='Nome',
            required=True,
            initial='Novo Produto',
            min_length=4,
            max_length=40,
            widget=forms.TextInput(attrs={'class':'input'})
        )
        self.fields['marca'] = forms.ChoiceField(
            label='Marca',
            required=True,
            choices=Mvars().marca,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['categoria'] = forms.ChoiceField(
            label='Categoria',
            required=True,
            choices=Mvars().categoria,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['preco'] = forms.DecimalField(
            label='Preco',
            required=True,
            initial='1.00',
            min_value=1,
            max_value=9999,
            max_digits=6,
            decimal_places=2,
            widget=forms.NumberInput(attrs={'class':'input', 'step': 0.25})
        )

        if type=='computador':
            self.computador()
        elif type=='telemovel':
            self.telemovel()
        elif type=='tablet':
            self.tablet()
        elif type=='camara':
            self.camara()
        elif type=='drone':
            self.drone()
        elif type=='tv':
            self.tv()
        elif type=='leitor_blueray':
            self.leitorblueray()
        elif type=='maquina_cafe':
            self.maquinacafe()
        elif type=='microondas':
            self.microondas()
        elif type=='maquina_lavar_roupa':
            self.maquinalavarroupa()
        elif type=='maquina_secar_roupa':
            self.maquinasecarroupa()
        elif type=='aspirador':
            self.aspirador()
        elif type=='gaming_pc':
            self.gamingpc()
        elif type=='consola':
            self.consola()
        elif type=='jogo':
            pass

        # create forms for each loja in DB
        query = g.list_loja_uri_nome()

        for e in query:
            id = g.get_value( e, 'uri' )
            nome = g.get_value( e, 'nome' )
            self.fields.update({
                'unidades_%s' % id: forms.IntegerField(
                                                label='Unidades em %s' % nome,
                                                required=False,
                                                initial=0,
                                                min_value=0,
                                                widget=forms.NumberInput(attrs={'class':'input', })
                                                ),
            })


    def set_initial_values(self, initial_fields,  id):
        # populate forms with initial_fields

        for field in self.fields:

            # dynamic forms
            if re.compile('_[0-9]+').search(field):

                query = g.list_modelo_em_loja_unidades(id)
                initial_value = 0

                loja_id = g.get_value( e, 'loja_uri' )
                for e in query:
                    unidades = g.get_value( e, 'unidades' )
                    if loja_id in field:
                        initial_value = unidades
            # static forms
            else:
                initial_value = initial_fields.get( field )

            field_type = self.fields[field].__class__.__name__

            # the regular way to set 'initial' doesn't seem to work to ChoiceField,
            # so here's a way a around it
            if field_type is 'ChoiceField':
                initial_choice = (initial_value, initial_value)
                self.fields[field].choices.remove( initial_choice )
                self.fields[field].choices = [initial_choice] + self.fields[field].choices

            elif field_type is 'DecimalField':
                self.fields[field].initial = float(initial_value)

            elif field_type is 'IntegerField':
                self.fields[field].initial = int(initial_value)

            elif field_type is 'CharField' or field_type is 'EmailField':
                self.fields[field].initial = initial_value

            else:
                print('\n\n\nSET THIS INITIAL FIELD DATA\n\n\n')

    def computador(self):
        self.fields['ram'] = forms.ChoiceField(
            label='Ram',
            required=True,
            choices=Mvars().computador_ram,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['processador'] = forms.ChoiceField(
            label='Processador',
            required=True,
            choices=Mvars().computador_processador,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['capacidadedisco'] = forms.ChoiceField(
            label='Capacidade do Disco',
            required=True,
            choices=Mvars().computador_capacidadedisco,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['grafica'] = forms.ChoiceField(
            label='Gráfica',
            required=True,
            choices=Mvars().computador_grafica,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['tamanhoecra'] = forms.DecimalField(
            label='Tamanho do Ecrã',
            required=True,
            initial='1.00',
            min_value=1,
            max_value=9999,
            max_digits=6,
            decimal_places=2,
            widget=forms.NumberInput(attrs={'class':'input', 'step': 0.25})
        )

    def telemovel(self):
        self.fields['ram'] = forms.ChoiceField(
            label='Ram',
            required=True,
            choices=Mvars().telemovel_ram,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['processador'] = forms.ChoiceField(
            label='Processador',
            required=True,
            choices=Mvars().telemovel_processador,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['capacidadememoria'] = forms.ChoiceField(
            label='Capacidade de Memória',
            required=True,
            choices=Mvars().telemovel_capacidadememoria,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['camara'] = forms.ChoiceField(
            label='Câmara',
            required=True,
            choices=Mvars().telemovel_camara,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['tamanhoecra'] = forms.DecimalField(
            label='Tamanho do Ecrã',
            required=True,
            initial='1.00',
            min_value=1,
            max_value=9999,
            max_digits=6,
            decimal_places=2,
            widget=forms.NumberInput(attrs={'class':'input', 'step': 0.25})
        )

    def tablet(self):
        self.fields['ram'] = forms.ChoiceField(
            label='Ram',
            required=True,
            choices=Mvars().tablet_ram,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['processador'] = forms.ChoiceField(
            label='Processador',
            required=True,
            choices=Mvars().tablet_processador,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['capacidadememoria'] = forms.ChoiceField(
            label='Capacidade de Memória',
            required=True,
            choices=Mvars().tablet_capacidadememoria,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['camara'] = forms.ChoiceField(
            label='Câmara',
            required=True,
            choices=Mvars().tablet_camara,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['tamanhoecra'] = forms.DecimalField(
            label='Tamanho do Ecrã',
            required=True,
            initial='1.00',
            min_value=1,
            max_value=9999,
            max_digits=6,
            decimal_places=2,
            widget=forms.NumberInput(attrs={'class':'input', 'step': 0.25})
        )

    def camara(self):
        self.fields['resolucaovideo'] = forms.ChoiceField(
            label='Resolução de Vídeo',
            required=True,
            choices=Mvars().camara_resolucaovideo,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['wireless'] = forms.ChoiceField(
            label='Wireless',
            required=True,
            choices=Mvars.boolean,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['resolucaofoto'] = forms.ChoiceField(
            label='Resolução de Foto',
            required=True,
            choices=Mvars().camara_resolucaofoto,
            widget=forms.Select(attrs={'class':'input'})
        )

    def drone(self):
        self.fields['autonomia'] = forms.ChoiceField(
            label='Autonomia',
            required=True,
            choices=Mvars().drone_autonomia,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['raio'] = forms.ChoiceField(
            label='Raio',
            required=True,
            choices=Mvars().drone_raio,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['camaraimb'] = forms.ChoiceField(
            label='Camara Imb',
            required=True,
            choices=Mvars.boolean,
            widget=forms.Select(attrs={'class':'input'})
        )

    def tv(self):
        self.fields['tamanhoecra'] = forms.DecimalField(
            label='Tamanho do Ecrã',
            required=True,
            initial='1.00',
            min_value=1,
            max_value=9999,
            max_digits=6,
            decimal_places=2,
            widget=forms.NumberInput(attrs={'class':'input', 'step': 0.25})
        )
        self.fields['qualidadeimagem'] = forms.ChoiceField(
            label='Qualidade de Imagem',
            required=True,
            choices=Mvars().tv_qualidadeimagem,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['frequencia'] = forms.ChoiceField(
            label='Frequência',
            required=True,
            choices=Mvars().tv_frequencia,
            widget=forms.Select(attrs={'class':'input'})
        )

    def leitorblueray(self):
        self.fields['formatosreproducao'] = forms.ChoiceField(
            label='Formatos de Reprodução',
            required=True,
            choices=Mvars().leitorblueray_formatosreproducao,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['resolucao'] = forms.ChoiceField(
            label='Resolução',
            required=True,
            choices=Mvars().leitorblueray_resolucao,
            widget=forms.Select(attrs={'class':'input'})
        )

    def maquinacafe(self):
        self.fields['cor'] = forms.ChoiceField(
            label='Cor',
            required=True,
            choices=Mvars().maquinacafe_cor,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['agua'] = forms.ChoiceField(
            label='Água',
            required=True,
            choices=Mvars().maquinacafe_agua,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['potencia'] = forms.ChoiceField(
            label='Potência',
            required=True,
            choices=Mvars().maquinacafe_potencia,
            widget=forms.Select(attrs={'class':'input'})
        )

    def microondas(self):
        self.fields['grill'] = forms.ChoiceField(
            label='Grill',
            required=True,
            choices=Mvars.boolean,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['volumemax'] = forms.ChoiceField(
            label='Volume Máximo',
            required=True,
            choices=Mvars().microndas_volumemax,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['potenciamax'] = forms.ChoiceField(
            label='Potência Máxima',
            required=True,
            choices=Mvars().microndas_potenciamax,
            widget=forms.Select(attrs={'class':'input'})
        )

    def maquinalavarroupa(self):
        self.fields['eficiencia'] = forms.ChoiceField(
            label='Eficiencia',
            required=True,
            choices=Mvars().maquinalavarroupa_eficiencia,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['capacidade'] = forms.ChoiceField(
            label='Capacidade',
            required=True,
            choices=Mvars().maquinalavarroupa_capacidade,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['velocidadecen'] = forms.ChoiceField(
            label='Velocidade Centrífuga',
            required=True,
            choices=Mvars().maquinalavarroupa_velocidadecen,
            widget=forms.Select(attrs={'class':'input'})
        )

    def maquinasecarroupa(self):
        self.fields['eficiencia'] = forms.ChoiceField(
            label='Eficiencia',
            required=True,
            choices=Mvars().maquinasecarroupa_eficiencia,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['capacidade'] = forms.ChoiceField(
            label='Capacidade',
            required=True,
            choices=Mvars().maquinasecarroupa_capacidade,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['consumo'] = forms.ChoiceField(
            label='Consumo',
            required=True,
            choices=Mvars().maquinasecarroupa_consumo,
            widget=forms.Select(attrs={'class':'input'})
        )

    def aspirador(self):
        self.fields['potenciamax'] = forms.ChoiceField(
            label='Potência Máxima',
            required=True,
            choices=Mvars().aspirador_potenciamax,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['volumemaxdep'] = forms.ChoiceField(
            label='Volume Máximo do Depósito',
            required=True,
            choices=Mvars().aspirador_volumemaxdep,
            widget=forms.Select(attrs={'class':'input'})
        )

    def gamingpc(self):
        self.fields['ram'] = forms.ChoiceField(
            label='Ram',
            required=True,
            choices=Mvars().gamingpc_ram,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['processador'] = forms.ChoiceField(
            label='Processador',
            required=True,
            choices=Mvars().gamingpc_processador,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['capacidadedisco'] = forms.ChoiceField(
            label='Capacidade do Disco',
            required=True,
            choices=Mvars().gamingpc_capacidadedisco,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['grafica'] = forms.ChoiceField(
            label='Gráfica',
            required=True,
            choices=Mvars().gamingpc_grafica,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['tamanhoecra'] = forms.DecimalField(
            label='Tamanho do Ecrã',
            required=True,
            initial='1.00',
            min_value=1,
            max_value=9999,
            max_digits=6,
            decimal_places=2,
            widget=forms.NumberInput(attrs={'class':'input', 'step': 0.25})
        )

    def consola(self):
        self.fields['cor'] = forms.ChoiceField(
            label='Cor',
            required=True,
            choices=Mvars().consola_cor,
            widget=forms.Select(attrs={'class':'input'})
        )
        self.fields['jogoincluido'] = forms.ChoiceField(
            label='Jogo Incluido',
            required=True,
            choices=Mvars().consola_jogoincluido,
            widget=forms.Select(attrs={'class':'input'})
        )


class Mvars:
    # modelo form constants
    boolean = [
        ('Sim', 'Sim'), ('Nao', 'Nao'),
    ]
    marca = [
        ('Asus', 'Asus'), ('HP', 'HP'), ('LeNovo', 'LeNovo'), ('Xiaomi', 'Xiaomi'), ('Apple', 'Apple'), ('Huawei', 'Huawei'),
        ('Canon', 'Canon'), ('Nikon', 'Nikon'), ('Parrot', 'Parrot'), ('Silver', 'Silver'), ('LG', 'LG'), ('Sony', 'Sony'),
        ('Nespresso', 'Nespresso'), ('Delta', 'Delta'), ('Samsung', 'Samsung'), ('Flama', 'Flama'), ('Whirlpoll', 'Whirlpoll'),
        ('Hotpoint', 'Hotpoint'), ('Indesit', 'Indesit'), ('Bosh', 'Bosh'), ('IronBot', 'IronBot'), ('Hoover', 'Hoover'),
        ('Rowenta', 'Rowenta'), ('Microsoft', 'Microsoft'), ('Nintendo', 'Nintendo'), ('PS4', 'PS4'), ('XBOX', 'XBOX'), ('SWITCH', 'SWITCH')
    ]
    categoria = [
        ('tecnologia_movel', 'tecnologia_movel'), ('fotografia', 'fotografia'), ('tecnologia_de_casa', 'tecnologia_de_casa'),
        ('cozinha', 'cozinha'), ('limpeza', 'limpeza'), ('videojogos', 'videojogos')
    ]

    computador_ram = [('1 GB','1 GB'), ('2 GB','2 GB'), ('3 GB','3 GB'), ('4 GB','4 GB'), ('8 GB','8 GB'), ('12 GB','12 GB'), ('16 GB','16 GB'), ('32 GB','32 GB'), ]
    computador_processador = [('i5-7200U 2.5GHz','i5-7200U 2.5GHz'), ('i7-8550U 1.8GHz','i7-8550U 1.8GHz'), ('i3-7020U 2.3GHz','i3-7020U 2.3GHz'), ('i5-825OU 1.6 GHz','i5-825OU 1.6 GHz'), ('i7-855OU 1.8 GHz','i7-855OU 1.8 GHz'), ('i5-825OU 1.6 GHz','i5-825OU 1.6 GHz'), ]
    computador_capacidadedisco = [('128 GB','128 GB'), ('256 GB','256 GB'), ('512 GB','512 GB'), ('1024 GB','1024 GB'), ('2048 GB','2048 GB'), ]
    computador_grafica = [('Radeon R5 530 2GB','Radeon R5 530 2GB'), ('HD Graphics 620','HD Graphics 620'), ('HD Graphics 620','HD Graphics 620'), ('GeForce MX110 2GB','GeForce MX110 2GB'), ('Radeon R5 530 2GB','Radeon R5 530 2GB'), ]

    telemovel_ram =  [('1 GB','1 GB'), ('2 GB','2 GB'), ('3 GB','3 GB'), ('4 GB','4 GB'), ('8 GB','8 GB'), ('12 GB','12 GB'), ('16 GB','16 GB'), ('32 GB','32 GB'), ]
    telemovel_processador = [('Quad-Core 2.0 GHz Cortex-A53','Quad-Core 2.0 GHz Cortex-A53'), ('Octa-core 2.0 GHz Cortex-A53','Octa-core 2.0 GHz Cortex-A53'), ('Hexa-core A12 Bionic','Hexa-core A12 Bionic'), ('Quad-core 2.23 GHz A10 Fusion','Quad-core 2.23 GHz A10 Fusion'), ('Octa-core(4x 2.36 GHz + 4x 1.7 GHz)','Octa-core(4x 2.36 GHz + 4x 1.7 GHz)'), ]
    telemovel_capacidadememoria = [('8 GB','8 GB'), ('16 GB','16 GB'), ('32 GB','32 GB'), ('64 GB','64 GB'), ('128 GB','128 GB'), ]
    telemovel_camara = [('12 MP','12 MP'), ('13 MP','13 MP'), ('Dual(12 MP + 5MP)','Dual(12 MP + 5MP)'), ('DUAL(16 MP + 2 MP)','DUAL(16 MP + 2 MP)'), ]

    tablet_ram = [('1 GB','1 GB'), ('2 GB','2 GB'), ('3 GB','3 GB'), ('4 GB','4 GB'), ('8 GB','8 GB'), ('16 GB','16 GB'), ('32 GB','32 GB'), ]
    tablet_processador = [('Quad-core 1.3 GHz','Quad-core 1.3 GHz'), ('Quad-Core 1.4 GHz','Quad-Core 1.4 GHz'), ('Dual-Core A10 Fusion','Dual-Core A10 Fusion'), ('Dual-core A10X Fusion','Dual-core A10X Fusion'), ('Quad-Core 1.4 GHz Snapdragon 425','Quad-Core 1.4 GHz Snapdragon 425'), ]
    tablet_capacidadememoria = [('8 GB','8 GB'), ('16 GB','16 GB'), ('32 GB','32 GB'), ('64 GB','64 GB'), ('128 GB','128 GB'), ]
    tablet_camara = [('2 MP','2 MP'), ('5 MP + 2 MP','5 MP + 2 MP'), ('8 MP + 1.2 MP','8 MP + 1.2 MP'), ('12 MP + 7 MP','12 MP + 7 MP'), ]

    camara_resolucaovideo = [('Full HD 1080p','Full HD 1080p'), ('UHD 4K','UHD 4K'), ]
    camara_resolucaofoto = [('16 MP','16 MP'), ('18 MP','18 MP'), ('20 MP','20 MP'), ('22 MP','22 MP'), ('24 MP','24 MP'), ('26 MP','26 MP'), ]

    drone_autonomia = [('Ate 9 min','Ate 9 min'), ('Ate 15 min','Ate 15 min'), ('Ate 25 min','Ate 25 min'), ]
    drone_raio = [('200 m','200 m'), ('300 m','300 m'), ]

    tv_qualidadeimagem = [('HD','HD'), ('HD 720p','HD 720p'), ('UHD 4K','UHD 4K'), ]
    tv_frequencia = [('50 Hz','50 Hz'), ('60 Hz','60 Hz'), ('100 Hz','100 Hz'), ]

    leitorblueray_formatosreproducao = [('BD,CD,DVD','BD,CD,DVD'), ]
    leitorblueray_resolucao = [('Full HD 1080p','Full HD 1080p'), ('4K','4K'), ]

    maquinacafe_cor = [('Branco','Branco'), ('Preto','Preto'), ('Vermelho','Vermelho'), ('Verde','Verde'), ('Azul','Azul'), ('Castanho','Castanho'), ]
    maquinacafe_agua = [('0.8 L','0.8 L'), ('1 L','1 L'), ('1.2 L','1.2 L'), ]
    maquinacafe_potencia = [('1200 W','1200 W'), ('1260 W','1260 W'), ]

    microndas_volumemax = [('20 L','20 L'), ('23 L','23 L'), ('28 L','28 L'), ]
    microndas_potenciamax = [('700 W','700 W'), ('800 W','800 W'), ('1500 W','1500 W'), ]

    maquinalavarroupa_eficiencia = [('B','B'), ('A+','A+'), ('A++','A++'), ('A+++','A+++'), ]
    maquinalavarroupa_capacidade = [('7.0 Kg','7.0 Kg'), ('8.0 Kg','8.0 Kg'), ('9.0 Kg','9.0 Kg'), ('10.0 Kg','10.0 Kg'), ('11.0 Kg','11.0 Kg'), ('12.0 Kg','12.0 Kg'), ]
    maquinalavarroupa_velocidadecen = [('1200 Rpm','1200 Rpm'), ('1400 Rpm','1400 Rpm'), ]

    maquinasecarroupa_eficiencia = [('B','B'), ('A+','A+'), ('A++','A++'), ('A+++','A+++'), ]
    maquinasecarroupa_capacidade = [('7.0 Kg','7.0 Kg'), ('8.0 Kg','8.0 Kg'), ('9.0 Kg','9.0 Kg'), ('10.0 Kg','10.0 Kg'), ('11.0 Kg','11.0 Kg'), ('12.0 Kg','12.0 Kg'), ]
    maquinasecarroupa_consumo = [('177 KWh','177 KWh'), ('236 KWh','236 KWh'), ('306 KWh','306 KWh'), ('338 KWh','338 KWh'), ('560 KWh','560 KWh'), ]

    aspirador_potenciamax = [('33 W','33 W'), ('700 W','700 W'), ('750 W','750 W'), ]
    aspirador_volumemaxdep = [('3.5 L','3.5 L'), ('3 L','3 L'), ]

    gamingpc_ram = [('8 GB','8 GB'), ('16 GB','16 GB'), ]
    gamingpc_processador = [('i7-8700 Hex-core','i7-8700 Hex-core'), ('i7-8750H 2.2 GHz','i7-8750H 2.2 GHz'), ('i5-825OU 1.60GHz','i5-825OU 1.60GHz'), ('i7-8750H 2.2 GHz','i7-8750H 2.2 GHz'), ]
    gamingpc_capacidadedisco = [('512 GB','512 GB'), ('1024 GB','1024 GB'), ]
    gamingpc_grafica = [('Geforce GTX 1050 Ti 4GB','Geforce GTX 1050 Ti 4GB'), ('Geforce GTX 1050 4GB','Geforce GTX 1050 4GB'), ]

    consola_cor = [('Branco','Branco'), ('Preto','Preto'), ('Vermelho','Vermelho'), ('Verde','Verde'), ('Azul','Azul'), ('Castanho','Castanho'), ('Azul/Vermelho','Azul/Vermelho'), ('Varias','Varias'), ]
    consola_jogoincluido = [('None','None'), ('Red Dead Redemption II','Red Dead Redemption II'), ('FIFA 19','FIFA 19'), ('Pokemon Lets Go Eevee','Pokemon Lets Go Eevee'), ('TOMB RAIDER','TOMB RAIDER'), ]
