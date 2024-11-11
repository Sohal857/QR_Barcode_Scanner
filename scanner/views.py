from django.shortcuts import render
from django.http import JsonResponse
from .models import ScannedData
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def scanner_view(request):
    return render(request, 'scanner/scanner.html')

@csrf_exempt
def submit_scan(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            scanned_data = data.get('scanned_data')
            if scanned_data:
                # Save scanned data to the database
                ScannedData.objects.create(data=scanned_data)
                return JsonResponse({'status': 'success', 'message': 'Data saved successfully!'})
            else:
                return JsonResponse({'status': 'error', 'message': 'No data provided'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)