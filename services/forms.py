from django import forms
from services.models import Sale, Making, Repair
from users.forms import StyleFormMixin

class SaleFormCreate(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('material', 'weight', 'sample_gold', 'sample_silver', 'sample_platinum')

class MakingFormCreate(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Making
        fields = ('material', 'weight', 'description', 'image_one', 'image_two')

class RepairFormCreate(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Repair
        fields = ('material', 'description', 'image_one', 'image_two')