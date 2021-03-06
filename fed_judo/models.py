from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User

# Create your models here.

class TipoUsuario(models.Model):
    tipo_usuario = models.TextField()
    def __str__(self):
        return self.tipo_usuario


class StatusEventos(models.Model):
    status_Evento = models.TextField()
    def __str__(self):
        return self.status_Evento


class Evento(models.Model):
    #usuario_proponente = models.ForeignKey(Usuario, default=1)
    nome_evento = models.TextField()
    data_inicio = models.DateField(blank=True,null=True)
    data_fim = models.DateField(blank=True,null=True)
    status_evento = models.ForeignKey(StatusEventos, default=2)
    premiacao = models.TextField()
    local = models.TextField(blank=True)
    descricao = models.TextField(blank=True)


    def setDescricao(self, descricao):
        self.descricao = descricao
    def getDescricao(self):
        return self.descricao

    def setLocalEvento(self, local=''):
        self.local = local
    def getLocalEvento(self):
        return self.local

    def setNome_Evento(self, nome_evento=''):
        self.nome_evento = nome_evento
    def getNome_Evento(self):
        return self.nome_evento

    def setData_Inicio(self, data_inicio=''):
        self.data_inicio = data_inicio
    def getData_Inicio(self):
        return self.data_inicio

    def setData_Fim(self, data_fim=''):
        self.data_fim = data_fim
    def getData_Fim(self):
        return self.data_fim

    def setPremiacao(self, premiacao=''):
        self.premiacao = premiacao
    def getPremiacao(self):
        return self.premiacao

    def __str__(self):
        return self.nome_evento






class Usuario(models.Model):
    user = models.OneToOneField(User, default=1)
    cpf = models.IntegerField(unique=True,null=True)
    #nome = models.CharField(max_length=50,null=True)
    #idade = models.IntegerField(null=True)
    sexo = models.IntegerField(default=0)
    tipo_usuario = models.ManyToManyField(TipoUsuario)
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=50)
    data_nascimento = models.DateField(blank=True,null=True)
    pontuacao = models.FloatField(default=0)
    eventos_cadastrado = models.ManyToManyField(Evento)
    #login = models.OneToOneField(User)
    #username = models.CharField(max_length=50,unique=True,null=True)
    #password = models.CharField(max_length=50,null=True)


    def setEventoCadastrado(self, eventos_cadastrado=''):
        self.eventos_cadastrado = eventos_cadastrado
        

    def setTipoUsuario(self, tipo_usuario=''):
        self.tipo_usuario = tipo_usuario
    def getTipoUsuario(self):
        return self.tipo_usuario


    def getCpf(self):
        return self.cpf
    def setCpf(self, cpf=0):
        self.cpf = cpf

    def getNome(self):
        return self.nome
    def setNome(self, nome=''):
        self.nome = nome

    def setTelefone(self,telefone=''):
        self.telefone = telefone
    def getTelefone(self):
        return self.telefone

    def getEndereco(self):
        return self.endereco
    def setEndereco(self,endereco=''):
        self.endereco=endereco

    def getDatadeNascimento(self):
        return self.data_nascimento
    def setDatadeNascimento(self,data_nascimento=''):
        self.data_nascimento=data_nascimento;
    def getUsername(self):
        return self.username
    def setUsername(self,username=''):
        self.username=username
    def getPassword(self):
        return self.password
    def setPassword(self,password=''):
        self.password = password

    def __str__(self):
        return self.user.username
       



class Noticia(models.Model):
    usuario = models.OneToOneField(Usuario, default=1)
    descricao = models.CharField(max_length=100, null=True)
    titulo = models.TextField()
    corpo = models.TextField()
    data_lancamento_noticia = models.DateTimeField(null=True)
    imagem = models.ImageField(upload_to='noticias')
    usuario = models.ForeignKey(Usuario, default=1)

    def setImagem(self, imagem=''):
        self.imagem = imagem

    def setTitulo(self, titulo=''):
        self.titulo = titulo
    def getTitulo(self):
        return self.titulo

    def setCorpo(self, corpo=''):
        self.corpo = corpo
    def getCorpo(self):
        return self.corpo

    def setDataLancamentoNoticia(self, data_lancamento_noticia=''):
        self.data_lancamento_noticia = data_lancamento_noticia
    def getDataLancamentoNoticia(self):
        return self.data_lancamento_noticia


    def __str__(self):
        return self.titulo


class Academia(models.Model):
    #id_academia = models.IntegerField()
    nome_Academia = models.TextField()
    endereco_academia = models.TextField()
    limite_atletas = models.IntegerField(null=True)
    telefone = models.IntegerField(null=True)
    email = models.EmailField(max_length=75, null=True)

    pontuacao = models.PositiveIntegerField(null=True)


    def setPontuacao(self, pontuacao=''):
        self.pontuacao = pontuacao
    def getPontuacao(self):
        return self.pontuacao



    def setTelefone(self, telefone=''):
        self.telefone = telefone
    def getTelefone(self):
        return self.telefone

    def setEmail(self, email=''):
        self.email = email
    def getEmail(self):
        return self.email

    def setIdAcademia(self, id_academia=''):
        self.id_academia = id_academia
    def getIdAcademia(self):
        return self.id_academia

    def setNomeAcademia(self, nome_Academia=''):
        self.nome_Academia = nome_Academia
    def getNomeAcademia(self):
        return self.nome_Academia

    def setEnderecoAcademia(self, endereco_academia=''):
        self.endereco_academia = endereco_academia
    def getEnderecoAcademia(self):
        return self.endereco_academia

    def setLimiteAtletasAcademia(self, limite_atletas=''):
        self.limite_atletas = limite_atletas
    def getLimiteAtletasAcademia(self):
        return self.limite_atletas

    def __str__(self):
        return self.nome_Academia



class Atleta(models.Model):
    usuario = models.OneToOneField(Usuario, default=1)
    academia_Associada = models.ForeignKey(Academia)
    categoria = models.TextField()
    graduacao = models.TextField()
    pontuacao = models.IntegerField(default=0);

class Administrador(models.Model):
    carga_horaria = models.IntegerField()
    salario = models.FloatField()


class Juiz(models.Model):
    posicao = models.TextField()
    funcao = models.TextField()



class FaleConosco(models.Model):
    nome = models.TextField()
    email = models.TextField()
    mensagem = models.TextField()
    hora_envio = models.DateTimeField(blank=True,null=True)

    def setNome(self, nome=''):
        self.nome = nome
    def getNome(self):
        return self.nome

    def setEmail(self, email=''):
        self.email = email
    def getEmail(self):
        return self.email

    def setMensagem(self, mensagem=''):
        self.mensagem = mensagem
    def getMensagem(self):
        return self.mensagem

    def setHoraEnvio(self, hora_envio=''):
        self.hora_envio = hora_envio
    def getHotaEnvio(self):
        return self.hora_envio

    def __str__(self):
        return self.nome


class Penalidades(models.Model):
    penalidade = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.penalidade

'''
class Lutas(models.Model):
    participante1 = models.ForeignKey(Usuario)
    participante2 = models.ForeignKey(Usuario)
    vencedor = models.ForeignKey(Usuario)
    tempo = models.FloatField(default=0)
    qt_ponto_part_01 = models.IntegerField(default=0)
    qt_ponto_part_02 = models.IntegerField(default=0)
    pernalidades_part_01 = models.TextField()
    pernalidades_part_02 = models.TextField()

'''