from django.forms import ModelForm
from main.models import Store

class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = ["name", "price", "description", "category", "thumbnail", "is_featured"]