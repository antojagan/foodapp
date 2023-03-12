from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Create your views here.
def index(request):
    item_list = Item.objects.all()
    
    context = {
        'item_list':item_list,
    }
    return render(request, 'foo/index.html',context)

class IndexClassView(ListView):
    model = Item;
    template_name = 'foo/index.html'
    context_object_name = 'item_list'

def item(request):
    return HttpResponse('This is an another view')

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context ={
        'item':item,
    }
    return render(request, 'foo/detail.html',context)

class FoodDetail(DetailView):
    model = Item
    template_name = 'foo/detail.html'


def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('foo:index')
    return render(request, 'foo/item-form.html', {'form':form})



def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('foo:index')
    return render(request, 'foo/item-form.html', {'form':form,'item':item})

def delete_item(request,id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('foo:index')
    return render(request, 'foo/item-delete.html', {'item':item})




