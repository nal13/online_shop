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
            self.jogo()


    def computador(self):
        self.fields['ram'] = forms.ChoiceField(
            label='Ram',
            required=True,
            choices=Fvars().computador_ram
        )
        self.fields['processador'] = forms.CharField(
            label='Processador',
            required=True,
            min_length=3,
            max_length=40
        )
        self.fields['capacidadedisco'] = forms.ChoiceField(
            label='Capacidade do Disco',
            required=True,
            choices=Fvars().computador_capacidade_disco
        )
        self.fields['grafica'] = forms.CharField(
            label='Gráfica',
            required=True,
            min_length=3,
            max_length=40
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
        self.fields['processador'] = forms.CharField(
            label='Processador',
            required=True,
            min_length=3,
            max_length=40
        )
        self.fields['capacidadememoria'] = forms.ChoiceField(
            label='Capacidade de Memória',
            required=True,
            choices=Fvars().telemovel_capacidade_memoria
        )
        self.fields['camara'] = forms.CharField(
            label='Câmara',
            required=True,
            min_length=3,
            max_length=40
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
        self.fields['processador'] = forms.CharField(
            label='Processador',
            required=True,
            min_length=3,
            max_length=40
        )
        self.fields['capacidadememoria'] = forms.ChoiceField(
            label='Capacidade de Memória',
            required=True,
            choices=Fvars().tablet_capacidade_memoria
        )
        self.fields['camara'] = forms.CharField(
            label='Câmara',
            required=True,
            min_length=3,
            max_length=40
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

    def jogo(self):
        self.fields['ram'] = forms.ChoiceField(
            label='Ram',
            required=True,
            choices=Fvars().jogo_ram
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
    computador_capacidade_disco = [('128 GB','128 GB'), ('256 GB','256 GB'), ('512 GB','512 GB'), ('1024 GB','1024 GB'), ('2048 GB','2048 GB'), ]

    telemovel_ram =  [('1 GB','1 GB'), ('2 GB','2 GB'), ('4 GB','4 GB'), ('8 GB','8 GB'), ('16 GB','16 GB'), ('32 GB','32 GB'), ]
    telemovel_capacidade_memoria = [('8 GB','8 GB'), ('16 GB','16 GB'), ('32 GB','32 GB'), ('64 GB','64 GB'), ('128 GB','128 GB'), ]

    tablet_ram = [('1 GB','1 GB'), ('2 GB','2 GB'), ('4 GB','4 GB'), ('8 GB','8 GB'), ('16 GB','16 GB'), ('32 GB','32 GB'), ]
    tablet_capacidade_memoria = [('8 GB','8 GB'), ('16 GB','16 GB'), ('32 GB','32 GB'), ('64 GB','64 GB'), ('128 GB','128 GB'), ]

    camara_resolucaovideo = [('Full HD 1080p','Full HD 1080p'), ('UHD 4K','UHD 4K'), ]
    camara_resolucaofoto = [('16 MP','16 MP'), ('18 MP','18 MP'), ('20 MP','20 MP'), ('22 MP','22 MP'), ('24 MP','24 MP'), ('26 MP','26 MP'), ]

    drone_autonomia = [('Ate 9 min','Ate 9 min'), ('Ate 15 min','Ate 15 min'), ]
    drone_raio = [('200 m','200 m'), ('300 m','300 m'), ]

    tv_qualidadeimagem = [('HD','HD'), ('HD 720p','HD 720p'), ('UHD 4K','UHD 4K'), ]
    tv_frequencia = [('50 Hz','50 Hz'), ('60 Hz','60 Hz'), ('100 Hz','100 Hz'), ]

    leitorblueray_formatosreproducao = [('BD','BD'), ('CD','CD'), ('DVD','DVD'), ]
    leitorblueray_resolucao = [('Full HD 1080p','Full HD 1080p'), ('4K','4K'), ]

    jogo_ram =  [('2 GB','2 GB'), ('4 GB','4 GB'), ('8 GB','8 GB'), ('16 GB','16 GB'), ('32 GB','32 GB'), ]
