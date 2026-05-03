from django.contrib import admin
from django.urls import path
from core.views import hello # Importe a função que você criou

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello), # Rota vazia significa a página inicial
]