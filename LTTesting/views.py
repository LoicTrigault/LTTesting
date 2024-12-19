from django.shortcuts import render

def site_view(request):
    return render(request, 'site.html')  # Charge site.html
