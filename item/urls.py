from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('product/<int:product_id>/rate/', views.rate_product, name='rate_product'),
    path('prescription_upload/',views.prescription_upload, name='prescription_upload'),
    path('product/<int:product_id>/show_rating/',views.show_rating,name='show_rating'),
    path('product/<int:product_id>/reviews/', views.reviews_list, name='reviews_list'),

]
