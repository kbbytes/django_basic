from django.shortcuts import render, HttpResponse, redirect
from .models import Item
# from django.template import loader
from .forms import ItemForm


def item(request):
    return HttpResponse("<h1>Thsi is an item view</h1>")


def index(request):
    item_list = Item.objects.all()
    context = {
        "item_list": item_list,
    }
    return render(request, "food/index.html", context)


def detail(request, item_id):
    detailItem = Item.objects.get(pk=item_id)
    context = {
        "item": detailItem,
    }
    return render(request, "food/detail.html", context)


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, "food/item-form.html", {'form': form})


def update_item(request, update_id):
    updateItem = Item.objects.get(id=update_id)

    form = ItemForm(request.POST or None, instance=updateItem)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, "food/item-form.html", {'form': form, 'item': updateItem})


def delete_item(request, delete_id):
    deleteItem = Item.objects.get(id=delete_id)
    if request.method == "POST":
        deleteItem.delete()

        return redirect("food:index")
    return render(request, "food/item-delete.html", {"item": deleteItem})
