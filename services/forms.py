from django import forms
from services.models import Sale
from users.forms import StyleFormMixin

class SaleFormCreate(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('material', 'weight', 'sample_gold', 'sample_silver', 'sample_platinum')
