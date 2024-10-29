from django.urls import path
from services.apps import ServicesConfig
from services.views import SaleCreate, AllCalculationsList, SaleDeleteView
app_name = ServicesConfig.name

urlpatterns = [
    path('sale/', SaleCreate.as_view(), name='sale'),
    path('all_calculations/', AllCalculationsList.as_view(), name='all_calculations'),
    path('delete/<int:pk>', SaleDeleteView.as_view(), name='delete_sale'),
]