from django import forms
from zohar_app.models import  survey



class SurveyForm(forms.ModelForm):
    class Meta:
        model = survey
        fields = ('barcode','item', 'item_name', 'item_class','item_status','manufacturer_code','m_model_code','m_serial','piba_name','main_item_name','main_item_code','site_code','sub_site_name','location','checked_by','checked_date','remarks')
        # fields = "__all__"
