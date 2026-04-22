from django.shortcuts import render, redirect
from .models import Bouquet

def index(request):
    return render(request, 'index.html')

def catalog(request):
    bouquets = Bouquet.objects.filter(is_active=True).select_related('occasion')
    return render(request, 'catalog.html'), {'bouquets': bouquets}

def card(request):
    return render(request, 'card.html')

def consultation(request):
    return render(request, 'consultation.html')

def order_step(request):
    return render(request, 'order-step.html')

def order(request):
    return render(request, 'order.html')

def quiz(request):
    if request.method == 'POST':
        event = request.POST.get('event')
        request.session['event'] = event
        return redirect('quiz-step')
    
    return render(request, "quiz.html")


def quiz_step(request):
    if request.method == 'POST':
        budget = request.POST.get('budget')
        request.session['budget'] = budget
        return redirect('result')
    return render(request, 'quiz-step.html')

def result(request):
    event = request.session.get('event')
    budget = request.session.get('budget')
    
    context = {
        'event': event,
        'budget': budget,
    }
    return render(request, 'result.html', context)