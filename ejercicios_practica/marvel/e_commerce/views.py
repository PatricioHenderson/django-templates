from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class BaseView(TemplateView):
    template_name = 'e_commerce/base.html'

class TablaView(TemplateView):
    template_name = 'e_commerce/00-tabla.html'

class ListaView(TemplateView):
    template_name = 'e_commerce/01-lista.html'

class FormularioView(TemplateView):
    template_name = 'e_commerce/02-formulario.html'

class TextoView(TemplateView):
    template_name = 'e_commerce/03-texto.html'

class ImagenView(TemplateView):
    template_name = 'e_commerce/04-imagen.html'