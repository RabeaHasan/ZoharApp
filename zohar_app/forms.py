from django import forms
from zohar_app.models import Survey


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ('barcode', 'item', 'item_name', 'item_class', 'item_status', 'manufacturer_code', 'm_model_code', 'm_serial', 'piba_name',
                  'main_item_name', 'main_item_code', 'site_code', 'sub_site_name', 'location', 'checked_by', 'checked_date', 'remarks', 'actions')
        # fields = "__all__"
        # widgets = {
        #     # 'name': forms.TextInput(attrs={ 'class': 'form-control' }),
        #     # 'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
        #     'checked_date': forms.DateField(attrs={'type': 'date'}),
        # }
