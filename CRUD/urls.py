from django.urls import path
from .import views
urlpatterns = [

    path('', views.index, name='index'),
    path('create/', views.create_view, name='create'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit/<id>', views.edit_view, name='edit'),
    path('delete/<id>', views.delete_view, name='delete'),
    path('update/<id>', views.update_view, name='update'),
]
