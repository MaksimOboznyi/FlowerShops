from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('card/', views.card, name='card'),
    path('bouquet/<slug:slug>/', views.bouquet_detail, name='bouquet_detail'),
    path('consultation/', views.consultation, name='consultation'),
    path('order-step/', views.order_step, name='order-step'),
    path('order/', views.order, name='order'),
    path('quiz-step/', views.quiz_step, name='quiz-step'),
    path('quiz/', views.quiz, name='quiz'),
    path('result/', views.result, name='result'),
]
