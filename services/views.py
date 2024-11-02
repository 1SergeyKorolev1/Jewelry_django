from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DeleteView
from services.models import Sale, Making
from services.forms import SaleFormCreate, MakingFormCreate
from services.functions import get_sale_price, get_making_price

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
        making = Making.objects.get(owner=self.request.user)
        print(making.image_one)
        making.image_one.delete(False)
        making.image_two.delete(False)
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