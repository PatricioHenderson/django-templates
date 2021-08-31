from django.urls import path
from e_commerce.api.marvel_api_views import *

# Importamos las API_VIEWS:
from e_commerce.views import *

urlpatterns = [
    # e-commerce base
    path('base', BaseView.as_view()),
    path('tabla', TablaView.as_view()),
    path('lista', ListaView.as_view()),
    path('formulario', FormularioView.as_view()),
    path('texto', TextoView.as_view()),
    path('imagen', ImagenView.as_view()),
]