from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import ExtendUser
from post.models import *
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.core.validators import *
# Create your views here.

def register(request):
    state = " Se dispone a realizar un nuevo registro.Recuerde que todos los campos son obligatorios"

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
			
            name_user = form.cleaned_data['username']
            email_user = form.cleaned_data['email']
            pass_user = form.cleaned_data['password1']
            create_user = User.objects.create_user(username= name_user, email= email_user,password=pass_user)           
            create_user.save()
            pseudo="@"+name_user
            extend=ExtendUser(user=create_user,pseudo=pseudo)
            extend.save()


            return redirect('/login')
        else:
				
			  state=" Error en el registro"
			  return render_to_response('nuevo.html', {'title':'Registro', 'formulario': form,'state':state}, context_instance=RequestContext(request))
    else:
        form =  RegistrationForm()
    return render_to_response('nuevo.html', {'title':'Registro', 'formulario': form,'state':state}, context_instance=RequestContext(request))


def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        state = "Password o usuario incorrecto."
        user = authenticate(username=username, password=password)
      
			
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return redirect('/home.html')
            else:
                state = "Your account is not active, please contact the site admin."
        else:
			try:
				userna=User.objects.get(email=username)
				user = authenticate(username=userna.username, password=password)
			except:
				state = "Password o usuario incorrecto."
				return render_to_response('login.html',{'title':'Login', 'state':state, 'username': username}, context_instance=RequestContext(request))

			if user is None:	
				state = "Password o usuario incorrecto."
			if user.is_active:
				login(request, user)
				
				return redirect('/home.html')
			else:
				return redirect('/home.html')
				state = "Your account is not active, please contact the site admin."

    return render_to_response('login.html',{'title':'Login', 'state':state, 'username': username}, context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return redirect('/home')
	
	
def update(request):
	error='Recuerde que las dos password deben coincidir.'
	usuario = request.user
	extendido = ExtendUser.objects.get(user=usuario)
	pseudo = extendido.pseudo[1:len(extendido.pseudo)]
	if request.method=='POST':
		usuario.username=request.POST.get('username')

		if request.POST.get('password'):

			if request.POST.get('password') == request.POST.get('rpassword'):
				usuario.set_password(request.POST.get('password'))
				error = "El password ha sido actualizado correctamente."
			else:
				error = "Los password no coinciden."
		try:
			if validate_email(request.POST.get('email')):
				usuario.email=request.POST.get('email')
		except:

			if error == 'Recuerde que los password deben coincidir.':

				error = "El e-mail es incorrecto."
			else:
				error = error + " El e-mail es incorrecto."

		usuario.save()
		if extendido.pseudo!=request.POST.get('alias'):
			extendido.pseudo='@'+request.POST.get('alias')

		if request.POST.get('photo'):
			extendido.photo=request.POST.get('photo')
		if "borrar" in request.POST.keys():
			extendido.photo='/static/img/default/defaultProfile.png'

		extendido.save()

	return render_to_response('profile.html', {'title':'Informacion personal', 'User': usuario, 'Extend':extendido, 'MERROR':error, 'Alias':pseudo}, context_instance=RequestContext(request))


def follow(request, user_id):
	if not request.user.is_authenticated():
		return redirect('/login/?next=%s' % request.path)
	else:
		
		usuario=ExtendUser.objects.get(user = request.user)
		usuario.followers.add(User.objects.get(id = user_id))
		return redirect('/home/')	
def unfollow(request, user_id):
	if not request.user.is_authenticated():
		return redirect('/login/?next=%s' % request.path)
	else:
		
		usuario=ExtendUser.objects.get(user = request.user)
		usuario.followers.remove(User.objects.get(id = user_id))
		return redirect('/home/')	
def deluser(request):
	if not request.user.is_authenticated():
		return redirect('/login/?next=%s' % request.path)
	else:
		E=ExtendUser.objects.get(user = request.user)
		E.delete()
		U=request.user
		logout(request)
		U.delete()
		return redirect('/index/')		

def perfil(request, user_id):
	if not request.user.is_authenticated():
		return redirect('/login/?next=%s' % request.path)
	else:
		
		usuario=User.objects.get(id=user_id)
		usuario_=ExtendUser.objects.get(user=usuario) 
		post=[]
		User__=usuario_.followers.all()
		followers=[]
		for u in (User__):
			followers.append(ExtendUser.objects.get(user=u))
		for t in Post.objects.all():
			if (t.creator==usuario):
				post.append(t)
		
		return render_to_response('perfil.html', {'title':'Perfil', 'user': usuario, 'User': usuario_, "tweets":post, 'follower':followers})
	
