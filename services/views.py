from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from services.models import Sale, Making, Repair, Other
from services.forms import SaleFormCreate, MakingFormCreate, RepairFormCreate, OtherFormCreate
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
        repair = Repair.objects.filter(owner=user)
        other = Other.objects.filter(owner=user)

        context['sale_list'] = sale
        context['making_list'] = making
        context['repair_list'] = repair
        context['other_list'] = other
        return context

def get_number_sale(r_, pk):
    sale_list_objects = Sale.objects.all()
    sale_list_number = []
    file_list_number = get_number_order_list()
    for s_ in sale_list_objects:
        if s_.number:
            sale_list_number.append(s_.number)
    for f_ in file_list_number:
        if f_ not in sale_list_number:
            sale_list_number.append(f_)

    sale = Sale.objects.get(pk=pk)
    if sale.number:
        pass
    else:
        random_number = get_random_number()
        if random_number not in sale_list_number:
            sale.number = random_number
            set_number_order_list(random_number)
        else:
            sale.number = random_number + random_number
            set_number_order_list(random_number + random_number)
        sale.save()

    return redirect(reverse('services:all_calculations'))

class SaleDtailView(LoginRequiredMixin, DetailView):
    model = Sale

class SaleDeleteView(LoginRequiredMixin, DeleteView):
    model = Sale
    success_url = reverse_lazy('services:all_calculations')

    def form_valid(self, form):
        sale = self.object
        delete_number_in_order_list(sale.number)
        return super().form_valid(form)

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

def get_number_making(r_, pk):
    making_list_objects = Making.objects.all()
    making_list_number = []
    file_list_number = get_number_order_list()
    for m_ in making_list_objects:
        if m_.number:
            making_list_number.append(m_.number)
    for f_ in file_list_number:
        if f_ not in making_list_number:
            making_list_number.append(f_)

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

class RepairCreate(LoginRequiredMixin, CreateView):
    model = Repair
    form_class = RepairFormCreate
    success_url = reverse_lazy('services:all_calculations')

    def form_valid(self, form):
        repair = form.instance
        repair.owner = self.request.user
        return super().form_valid(form)

class RepairDeleteView(LoginRequiredMixin, DeleteView):
    model = Repair
    success_url = reverse_lazy('services:all_calculations')

    def form_valid(self, form):
        repair = self.object
        repair.image_one.delete(False)
        repair.image_two.delete(False)
        delete_number_in_order_list(repair.number)
        return super().form_valid(form)

def get_number_repair(r_, pk):
    repair_list_objects = Repair.objects.all()
    repair_list_number = []
    file_list_number = get_number_order_list()
    for r_ in repair_list_objects:
        if r_.number:
            repair_list_number.append(r_.number)
    for f_ in file_list_number:
        if f_ not in repair_list_number:
            repair_list_number.append(f_)

    repair = Repair.objects.get(pk=pk)
    if repair.number:
        pass
    else:
        random_number = get_random_number()
        if random_number not in repair_list_number:
            repair.number = random_number
            set_number_order_list(random_number)
        else:
            repair.number = random_number + random_number
            set_number_order_list(random_number + random_number)
        repair.save()

    return redirect(reverse('services:all_calculations'))

class RepairDtailView(LoginRequiredMixin, DetailView):
    model = Repair

class OtherCreate(LoginRequiredMixin, CreateView):
    model = Other
    form_class = OtherFormCreate
    success_url = reverse_lazy('services:all_calculations')

    def form_valid(self, form):
        other = form.instance
        other.owner = self.request.user
        return super().form_valid(form)

def get_number_other(r_, pk):
    other_list_objects = Other.objects.all()
    other_list_number = []
    file_list_number = get_number_order_list()
    for r_ in other_list_objects:
        if r_.number:
            other_list_number.append(r_.number)
    for f_ in file_list_number:
        if f_ not in other_list_number:
            other_list_number.append(f_)

    other = Other.objects.get(pk=pk)
    if other.number:
        pass
    else:
        random_number = get_random_number()
        if random_number not in other_list_number:
            other.number = random_number
            set_number_order_list(random_number)
        else:
            other.number = random_number + random_number
            set_number_order_list(random_number + random_number)
        other.save()

    return redirect(reverse('services:all_calculations'))

class OtherDeleteView(LoginRequiredMixin, DeleteView):
    model = Other
    success_url = reverse_lazy('services:all_calculations')

    def form_valid(self, form):
        other = self.object
        other.image_one.delete(False)
        other.image_two.delete(False)
        delete_number_in_order_list(other.number)
        return super().form_valid(form)

class OtherDtailView(LoginRequiredMixin, DetailView):
    model = Other

def start_bot(r_):
    start_vk_bot.delay()
    return redirect(reverse('javerly:home'))