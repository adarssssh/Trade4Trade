from django.shortcuts import render

from .models import Book

# Create your views here.
def addBooks(request):
    if request.method == 'POST':
        if request.POST.get('title'):
            details = Book()
            details.title = request.POST.get('title')
            details.category = request.POST.get('category')
            details.tags = request.POST.get('tags')
            details.discription = request.POST.get('discription')
            details.price = request.POST.get('price')
            details.img = request.POST.get('img')

            details.save()

            return render(request, 'add_books.html', {})

    else:
        return render(request, 'add_books.html', {})

def viewBooks(request):
    obj = Book.objects.get(id=66)
    return render(request, 'homepage.html', {'details': obj})