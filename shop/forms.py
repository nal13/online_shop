from django import forms


class AddModelForm(forms.Form):

    def __init__(self, type, *args, **kwargs):
        super(AddModelForm, self).__init__(*args, **kwargs)

        self.fields['nome'] = forms.CharField(
            label='Nome',
            required=True,
            min_length=8,
            max_length=40
        )
        self.fields['marca'] = forms.ChoiceField(
            label='Marca',
            required=True,
            choices=Fvars().marca
        )
        self.fields['categoria'] = forms.ChoiceField(
            label='Categoria',
            required=True,
            choices=Fvars().categoria
        )
        self.fields['preco'] = forms.DecimalField(
            label='Preco',
            required=True,
            initial='0',
            min_value=1,
            max_value=9999,
            max_digits=6,
            decimal_places=2
        )

        if type=='computador':
            self.computador()
        if type=='telemovel':
            self.telemovel()
        if type=='tablet':
            self.tablet()
        if type=='camara':
            self.camara()
        if type=='drone':
            self.drone()
        if type=='tv':
            self.tv()
        if type=='leitorblueray':
            self.leitorblueray()
        if type=='maquinacafe':
            self.maquinacafe()
        if type=='microondas':
            self.microondas()
        if type=='maquinalavarroupa':
            self.maquinalavarroupa()
        if type=='maquinasecarroupa':
            self.maquinasecarroupa()
        if type=='aspirador':
            self.aspirador()
        if type=='aspirador':
            self.aspirador()
        if type=='gamingpc':
            self.gamingpc()
        if type=='consola':
            self.consola()
        if type=='jogo':
            pass



    def computador(self):
        self.fields['ram'] = forms.ChoiceField(
            label='Ram',
            required=True,
            choices=Fvars().computador_ram
        )
        self.fields['processador'] = forms.ChoiceField(
            label='Processador',
            required=True,
            choices=Fvars().computador_processador
        )
        self.fields['capacidadedisco'] = forms.ChoiceField(
            label='Capacidade do Disco',
            required=True,
            choices=Fvars().computador_capacidadedisco
        )
        self.fields['grafica'] = forms.ChoiceField(
            label='Gráfica',
            required=True,
            choices=Fvars().computador_grafica
        )
        self.fields['tamanhoecra'] = forms.DecimalField(
            label='Tamanho do Ecrã',
            required=True,
            initial='0',
            min_value=1,
            max_value=9999,
            max_digits=6,
            decimal_places=1
        )

    def telemovel(self):
        self.fields['ram'] = forms.ChoiceField(
            label='Ram',
            required=True,
            choices=Fvars().telemovel_ram
        )
        self.fields['processador'] = forms.ChoiceField(
            label='Processador',
            required=True,
            choices=Fvars().telemovel_processador
        )
        self.fields['capacidadememoria'] = forms.ChoiceField(
            label='Capacidade de Memória',
            required=True,
            choices=Fvars().telemovel_capacidadememoria
        )
        self.fields['camara'] = forms.ChoiceField(
            label='Câmara',
            required=True,
            choices=Fvars().telemovel_camara
        )
        self.fields['tamanhoecra'] = forms.DecimalField(
            label='Tamanho do Ecrã',
            required=True,
            initial='0',
            min_value=1,
            max_value=9999,
            max_digits=6,
            decimal_places=2
        )

    def tablet(self):
        self.fields['ram'] = forms.ChoiceField(
            label='Ram',
            required=True,
            choices=Fvars().tablet_ram
        )
        self.fields['processador'] = forms.ChoiceField(
            label='Processador',
            required=True,
            choices=Fvars().tablet_processador
        )
        self.fields['capacidadememoria'] = forms.ChoiceField(
            label='Capacidade de Memória',
            required=True,
            choices=Fvars().tablet_capacidadememoria
        )
        self.fields['camara'] = forms.ChoiceField(
            label='Câmara',
            required=True,
            choices=Fvars().tablet_camara
        )
        self.fields['tamanhoecra'] = forms.DecimalField(
            label='Tamanho do Ecrã',
            required=True,
            initial='0',
            min_value=1,
            max_value=9999,
            max_digits=6,
            decimal_places=2
        )

    def camara(self):
        self.fields['resolucaovideo'] = forms.ChoiceField(
            label='Resolução de Vídeo',
            required=True,
            choices=Fvars().camara_resolucaovideo
        )
        self.fields['wireless'] = forms.BooleanField(
            label='Wireless',
            required=True,
        )
        self.fields['resolucaofoto'] = forms.ChoiceField(
            label='Resolução de Foto',
            required=True,
            choices=Fvars().camara_resolucaofoto
        )

    def drone(self):
        self.fields['autonomia'] = forms.ChoiceField(
            label='Autonomia',
            required=True,
            choices=Fvars().drone_autonomia
        )
        self.fields['raio'] = forms.ChoiceField(
            label='Raio',
            required=True,
            choices=Fvars().drone_raio
        )
        self.fields['camaraimb'] = forms.BooleanField(
            label='Camara Imb',
            required=True,
        )

    def tv(self):
        self.fields['tamanhoecra'] = forms.DecimalField(
            label='Tamanho do Ecrã',
            required=True,
            initial='0',
            min_value=1,
            max_value=9999,
            max_digits=6,
            decimal_places=1
        )
        self.fields['qualidadeimagem'] = forms.ChoiceField(
            label='Qualidade de Imagem',
            required=True,
            choices=Fvars().tv_qualidadeimagem
        )
        self.fields['frequencia'] = forms.ChoiceField(
            label='Frequência',
            required=True,
            choices=Fvars().tv_frequencia
        )

    def leitorblueray(self):
        self.fields['formatosreproducao'] = forms.MultipleChoiceField(
            label='Formatos de Reprodução',
            required=True,
            choices=Fvars().leitorblueray_formatosreproducao
        )
        self.fields['resolucao'] = forms.ChoiceField(
            label='Resolução',
            required=True,
            choices=Fvars().leitorblueray_resolucao
        )

    def maquinacafe(self):
        self.fields['cor'] = forms.ChoiceField(
            label='Cor',
            required=True,
            choices=Fvars().maquinacafe_cor
        )
        self.fields['agua'] = forms.ChoiceField(
            label='Água',
            required=True,
            choices=Fvars().maquinacafe_agua
        )
        self.fields['potencia'] = forms.ChoiceField(
            label='Potência',
            required=True,
            choices=Fvars().maquinacafe_potencia
        )

    def microondas(self):
        self.fields['grill'] = forms.BooleanField(
            label='Grill',
            required=True,
        )
        self.fields['volumemax'] = forms.ChoiceField(
            label='Volume Máximo',
            required=True,
            choices=Fvars().microndas_volumemax
        )
        self.fields['potenciamax'] = forms.ChoiceField(
            label='Potência Máxima',
            required=True,
            choices=Fvars().microndas_potenciamax
        )

    def maquinalavarroupa(self):
        self.fields['eficiencia'] = forms.ChoiceField(
            label='Eficiencia',
            required=True,
            choices=Fvars().maquinalavarroupa_eficiencia
        )
        self.fields['capacidade'] = forms.ChoiceField(
            label='Capacidade',
            required=True,
            choices=Fvars().maquinalavarroupa_capacidade
        )
        self.fields['velocidadecen'] = forms.ChoiceField(
            label='Velocidade Centrífuga',
            required=True,
            choices=Fvars().maquinalavarroupa_velocidadecen
        )

    def maquinasecarroupa(self):
        self.fields['eficiencia'] = forms.ChoiceField(
            label='Eficiencia',
            required=True,
            choices=Fvars().maquinasecarroupa_eficiencia
        )
        self.fields['capacidade'] = forms.ChoiceField(
            label='Capacidade',
            required=True,
            choices=Fvars().maquinasecarroupa_capacidade
        )
        self.fields['consumo'] = forms.ChoiceField(
            label='Consumo',
            required=True,
            choices=Fvars().maquinasecarroupa_consumo
        )

    def aspirador(self):
        self.fields['potenciamax'] = forms.ChoiceField(
            label='Potência Máxima',
            required=True,
            choices=Fvars().aspirador_potenciamax
        )
        self.fields['volumemaxdep'] = forms.ChoiceField(
            label='Volume Máximo do Depósito',
            required=True,
            choices=Fvars().aspirador_volumemaxdep
        )

    def gamingpc(self):
        self.fields['ram'] = forms.ChoiceField(
            label='Ram',
            required=True,
            choices=Fvars().gamingpc_ram
        )
        self.fields['processador'] = forms.ChoiceField(
            label='Processador',
            required=True,
            choices=Fvars().gamingpc_processador
        )
        self.fields['capacidadedisco'] = forms.ChoiceField(
            label='Capacidade do Disco',
            required=True,
            choices=Fvars().gamingpc_capacidadedisco
        )
        self.fields['grafica'] = forms.ChoiceField(
            label='Gráfica',
            required=True,
            choices=Fvars().gamingpc_grafica
        )
        self.fields['tamanhoecra'] = forms.DecimalField(
            label='Tamanho do Ecrã',
            required=True,
            initial='0',
            min_value=1,
            max_value=9999,
            max_digits=6,
            decimal_places=2
        )

    def consola(self):
        self.fields['cor'] = forms.MultipleChoiceField(
            label='Cor',
            required=True,
            choices=Fvars().consola_cor
        )
        self.fields['jogoincluido'] = forms.ChoiceField(
            label='Jogo Incluido',
            required=True,
            choices=Fvars().consola_jogoincluido
        )
        self.fields['capacidadedisco'] = forms.ChoiceField(
            label='Capacidade do Disco',
            required=True,
            choices=Fvars().gamingpc_capacidadedisco
        )
        self.fields['grafica'] = forms.ChoiceField(
            label='Gráfica',
            required=True,
            choices=Fvars().gamingpc_grafica
        )
        self.fields['tamanhoecra'] = forms.DecimalField(
            label='Tamanho do Ecrã',
            required=True,
            initial='0',
            min_value=1,
            max_value=9999,
            max_digits=6,
            decimal_places=2
        )


class Fvars:
    marca = [
        ('Asus', 'Asus'), ('HP', 'HP'), ('LeNovo', 'LeNovo'), ('Xiaomi', 'Xiaomi'), ('Apple', 'Apple'), ('Huawei', 'Huawei'),
        ('Canon', 'Canon'), ('Nikon', 'Nikon'), ('Parrot', 'Parrot'), ('Silver', 'Silver'), ('LG', 'LG'), ('Sony', 'Sony'),
        ('Nespresso', 'Nespresso'), ('Delta', 'Delta'), ('Samsung', 'Samsung'), ('Flama', 'Flama'), ('Whirlpoll', 'Whirlpoll'),
        ('Hotpoint', 'Hotpoint'), ('Indesit', 'Indesit'), ('Bosh', 'Bosh'), ('IronBot', 'IronBot'), ('Hoover', 'Hoover'),
        ('Rowenta', 'Rowenta'), ('Microsoft', 'Microsoft'), ('Nintendo', 'Nintendo'), ('PS4', 'PS4'), ('XBOX', 'XBOX'), ('SWITCH', 'SWITCH')
    ]
    categoria = [
        ('Comunicação Móvel', 'Comunicação Móvel'), ('Fotografia', 'Fotografia'), ('Tecnologia de Casa', 'Tecnologia de Casa'),
        ('Cozinha', 'Cozinha'), ('Limpeza', 'Limpeza'), ('Videojogos', 'Videojogos')
    ]

    computador_ram = [('1 GB','1 GB'), ('2 GB','2 GB'), ('4 GB','4 GB'), ('8 GB','8 GB'), ('16 GB','16 GB'), ('32 GB','32 GB'), ]
    computador_processador = [('i5-7200U 2.5GHz','i5-7200U 2.5GHz'), ('i7-8550U 1.8GHz','i7-8550U 1.8GHz'), ('i3-7020U 2.3GHz','i3-7020U 2.3GHz'), ('i5-825OU 1.6 GHz','i5-825OU 1.6 GHz'), ('i7-855OU 1.8 GHz','i7-855OU 1.8 GHz'), ('i5-825OU 1.6 GHz','i5-825OU 1.6 GHz'), ]
    computador_capacidadedisco = [('128 GB','128 GB'), ('256 GB','256 GB'), ('512 GB','512 GB'), ('1024 GB','1024 GB'), ('2048 GB','2048 GB'), ]
    computador_grafica = [('Radeon R5 530 2GB','Radeon R5 530 2GB'), ('HD Graphics 620','HD Graphics 620'), ('HD Graphics 620','HD Graphics 620'), ('GeForce MX110 2GB','GeForce MX110 2GB'), ('Radeon R5 530 2GB','Radeon R5 530 2GB'), ]

    telemovel_ram =  [('1 GB','1 GB'), ('2 GB','2 GB'), ('4 GB','4 GB'), ('8 GB','8 GB'), ('16 GB','16 GB'), ('32 GB','32 GB'), ]
    telemovel_processador = [('Quad-Core 2.0 GHz Cortex-A53','Quad-Core 2.0 GHz Cortex-A53'), ('Hexa-core A12 Bionic','Hexa-core A12 Bionic'), ('Quad-core 2.23 GHz A10 Fusion','Quad-core 2.23 GHz A10 Fusion'), ('Octa-core(4x 2.36 GHz + 4x 1.7 Ghz)','Octa-core(4x 2.36 GHz + 4x 1.7 Ghz)'), ]
    telemovel_capacidadememoria = [('8 GB','8 GB'), ('16 GB','16 GB'), ('32 GB','32 GB'), ('64 GB','64 GB'), ('128 GB','128 GB'), ]
    telemovel_camara = [('12 MP','12 MP'), ('13 MP','13 MP'), ('Dual(12 MP + 5MP)','Dual(12 MP + 5MP)'), ('DUAL(16 MP + 2 MP)','DUAL(16 MP + 2 MP)'), ]

    tablet_ram = [('1 GB','1 GB'), ('2 GB','2 GB'), ('4 GB','4 GB'), ('8 GB','8 GB'), ('16 GB','16 GB'), ('32 GB','32 GB'), ]
    tablet_processador = [('Quad-Core 1.3 GHz','Quad-Core 1.3 GHz'), ('Quad-Core 1.4 GHz','Quad-Core 1.4 GHz'), ('Dual-Core A10 Fusion','Dual-Core A10 Fusion'), ('Dual-Core A10X Fusion','Dual-Core A10X Fusion'), ('Quad-Core 1.4 GHz Snapdragon 425','Quad-Core 1.4 GHz Snapdragon 425'), ]
    tablet_capacidadememoria = [('8 GB','8 GB'), ('16 GB','16 GB'), ('32 GB','32 GB'), ('64 GB','64 GB'), ('128 GB','128 GB'), ]
    tablet_camara = [('5 MP + 2 MP','Quad-Core 1.4 GHz'), ('8 MP + 1.2 MP','8 MP + 1.2 MP'), ('12 MP + 7 MP','12 MP + 7 MP'), ]

    camara_resolucaovideo = [('Full HD 1080p','Full HD 1080p'), ('UHD 4K','UHD 4K'), ]
    camara_resolucaofoto = [('16 MP','16 MP'), ('18 MP','18 MP'), ('20 MP','20 MP'), ('22 MP','22 MP'), ('24 MP','24 MP'), ('26 MP','26 MP'), ]

    drone_autonomia = [('Ate 9 min','Ate 9 min'), ('Ate 15 min','Ate 15 min'), ]
    drone_raio = [('200 m','200 m'), ('300 m','300 m'), ]

    tv_qualidadeimagem = [('HD','HD'), ('HD 720p','HD 720p'), ('UHD 4K','UHD 4K'), ]
    tv_frequencia = [('50 Hz','50 Hz'), ('60 Hz','60 Hz'), ('100 Hz','100 Hz'), ]

    leitorblueray_formatosreproducao = [('BD','BD'), ('CD','CD'), ('DVD','DVD'), ]
    leitorblueray_resolucao = [('Full HD 1080p','Full HD 1080p'), ('4K','4K'), ]

    maquinacafe_cor = [('Branco','Branco'), ('Preto','Preto'), ('Vermelho','Vermelho'), ('Verde','Verde'), ('Azul','Azul'), ('Castanho','Castanho'), ]
    maquinacafe_agua = [('0.8 L','0.8 L'), ('1 L','1 L'), ('1.2 L','1.2 L'), ]
    maquinacafe_potencia = [('1200 W','1200 W'), ('1260 W','1260 W'), ]

    microndas_volumemax = [('20 L','20 L'), ('23 L','23 L'), ('28 L','28 L'), ]
    microndas_potenciamax = [('700 L','700 L'), ('800 L','800 L'), ('1500 L','1500 L'), ]

    maquinalavarroupa_eficiencia = [('B','B'), ('A+','A+'), ('A+++','A+++'), ]
    maquinalavarroupa_capacidade = [('7.0 Kg','7.0 Kg'), ('8.0 Kg','8.0 Kg'), ('9.0 Kg','9.0 Kg'), ('10.0 Kg','10.0 Kg'), ('11.0 Kg','11.0 Kg'), ('12.0 Kg','12.0 Kg'), ]
    maquinalavarroupa_velocidadecen = [('1200 Rpm','1200 Rpm'), ('1400 Rpm','1400 Rpm'), ]

    maquinasecarroupa_eficiencia = [('B','B'), ('A+','A+'), ('A+++','A+++'), ]
    maquinasecarroupa_capacidade = [('7.0 Kg','7.0 Kg'), ('8.0 Kg','8.0 Kg'), ('9.0 Kg','9.0 Kg'), ('10.0 Kg','10.0 Kg'), ('11.0 Kg','11.0 Kg'), ('12.0 Kg','12.0 Kg'), ]
    maquinasecarroupa_consumo = [('177 kWh','177 kWh'), ('236 kWh','236 kWh'), ('306 kWh','306 kWh'), ('338 kWh','338 kWh'), ('560 Rpm"','560 Rpm"'), ]

    aspirador_potenciamax = [('33 W','33 W'), ('700 W','700 W'), ('750 W','750 W'), ]
    aspirador_volumemaxdep = [('3.5 L','3.5 L'), ('3 L','3 L'), ]

    gamingpc_ram = [('8 GB','8 GB'), ('16 GB','16 GB'), ]
    gamingpc_processador = [('i7-8700 Hex-core','i7-8700 Hex-core'), ('i7-8750H 2.2 GHz','i7-8750H 2.2 GHz'), ('i5-825OU 1.60GHz','i5-825OU 1.60GHz'), ('i7-8750H 2.2 GHz','i7-8750H 2.2 GHz'), ]
    gamingpc_capacidadedisco = [('512 GB','512 GB'), ('1024 GB','1024 GB'), ]
    gamingpc_grafica = [('Geforce GTX 1050 Ti 4GB','Geforce GTX 1050 Ti 4GB'), ('Geforce GTX 1050 4GB','Geforce GTX 1050 4GB'), ]

    consola_cor = [('Branco','Branco'), ('Preto','Preto'), ('Vermelho','Vermelho'), ('Verde','Verde'), ('Azul','Azul'), ('Castanho','Castanho'), ]
    consola_jogoincluido = [('None','None'), ('Red Dead Redemption II','Red Dead Redemption II'), ('FIFA 19','FIFA 19'), ('Pokemon Lets Go Eevee','Pokemon Lets Go Eevee'), ]
