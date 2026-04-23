from django.shortcuts import render, redirect, get_object_or_404

from .forms import OrderForm
from .models import Bouquet


def index(request):
    recommended_bouquets = Bouquet.objects.filter(is_active=True).order_by('?')[:3]
    return render(request, 'index.html', {'recommended_bouquets': recommended_bouquets})


def catalog(request):
    bouquets = Bouquet.objects.filter(is_active=True).select_related('occasion')
    return render(request, 'catalog.html', {'bouquets': bouquets})


def bouquet_detail(request, slug):
    bouquet = get_object_or_404(Bouquet, slug=slug, is_active=True)
    return render(request, 'card.html', {'bouquet': bouquet})


def card(request):
    return render(request, 'card.html')


def consultation(request):
    return render(request, 'consultation.html')


def consultation_done(request):
    return render(request, 'consultation_done.html')


def order(request, slug):
    bouquet = get_object_or_404(Bouquet, slug=slug, is_active=True)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.bouquet = bouquet
            new_order.save()
            return redirect('order-done')
    else:
        form = OrderForm()

    return render(request, 'order.html', {'form': form, 'bouquet': bouquet})


def order_done(request):
    return render(request, 'order_done.html')


def order_step(request):
    return render(request, 'order-step.html')


def quiz(request):
    if request.method == 'POST':
        request.session['event'] = request.POST.get('event')
        return redirect('quiz-step')
    return render(request, 'quiz.html')


def quiz_step(request):
    if request.method == 'POST':
        request.session['budget'] = request.POST.get('budget')
        return redirect('result')
    return render(request, 'quiz-step.html')


def result(request):
    event = request.session.get('event')
    budget = request.session.get('budget')
    return render(request, 'result.html', {'event': event, 'budget': budget})