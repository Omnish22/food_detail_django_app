from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm 
from django.template import loader


# Create your views here.
def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {'item_list':item_list}
    return HttpResponse(template.render(context, request))


def item(request):
    return HttpResponse('<h1>This is item</h1>')

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item
    }
    template = loader.get_template('food/details.html')
    return HttpResponse(template.render(context, request))

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        # POST request
        return redirect('food:index')
    
    # GET request
    return render(request, 'food/item-form.html', {'form':form})

def edit_item(request, item_id):
    item = Item.objects.get(id = item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("food:index")

    return render(request, 'food/item-form.html', {'form':form, 'item':item})


def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect("food:index")
    
    return render(request, 'food/delete-item.html')

    