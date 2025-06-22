from django.urls import path

from . import views

app_name = 'infra_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('second/', views.second_page, name='second_page'),

]
# для проверки на pep8
# pip install flake8 pep8-naming flake8-broken-line flake8-return flake8-isort
# flake8 .
# исправить недочеты в папке (если не можем найти сами (можно и все сразу))
# isort infra_project/urls.py
