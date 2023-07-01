from django.shortcuts import render

from items.models import Category, Item

from .forms import SignupForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'items': items
    }
    return render(request, 'core/index.html', context)

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    form = SignupForm

    context = {
        'form': form
    }

    return render(request, 'core/signup.html    ', context)