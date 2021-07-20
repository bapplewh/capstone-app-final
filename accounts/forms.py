from django.forms import ModelForm
from .models import Order, Client


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'