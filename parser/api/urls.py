from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('quotes/', views.getQuotes),
    path('quotes/<str:name>/', views.getQuote),
]