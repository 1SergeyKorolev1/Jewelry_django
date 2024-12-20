from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from services.models import Sale, Making
from services.forms import SaleFormCreate, MakingFormCreate
from services.functions.functions_get_price import get_sale_price, get_making_price
from services.functions.get_random_number import get_random_number

from services.functions.number_order import (get_number_order_list,
                                             set_number_order_list,
                                             delete_number_in_order_list)

from services.functions.vk_api_message import start_vk_bot


class SaleCreate(LoginRequiredMixin, CreateView):
    model = Sale
    form_class = SaleFormCreate
    success_url = reverse_lazy('services:all_calculations')

    def form_valid(self, form):
        sale = form.instance
        sale.owner = self.request.user
        sale.result = get_sale_price(
            sale.material,
            sale.weight,
            sale.sample_gold,
            sale.sample_silver,
            sale.sample_platinum,
        )
        return super().form_valid(form)

class AllCalculationsList(LoginRequiredMixin, ListView):
    model = Sale
    extra_context = {
        'title_name_services': 'Ваши расчеты',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user = self.request.user
        sale = Sale.objects.filter(owner=user)
        making = Making.objects.filter(owner=user)

        context['sale_list'] = sale
        context['making_list'] = making
        return context

class SaleDeleteView(LoginRequiredMixin, DeleteView):
    model = Sale
    success_url = reverse_lazy('services:all_calculations')

class MakingDeleteView(LoginRequiredMixin, DeleteView):
    model = Making
    success_url = reverse_lazy('services:all_calculations')

    def form_valid(self, form):
        making = self.object
        making.image_one.delete(False)
        making.image_two.delete(False)
        delete_number_in_order_list(making.number)
        return super().form_valid(form)

class MakingCreate(LoginRequiredMixin, CreateView):
    model = Making
    form_class = MakingFormCreate
    success_url = reverse_lazy('services:all_calculations')

    def form_valid(self, form):
        making = form.instance
        making.owner = self.request.user
        making.result = get_making_price(
            making.material,
            making.weight,
        )
        return super().form_valid(form)

def get_number(r_, pk):
    making_list_objects = Making.objects.all()
    making_list_number = []
    for m_ in making_list_objects:
        if m_.number:
            making_list_number.append(m_.number)

    making = Making.objects.get(pk=pk)
    if making.number:
        pass
    else:
        random_number = get_random_number()
        if random_number not in making_list_number:
            making.number = random_number
            set_number_order_list(random_number)
        else:
            making.number = random_number + random_number
            set_number_order_list(random_number + random_number)
        making.save()

    return redirect(reverse('services:all_calculations'))


class MakingDtailView(LoginRequiredMixin, DetailView):
    model = Making

def start_bot(r_):
    start_vk_bot.delay()
    return redirect(reverse('javerly:home'))