from django.shortcuts import render, get_object_or_404,render_to_response,redirect
from .models import Usuario, Evento, FaleConosco, Academia, Noticia

from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm, EditProfileForm
from datetime import datetime

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth

from random import randint


def academias(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    academias = Academia.objects.all()#.order_by('published_date')
    return render (request, 'academias.html', {'academias':academias})



# Create your views here.
def index(request):
    noticias = Noticia.objects.all().order_by('data_lancamento_noticia').reverse()
    eventos = Evento.objects.all()
    return render (request, 'index.html', {'noticias':noticias, 'eventos':eventos})




def sobre(request):
    return render (request, 'sobre.html')

#def cadastro_usuario(request):
#   usuario = Usuario()
#   if(request.method=='POST'):
        #if(request.POST.get('senha')==request.POST.get('comfirmaca_senha')):
        #   usuario.setNome(request.POST.get('nome'))
        #   return render (request, 'cadastro_usuario.html')
 #      return render (request, 'cadastro_usuario.html')
 #      return render (request, 'cadastro_usuario.html',{})


def eventos(request):

    eventos = Evento.objects.all()
    return render (request, 'eventos.html', {'eventos':eventos})

    ns = Noticia.objects.all()
    eventos = Evento.objects.all()
    return render (request, 'eventos.html', {'eventos':eventos, 'ns':ns})


def rankings(request):
    academias = Academia.objects.all().order_by('pontuacao').reverse()
    usuario = Usuario.objects.all().order_by('pontuacao').reverse()
    return render (request, 'rankings.html', {'academias':academias, 'usuario':usuario})



def login(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')#'teste'# aqui e pego o que esta no formulario html e salvo na var de ususario
        password = request.POST.get('senha')#'tomaz123'# aqui e pego o que esta no formulario html e salvo na var de senha
        print(username)#isso e so um print comum
        user  = auth.authenticate(username=username, password=password)# essa funcao pronta do djanco para verificae e logar em uma conta
        if user is not None:
            auth.login(request, user)#aqui e sogado e construido a request com os dados de
            return HttpResponseRedirect('/index/')#tela de feeds chamada se der certo logui
            if request.user.is_authenticaded():
                return HttpResponseRedirect('/index/')
        else:
            #c = {}
            #c.update(csrf(request))
            #c.update({'error_message': 'Senha ou Usuario Incorretos'})
            return render(request, 'interface_usuario.html', {})# ususario e senhas invalidas arruamar a pagina para exibir erro
    return render (request, 'login.html')


def cadastro_eventos(request):
    eventos = Evento()
    codigo = 0
    if(request.method == 'POST'):
        eventos.setNome_Evento(request.POST.get('nome'))
        eventos.setData_Inicio(request.POST.get('data_inicio'))
        eventos.setData_Fim(request.POST.get('data_fim'))
        eventos.setPremiacao(request.POST.get('premiacao'))
        eventos.save()
        codigo = 1
        return render (request, 'cadastro_eventos.html', {'codigo':codigo})
    return render(request, 'cadastro_eventos.html', {'codigo':codigo})


def cadastro_noticias(request):
	noticia = Noticia()
	codigo = 0
	if (request.method == 'POST'):
		noticia.setTitulo(request.POST.get('titulo_noticia'))
		noticia.setCorpo(request.POST.get('corpo_noticia'))
		noticia.setImagem(request.POST.get('imagem_noticia'))
		noticia.setDataLancamentoNoticia(datetime.now())
		noticia.save()
		codigo = 1
		return render (request, 'cadastro_noticias.html', {'codigo':codigo})
	return render (request,'cadastro_noticias.html', {'codigo':codigo})

'''
    noticia = Noticia()
    codigo = 0
    if (request.method == 'POST'):
        noticia.setTitulo(request.POST.get('titulo_noticia'))
        noticia.setCorpo(request.POST.get('corpo_noticia'))
        noticia.setImagem(request.POST.get('imagem_noticia'))
        noticia.setDataLancamentoNoticia(datetime.now())
        noticia.save()
        codigo = 1
        return render (request, 'cadastro_noticias.html', {'codigo':codigo})

    return render (request,'cadastro_noticias.html', {'codigo':codigo})
'''



def administracao(request):
    return render (request, 'administracao.html')

'''
def cadastro_usuario(request):
    if not request.user.is_authenticated():
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password != password2:
                if first_name == '' or last_name == '' or email == '':
                    return render(request, 'register.html')
                else:
                    return render(request, 'register.html')
            elif first_name == '' or last_name == '' or email == '':
                return render(request, 'register.html')
            user.set_password(password)
            user.save()

            if user is not None:
                if user.is_active:
                    return redirect('/index')#criar uma tela de confirmacao de registro de usuario
        return render(request, 'cadastro_usuario.html', {'form':form})
    else:
        return HttpResponseRedirect('/index')




def cadastro_usuario(request):
    usuario = Usuario()
    codigo = 0
    if(request.method == 'POST' and request.POST.get('senha') == request.POST.get('confirmacao_senha')):
        usuario.setNome(request.POST.get('nome'))
        usuario.setEndereco(request.POST.get('endereco'))
        usuario.setTelefone(request.POST.get('telefone'))
        usuario.setDatadeNascimento(request.POST.get('data_nascimento'))
        usuario.setCpf(request.POST.get('cpf'))
        usuario.setUsername(request.POST.get('login'))
        usuario.setPassword(request.POST.get('senha'))
        usuario.save()
        codigo = 1
        return render(request,'cadastro_usuario.html',{'codigo':codigo})
    elif(request.method == 'POST' and request.POST.get('senha') != request.POST.get('confirmacao_senha')):
        usuario.setNome(request.POST.get('nome'))
        usuario.setEndereco(request.POST.get('endereco'))
        usuario.setTelefone(request.POST.get('telefone'))
        usuario.setDatadeNascimento(request.POST.get('data_nascimento'))
        usuario.setCpf(request.POST.get('cpf'))
        usuario.setUsername(request.POST.get('login'))
        codigo = 2
        return render(request,'cadastro_usuario.html',{'nome':usuario.getNome(),'endereco':usuario.getEndereco(),'telefone':usuario.getTelefone(),'data_nascimento':usuario.getDatadeNasciento(),'cpf':usuario.getCpf(),'username':usuario.getUsername(),'codigo':codigo})
    return render(request,'cadastro_usuario.html',{'codigo':codigo})
'''
def cadastro_usuario(request):
        form = RegistrationForm(request.POST or None)        
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']          
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password != password2:
                if first_name == '' or last_name == '' or email == '':
                    return render(request, 'cadastro_usuario.html')
                else:
                    return render(request, 'cadastro_usuario.html')
            elif first_name == '' or last_name == '' or email == '':
                return render(request, 'cadastro_usuario.html')
            user.set_password(password)
            user.save()


            if user is not None:
                if user.is_active:
                    return redirect('/interface_usuario')                    
        return render(request, 'cadastro_usuario.html', {'form':form})


def fale_conosco(request):
    mensagem = FaleConosco()
    codigo = 0
    if (request.method == 'POST'):
        mensagem.setNome(request.POST.get('nome'))
        mensagem.setEmail(request.POST.get('email'))
        mensagem.setMensagem(request.POST.get('mensagem'))
        mensagem.setHoraEnvio(datetime.now())
        mensagem.save()
        codigo = 1
        return render (request, 'fale_conosco.html', {'codigo':codigo})
    return render(request, 'fale_conosco.html', {'codigo':codigo})


def cadastro_academias(request):#corrigir a atribuicao de id para academia/inserir pesquisa para verificar se o valor ja esta salvo no banco
    academia = Academia()
    codigo = 0
    if (request.method == 'POST'):
        academia.setNomeAcademia(request.POST.get('nome_Academia'))
        academia.setEnderecoAcademia(request.POST.get('endereco_academia'))
        academia.setLimiteAtletasAcademia(request.POST.get('limite-atletas'))
        academia.setTelefone(request.POST.get('telefone_academia'))
        academia.setPontuacao(0)
        academia.setEmail(request.POST.get('email_academia'))
        academia.setIdAcademia(randint(0, 9999999))
        academia.save()
        codigo = 1
        return render (request, 'cadastro_academias.html', {'codigo':codigo})

    return render(request, 'cadastro_academias.html', {'codigo': codigo})


def consulta(request):
    consulta = ColetaAgendada()
    codigo = 0
    if(request.method == 'POST'):
        codigo = 1
        consulta.setNome(request.POST.get('nomecompleto'))
        consulta.setRua(request.POST.get('rua'))
        consulta.setBairro(request.POST.get('bairro'))
        consulta.setNumero(request.POST.get('numero'))
        consulta.setTelefone(request.POST.get('telefone'))
        consulta.setEmail(request.POST.get('email'))
        consulta.setComplemento(request.POST.get('complemento'))
        consulta.save()
        return render(request,'paginas/consulta.html',{'codigo':codigo})
    return render(request,'paginas/consulta.html',{'codigo':codigo})


def login_user(request):#Este esta sendo usado para LOGIN
    if request.method == "POST":
        #username = request.POST['username']
        #password = request.POST['password']
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                #login(request, user)
                auth.login(request, user)
                if request.user.is_staff:
                    return redirect('/admin')
                else:
                    #return render(request,'interface_usuario.html',{'user':user})
                    return render(request,'interface_usuario.html')

            else:
                return render(request, 'login.html', {'error_message': 'Sua conta nao esta ativa.'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')





def interface_usuario(request, pk=None):
    if not request.user.is_authenticated():
        return redirect('/login')

    else:
        if pk:
            user = User.objects.get(pk=pk)
        else:
            user = request.user
            args = {'user': user}
            #posts = Post.objects.filter(author=user)
            #posts = posts.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return render(request, 'interface_usuario.html', {'args': args})




    return render (request, 'interface_usuario.html')


def logout(request):
    auth.logout(request)
    #return render_to_response('index.html')
    return redirect('/index')

'''
def editar_perfil(request):
    if not request.user.is_authenticated():
        return redirect('/login')
    else:      
    	codigo = 0
    	if(request.method == 'POST'):
        	form = EditProfileForm(request.POST, instance=request.user)
        	if form.is_valid():
        		form.save()
        		return redirect('/interface_usuario')
        	else:
        		form = EditProfileForm(instance=request.user)
        		args = {'form': form, 'codigo':codigo}
        		return render(request, 'editar_perfil.html', args)

            

'''

'''
def editar_perfil(request):
	#alteracao = Usuario()
	#print(request.user.id)
	codigo = 0
	if(request.method == 'POST'):
		
		request.user.cpf.setCpf.request.POST.get('cpf')
		request.user.telefone.setTelefone.request.POST.get('telefone')
		request.user.endereco.setEndereco.request.POST.get('endereco')
		request.user.data_nascimentorequest.setDataNascimento.request.POST.get('data_nascimento')
		request.user.save()
		
		a = (int(request.POST.get('cpf')))
		Usuario.setCpf(1111111111)
		Usuario.setEndereco(request.POST.get('endereco'))
		Usuario.setTelefone(request.POST.get('telefone'))
		Usuario.setDataNascimento(request.POST.get('data_nascimento'))
		Usuario.save()
    #return render (request,'editar_perfil.html',{'codigo':codigo})       
    return render (request,'editar_perfil.html',{'codigo':codigo})

    alteracao = Usuario()
    codigo = 0
    if(request.method == 'POST'):
        request.user.cpf = request.POST.get('cpf')
        request.user.telefone = request.POST.get('telefone')
        request.user.endereco = request.POST.get('endereco')
        request.user.data_nascimento = request.POST.get('data_nascimento')
        request.user.save()
    return render (request, 'editar_perfil.html', {'codigo':codigo})
 '''

def editar_perfil(request):
    codigo = 0
    if(request.method == 'POST'):
        redirect('/interface_usuario')
    else:
        return render (request, 'editar_perfil.html', {'codigo':codigo})   


def informacoes_eventos(request):
    return render (request, 'informacoes_eventos.html')


'''
def cadastro_em_evento(request):
	eventos = Evento.objects.all()
    #print (request.POST.get('sel1'))
    if(request.method == 'POST'):
		#Usuario.setEventoCadastrado(request.POST.get('eventos'))
		Usuario.eventos_cadastrado = request.POST.get('eventos')
		redirect('/interface_usuario')
	return render(request,'cadastro_em_evento.html', {'eventos':eventos})
'''

def cadastro_em_evento(request, id):
    eventos = Evento.objects.all().filter(id=id)
    Usuario.setEventoCadastrado(eventos)
    Usuario.save
    #if (request.method == 'POST'):
    #    print("aaa")
    return render(request, 'cadastro_em_evento.html', {'eventos':eventos})


def noticia(request, id):
    #noticia = get_object_or_404(Noticia, id)
    noticia = Noticia.objects.get(id=id)
    return render(request, 'noticia.html', {'noticia':noticia})
    #return render(request, 'noticia.html')

#   eventos = Evento.objects.all()
    
#    return render(request, 'cadastro_em_evento.html', {'eventos':eventos})




# ---------------------------------------------------------------------------------------------------


#  VIEWS NAO UTILIZADAS - NAO MEXER
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                   password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def login_alternativo(request):
    if request.method == "POST":
        usuario = Usuario.objects.all()
        username = request.POST['username']
        password = request.POST['password']
        #user = authenticate(username=username, password=password)
        for user in usuario:
            if (user.getUsername() == username and user.getPassword() == password):
                return render(request, 'interface_usuario.html',{'user':user})
            else:
                return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')

