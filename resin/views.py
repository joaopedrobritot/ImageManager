from django.shortcuts import render
from django.http import HttpResponse
from .models import Calculator
from .forms import CalculatorForm
from . import ResinCalculator

def calculator(request):
    data = {}
    if request.method == 'POST':
        data['form'] = CalculatorForm(request.POST)

        if data['form'].is_valid():
            data['result'] = ResinCalculator.resinCalculator(request.POST.get('your_resin'), request.POST.get('target_resin'))
            data['form'] = CalculatorForm()
            return render(request, 'calculator.html', data)
    else:
        data['form'] = CalculatorForm()
        data['result'] = '99:99'
        return render(request, 'calculator.html', data)