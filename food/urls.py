from django.urls import path
from . import views

app_name='food'
urlpatterns = [
    # food/
    path('', views.index, name='index'),

    # food/item/
    path('item/',views.item, name='item'),

    # food/1/
    path('<int:item_id>/',views.detail, name='detail'),

    # food/add/
    path("add/", views.create_item, name="create_item"),

    # food/edit/2
    path("edit/<int:item_id>/", views.edit_item, name="edit_item"),

    # food/delete/
    path("delete/<int:item_id>", views.delete_item, name="delete_item")
]
