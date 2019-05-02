from django.shortcuts import render

# Create your views here.


def test(request, course_id, module_id):
    return render(request, 'ttest/test.html')

def test_result(request, course_id, module_id):
    return render(request, 'ttest/test_result.html')

# def test(request):
#     return render(request, 'ttest/tests.html')

# def test_result(request):
#     return render(request, 'ttest/resultsTests.html')

