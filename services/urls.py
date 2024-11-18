from django.urls import path
from services.apps import ServicesConfig
from services.views import (SaleCreate, AllCalculationsList,
                            SaleDeleteView, MakingCreate,
                            MakingDeleteView, get_number,
                            start_bot, MakingDtailView)
app_name = ServicesConfig.name

urlpatterns = [
    path('sale/', SaleCreate.as_view(), name='sale'),
    path('all_calculations/', AllCalculationsList.as_view(), name='all_calculations'),
    path('delete/sale/<int:pk>/', SaleDeleteView.as_view(), name='delete_sale'),
    path('making/', MakingCreate.as_view(), name='making'),
    path('delete/making/<int:pk>/', MakingDeleteView.as_view(), name='delete_making'),
    path('get_number/<int:pk>/', get_number, name='get_number'),
    path('detail/making/<int:pk>/', MakingDtailView.as_view(), name='detail_making'),
    path('start_bot/call_only_once/jewelry_rybinsk_city/vk', start_bot, name='start_bot'),
]