from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import Libro, Comentario
from AppCoder.forms import FormularioEdicion, FormularioCambioPassword, FormularioNuevoLibro, SearchForm, ActualizacionoLibro, UserCreationFormCustom, FormularioComentario
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.template import Template, Context
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


# Create your views here.

# def home(request):
#     return render(request, 'home.html', {})
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

class LoginPagina(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

class RegistroPagina(FormView):
    template_name = 'registro.html'
    form_class = UserCreationFormCustom
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)
    
class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'editar_perfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'passwordExitoso.html', {})



# def login_request(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data = request.POST)
#         if form.is_valid():  # Si pasó la validación de Django
#             user = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')


#             user = authenticate(username= user, password=password)


#             login(request, user)            
#             return render(request, "index.html", {"mensaje": f'Bienvenido {user.username}'})
#     else:
#         form = AuthenticationForm()
#     return render(request, "login.html", {"form": form})

#def register(request):
    #if request.method == 'POST':
        #form = UserCreationForm(request, data = request.POST)
        #if form.is_valid():
           # user = form.cleaned_data['username']
            #form.save()
            #return render(request, "index.html",  {"mensaje":"Usuario creado"})
        #else:
            #form = UserCreationForm()          
            #return render(request,"registro.html" ,  {"form":form})

# class RegisterView(CreateView):
#     template_name='registro.html'
#     form_class = UserCreationFormCustom
#     success_url = reverse_lazy('login')
    

# def libro_list(request):
#     libro = Libro.objects.all()
#     return render(request, 'libro_list.html', {'libro': libro})

# def libro_create(request):
#     if request.method == 'POST':
#         titulo = request.POST.get('titulo')
#         #libroCategoria = request.POST.get('libro')
#         autor = request.POST.get('autor')
#         libro = Libro(titulo=titulo, autor=autor) #libroCategoria=libroCategoria
#         libro.save()
#         return redirect(libro_list)
#     return render(request, 'libro_create.html')

# def libro_formulario(request):
#     if request.method == 'POST':
#         mi_formulario = FormularioNuevoLibro(request.POST)
        
#         print(mi_formulario)
        
#         if mi_formulario.is_valid:
#             informacion = mi_formulario.cleaned_data
#             libro = Libro(titulo=informacion["titulo"],autor=informacion["autor"])
#             libro.save()
#             return redirect('index')
#     else:
#         mi_formulario = FormularioNuevoLibro()
#         return render(request, 'libro_formulario.html', {"mi_formulario": mi_formulario})
    
    
# def libro_buscar(request):
#     libros = []
#     mi_formulario = SearchForm(request.GET) 
#     if mi_formulario.is_valid():
#         titulo = mi_formulario.cleaned_data.get('titulo')
#         if titulo:
#             libros = Libro.objects.filter(titulo__icontains=titulo)
#     return render(request, 'libro_buscar.html', {'mi_formulario': mi_formulario, 'libros': libros})

#ficcion y literatura
class ficcionListView(LoginRequiredMixin, ListView):
    model = Libro
    context_object_name = 'ficcion_list'
    queryset = Libro.objects.filter(libroCategoria__startswith='ficcion')
    template_name = 'ficcion_list.html'
    login_url = '/login/'

class ficcionDetailView(LoginRequiredMixin, DetailView):
    model = Libro
    context_object_name = 'ficcion'
    template_name = 'ficcion_detail.html'

class ficcionUpdate(LoginRequiredMixin, UpdateView):
    model = Libro
    form_class = ActualizacionoLibro
    success_url = reverse_lazy('ficcion_list')
    context_object_name = 'ficcion'
    template_name = 'ficcion_edit.html'

class ficcionDelete(LoginRequiredMixin, DeleteView):
    model = Libro
    success_url = reverse_lazy('ficcion_list')
    context_object_name = 'ficcion'
    template_name = 'ficcion_delete.html'


#Ciencias
class cienciasListView(LoginRequiredMixin, ListView):
    context_object_name = 'ciencias_list'
    queryset = Libro.objects.filter(libroCategoria__startswith='ciencias')
    template_name = 'ciencias_list.html'
    
class cienciasDetailView(LoginRequiredMixin,DetailView):
    model = Libro
    context_object_name = 'ciencias'
    template_name = 'ciencias_detail.html'

class cienciasUpdate(LoginRequiredMixin, UpdateView):
    model = Libro
    form_class = ActualizacionoLibro
    success_url = reverse_lazy('ciencias_list')
    context_object_name = 'ciencias'
    template_name = 'ciencias_edit.html'

class cienciasDelete(LoginRequiredMixin, DeleteView):
    model = Libro
    success_url = reverse_lazy('ciencias_list')
    context_object_name = 'ciencias'
    template_name = 'ciencias_delete.html'

#Infantil
class infantilListView(LoginRequiredMixin, ListView):
    context_object_name = 'infantil_list'
    queryset = Libro.objects.filter(libroCategoria__startswith='infantil')
    template_name = 'infantil_list.html'
    
class infantilDetailView(LoginRequiredMixin,DetailView):
    model = Libro
    context_object_name = 'infantil'
    template_name = 'infantil_detail.html'

class infantilUpdate(LoginRequiredMixin, UpdateView):
    model = Libro
    form_class = ActualizacionoLibro
    success_url = reverse_lazy('infantil_list')
    context_object_name = 'infantil'
    template_name = 'infantil_edit.html'

class infantilDelete(LoginRequiredMixin, DeleteView):
    model = Libro
    success_url = reverse_lazy('infantil_list')
    context_object_name = 'infantil'
    template_name = 'infantil_delete.html'

#Otras categorías
class otroListView(LoginRequiredMixin, ListView):
    context_object_name = 'otro_list'
    queryset = Libro.objects.filter(libroCategoria__startswith='otro')
    template_name = 'otro_list.html'

class otroDetailView(LoginRequiredMixin,DetailView):
    model = Libro
    context_object_name = 'otro'
    template_name = 'otro_detail.html'

class otroUpdate(LoginRequiredMixin, UpdateView):
    model = Libro
    form_class = ActualizacionoLibro
    success_url = reverse_lazy('otro_list')
    context_object_name = 'otro'
    template_name = 'otro_edit.html'

class otroDelete(LoginRequiredMixin, DeleteView):
    model = Libro
    success_url = reverse_lazy('otro_list')
    context_object_name = 'otro'
    template_name = 'otro_delete.html'


# CREACION INSTRUMENTO

class LibroCreacion(LoginRequiredMixin, CreateView):
    model = Libro
    form_class = FormularioNuevoLibro
    success_url = reverse_lazy('home')
    template_name = 'libro_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(LibroCreacion, self).form_valid(form)


# COMENTARIOS


class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'comentario.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

# ACERCA DE MI

def about(request):
    return render(request, 'acercaDeMi.html', {})

