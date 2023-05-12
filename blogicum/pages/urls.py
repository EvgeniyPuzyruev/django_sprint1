from django.urls import path
# from pages import views
from django.views.generic.base import TemplateView

app_name = 'pages'

urlpatterns = [
    path('about/', TemplateView.as_view(template_name='pages/about.html'),
         name='about'),
    path('rules/', TemplateView.as_view(template_name='pages/rules.html'),
         name='rules'),
]
# Действительно очень крутая штука, которая позволит "не множить сущее(view.py)
# без необходимости". Правда удалять его пока не буду, мало ли тесты не пройдут
# или потом понадобится
