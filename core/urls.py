from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    HomeView,
    ItemDetailView,
    checkout,
    add_to_cart,
    remove_from_cart,
    login,
    signup
)

app_name = 'core'

urlpatterns = [
                  path('', HomeView.as_view(), name='home'),
                  path('checkout/', checkout, name='checkout'),
                  path('product/<slug>/', ItemDetailView.as_view(), name='product'),
                  path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
                  path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
                  path("login/", login, name="account_login"),
                  path("signup/", signup, name="account_signup")

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
