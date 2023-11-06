from django.shortcuts import render, HttpResponse, redirect
from .models import Item
# from django.template import loader
from .forms import ItemForm
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def item(request):
    return HttpResponse("<h1>This is an item view</h1>")


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
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('food:index')
    else:
        form = ItemForm()

    return render(request, 'food/item-form.html', {'form': form})


def update_item(request, update_id):
    updateItem = Item.objects.get(id=update_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=updateItem)
        if form.is_valid():
            form.save()
            return redirect('food:index')
    else:
        form = ItemForm(instance=updateItem)

    return render(request, 'food/item-form.html', {'form': form, 'item': updateItem})


def delete_item(request, delete_id):
    deleteItem = Item.objects.get(id=delete_id)
    if request.method == "POST":
        deleteItem.delete()

        return redirect("food:index")
    return render(request, "food/item-delete.html", {"item": deleteItem})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("food:index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="food/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("food:index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="food/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("food:index")
