from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView
from services.models import Sale
from services.forms import SaleFormCreate
from services.functions import get_sale_price

class SaleCreate(LoginRequiredMixin, CreateView):
    model = Sale
    form_class = SaleFormCreate
    success_url = reverse_lazy('services:all_calculations')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.result = get_sale_price(form.instance.material, form.instance.weight)
        return super().form_valid(form)

class AllCalculationsList(LoginRequiredMixin, ListView):
    model = Sale
    extra_context = {
        'title_name_services': 'Ваши расчеты',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        sale = Sale.objects.all()

        context['sale_list'] = sale
        return context
