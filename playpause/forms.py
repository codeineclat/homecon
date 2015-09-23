from django import forms
 
from playpause.models import Uploadfile
 
 
class UploadFileForm(forms.ModelForm):
     
    class Meta:
        model = Uploadfile
        fields = '__all__'