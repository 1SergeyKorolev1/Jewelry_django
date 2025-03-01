from django.urls import path
from services.apps import ServicesConfig
from services.views import (SaleCreate, RepairCreate, AllCalculationsList,
                            SaleDeleteView, RepairDeleteView, MakingCreate,
                            MakingDeleteView, get_number_making, get_number_sale,
                            start_bot, MakingDtailView, SaleDtailView, get_number_repair,
                            RepairDtailView, OtherCreate, get_number_other, OtherDeleteView,
                            OtherDtailView)

app_name = ServicesConfig.name

urlpatterns = [
    path('sale/', SaleCreate.as_view(), name='sale'),
    path('repair/', RepairCreate.as_view(), name='repair'),
    path('other/', OtherCreate.as_view(), name='other'),
    path('all_calculations/', AllCalculationsList.as_view(), name='all_calculations'),
    path('delete/sale/<int:pk>/', SaleDeleteView.as_view(), name='delete_sale'),
    path('delete/other/<int:pk>/', OtherDeleteView.as_view(), name='delete_other'),
    path('delete/repair/<int:pk>/', RepairDeleteView.as_view(), name='delete_repair'),
    path('making/', MakingCreate.as_view(), name='making'),
    path('delete/making/<int:pk>/', MakingDeleteView.as_view(), name='delete_making'),
    path('get_number_making/<int:pk>/', get_number_making, name='get_number_making'),
    path('get_number_sale/<int:pk>/', get_number_sale, name='get_number_sale'),
    path('get_number_other/<int:pk>/', get_number_other, name='get_number_other'),
    path('get_number_repair/<int:pk>/', get_number_repair, name='get_number_repair'),
    path('detail/making/<int:pk>/', MakingDtailView.as_view(), name='detail_making'),
    path('detail/sale/<int:pk>/', SaleDtailView.as_view(), name='detail_sale'),
    path('detail/other/<int:pk>/', OtherDtailView.as_view(), name='detail_other'),
    path('detail/repair/<int:pk>/', RepairDtailView.as_view(), name='detail_repair'),
    path('start_bot/call_only_once/jewelry_rybinsk_city/vk', start_bot, name='start_bot'),
]
