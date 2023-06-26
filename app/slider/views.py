from django.shortcuts import render
from  .models import SliderItem
# Create your views here.


def index(request):
    slider_items = SliderItem.objects.all()
    context = {
        'slider_items': slider_items
    }

    return render(request, "slider/index.html", context)
