from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("seguros/", views.insurance, name="insurance"),
    path("alugeis/", views.rent, name="rent"),
    path("vendas/", views.sale, name="sale"),
    path("servicos/", views.service, name="service"),
    path("anotacoes/", views.notes, name="notes"),
    path("receita_diaria/", views.daily_income, name="daily_income"),
    path("receita_mensal/", views.monthly_income, name="monthly_income"),
    path("pagar/<str:contract>/<int:pk>", views.pay, name="pay"),
    path("editar/<str:contract>/<int:pk>", views.edit, name="edit"),
    path("deletar/<str:contract>/<int:pk>", views.delete, name="delete"),
    path("deletar_anotacao/<int:pk>", views.delete_note, name="delete_note"),
    path("contrato/<str:contract>/<int:pk>", views.print_contract, name="print_contract"),
    path("clientes/<str:contract>/<str:value>", views.print_client_list, name="print_client_list")
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)