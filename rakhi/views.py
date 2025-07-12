from django.shortcuts import render
from .models import Product
# Create your views here.
def home(request):
    kids = Product.objects.filter(category='kids')
    midrange = Product.objects.filter(category='midrange')
    bhaiya_bhabhi = Product.objects.filter(category='bhaiya_bhabhi')
    
    context = {
        'kids': kids,
        'midrange': midrange,
        'bhaiya_bhabhi': bhaiya_bhabhi,
    }
    return render(request, 'rakhi/home.html', context)