from django import views
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .views import HomeView, LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword, LibroCreacion, ComentarioPagina, ficcionListView, ficcionDetailView, ficcionUpdate, ficcionDelete, cienciasListView, cienciasDetailView, cienciasUpdate, cienciasDelete, infantilListView, infantilDetailView, infantilDelete, infantilUpdate, otroListView, otroDelete, otroDetailView, otroUpdate

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),
    #path('libro_list/', LibroCreacion.as_view(), name='libro_list'),
    path('libro_create/', LibroCreacion.as_view(), name='libro_create'),
    #path('libro_formulario/', views.libro_formulario, name='libro_formulario'),
    #path('libro_buscar/', views.libro_buscar, name='libro_buscar'),
    path('ficcion_list/', views.ficcionListView.as_view(), name='ficcion_list'),
    path('ficcion_detail/<int:pk>/', views.ficcionDetailView.as_view(), name='ficcion_detail'),
    path('ficcion_edit/<int:pk>/', views.ficcionUpdate.as_view(), name='ficcion_edit'),
    path('ficcion_delete/<int:pk>/', views.ficcionDelete.as_view(), name='ficcion_delete'),
    path('ficcion_detail/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('ciencias_list/', views.cienciasListView.as_view(), name='ciencias_list'),
    path('ciencias_detail/<int:pk>/', views.cienciasDetailView.as_view(), name='ciencias_detail'),
    path('ciencias_edit/<int:pk>/', views.cienciasUpdate.as_view(), name='ciencias_edit'),
    path('ciencias_delete/<int:pk>/', views.cienciasDelete.as_view(), name='ciencias_delete'),
    path('ciencias_detail/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('infantil_list/', views.infantilListView.as_view(), name='infantil_list'),
    path('infantil_detail/<int:pk>/', views.infantilDetailView.as_view(), name='infantil_detail'),
    path('infantil_edit/<int:pk>/', views.infantilUpdate.as_view(), name='infantil_edit'),
    path('infantil_delete/<int:pk>/', views.infantilDelete.as_view(), name='infantil_delete'),
    path('infantil_detail/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('otro_list/', views.otroListView.as_view(), name='otro_list'),
    path('otro_detail/<int:pk>/', views.otroDetailView.as_view(), name='otro_detail'),
    path('otro_edit/<int:pk>/', views.otroUpdate.as_view(), name='otro_edit'),
    path('otro_delete/<int:pk>/', views.otroDelete.as_view(), name='otro_delete'),
    path('otro_detail/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    # path('login/', views.login_request, name='login'),
    # path('logout/', views.login_request, name='logout'),
    # path('registro/', views.RegisterView.as_view(), name='registro'),
    path('acercaDeMi/', views.about, name='acercaDeMi'),
]



#path('instrumentoCreacion/', InstrumentoCreacion.as_view(), name='nuevo'),