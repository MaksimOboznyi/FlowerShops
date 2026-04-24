from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('card/', views.card, name='card'),
    path('bouquet/<slug:slug>/', views.bouquet_detail, name='bouquet_detail'),
    path('consultation/', views.consultation, name='consultation'),
    path('consultation/done/', views.consultation_done, name='consultation-done'),
    path('order/done/', views.order_done, name='order-done'),
    path('order/<slug:slug>/', views.order, name='order'),
    path('order-step/', views.order_step, name='order-step'),
    path('quiz-step/', views.quiz_step, name='quiz-step'),
    path('quiz/', views.quiz, name='quiz'),
    path('result/', views.result, name='result'),
]
