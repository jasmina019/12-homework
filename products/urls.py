from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'
urlpatterns = [
    path('about_page/', views.about_page, name='about'),
    path('product_list/', views.products_list, name='list'),
    path('product_detail/<int:pk>/', views.product_detail, name='detail'),
    path('product_create/', views.product_create, name='create'),
] + static(settings.MEDIA_URL, documnt_root=settings.MEDIA_ROOT)
