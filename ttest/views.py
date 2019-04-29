from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request, 'ttest/tests.html')

def test_result(request):
    return render(request, 'ttest/resultsTests.html')
