from django.urls import path
from .views import item_list
from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'

urlpatterns = [
    path('', item_list, name='item-list')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
