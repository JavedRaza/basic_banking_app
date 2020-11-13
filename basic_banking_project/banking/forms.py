from django.forms import ModelForm
from .models import Transfer


class TransferForm(ModelForm):
	class Meta:
		model = Transfer
		fields = '__all__'