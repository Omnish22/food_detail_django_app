from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm 
from django.template import loader
from django.contrib.auth.decorators import login_required

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


# Create your views here.
# @login_required
# def index(request):
#     item_list = Item.objects.all()
#     template = loader.get_template('food/index.html')
#     context = {'item_list':item_list}
#     return HttpResponse(template.render(context, request))

class IndexClassView(ListView):
    model = Item
    template_name = "food/index.html"
    context_object_name = "item_list"


def item(request):
    return HttpResponse('<h1>This is item</h1>')

# @login_required
# def detail(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         'item':item
#     }
#     template = loader.get_template('food/details.html')
#     return HttpResponse(template.render(context, request))
class FoodDetail(DetailView):
    model = Item 
    template_name = 'food/details.html'



# @login_required
# def create_item(request):
#     form = ItemForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         # POST request
#         return redirect('food:index')
    
#     # GET request
#     return render(request, 'food/item-form.html', {'form':form})

class CreateItem(CreateView):
    model = Item 
    fields = ['item_name', 'item_description', 'item_price', 'item_image']
    template_name = "food/item-form.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user_name = self.request.user

        return super().form_valid(form)

@login_required
def edit_item(request, item_id):
    item = Item.objects.get(id = item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("food:index")

    return render(request, 'food/item-form.html', {'form':form, 'item':item})

@login_required
def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect("food:index")
    
    return render(request, 'food/delete-item.html')

    