from django.shortcuts import render

# Create your views here.
def scanner_view(request):
    return render(request, 'scanner/scanner.html')



