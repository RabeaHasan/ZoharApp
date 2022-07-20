from django import forms  
from zohar_app.models import Survey  
class SurveyForm(forms.ModelForm):  
    class Meta:  
        model = Survey  
        fields = "__all__"  