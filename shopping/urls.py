from django.urls import path, include
from . import views as my_views

# Imports for serving media images on debug mode
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', my_views.HomePageView.as_view(), name='home'),
    path('about', my_views.AboutPageView.as_view(), name='about'),
    path('soon', my_views.SoonPageView.as_view(), name='soon'),
    
    path('products/new/', my_views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:product_pk>/edit/', my_views.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:product_pk>/delete/', my_views.ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:product_pk>/comments/', include('comments.urls')),
    path('products/<int:product_pk>/', my_views.ProductDetailView.as_view(), name='product_detail'),
    path('products', my_views.ProductListView.as_view(), name='product_list'),

    path('cart/add/', my_views.cart_submit, name='cart_create'),
    path('cart/<int:pk>/delete/', my_views.CartDeleteView.as_view(), name='cart_delete'),
    path('cart/', my_views.CartListView.as_view(), name='cart_list'),
]

# url for serving media on debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)