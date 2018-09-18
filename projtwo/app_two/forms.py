from django import forms
from django.core import validators
from .models import Logininfo,userprofileinfo
from django.contrib.auth.models import User
#for validating single term
# def check_for_a(value):
#     if value[0].lower()!='a':
#         raise forms.ValidationError('start with a')

class formName(forms.ModelForm):
    # name=forms.CharField()# for check_for_a enter validator=[check_for_a] in name charfield
    # email=forms.EmailField()
    # verify_email=forms.EmailField(label='enter gain')
    # text=forms.CharField(widget=forms.Textarea)
    # #for catching bot
    # #botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    # def clean(self):
    #     all_clean_data=super().clean()#by this we obtain all the form data whic was inputted by the user!!
    #     email=all_clean_data['email']
    #     vmail=all_clean_data['verify_email']
    #     if email != vmail:
    #         raise forms.ValidationError('not matched')
    
    
    
    class Meta:#This helps you to connect the model with form class
        model=Logininfo
        fields='__all__' #it helps to provide all the model info to form.
        #exclude=['email'] #to exclude particular objects display.
        #fields=('field1','field2') #to include only particular objects.
        
class userprofileinfoform(forms.ModelForm):
    class Meta:
        model=userprofileinfo
        fields=('portfolio_user','profile_image')
class userinfoform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','email','password')
        



    