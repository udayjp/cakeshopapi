from django.urls import path,include
from django.conf.urls import url
from .views import *

urlpatterns=[
    path('register',UserRegistrationView.as_view(),name='user_registration'),
    path('user',UserView.as_view(),name='user'),
    path('cakes',CakeListView.as_view(),name='cakes'),
    url(r'^search/(?P<name>\w+)/$', CakeSearchListView.as_view(), name='search'),
    path('addcake',CakeCreateView.as_view(),name='add_cakes'),
    path('addtocart',CartCreateView.as_view(),name='add_tocart'),
    path('cartitems',CartView.as_view(),name='cart_items'),
    path('removecartitem/<int:pk>',CartView.as_view(),name='removecartitems'),
    path('orders',OrdersView.as_view(),name='orders'),
    path('cakes/<int:pk>',CakeDetailsRetrieveView.as_view(),name='cake_details'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),


]

