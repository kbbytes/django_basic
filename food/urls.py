from . import views
from django.urls import path


app_name = 'food'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:item_id>', views.detail, name="detail"),
    path('item/', views.item, name="item"),
    path('add/', views.create_item, name="create_item"),
    path('update/<int:update_id>/', views.update_item, name="update_item"),
    path('delete/<int:delete_id>/', views.delete_item, name="delete_item"),

]
