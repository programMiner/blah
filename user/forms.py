from django import forms
from .models import BlogUser

class NewUserForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True,label='',
    widget=forms.TextInput(attrs={'name':'name','placeholder': 'name', 'class':'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white'}),
    )
    nickname = forms.CharField(max_length=255, label="", required=False,
    widget=forms.TextInput(attrs={'name':'nc','placeholder': 'Nick Name', 'class':'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500'})
    )
    password = forms.CharField(max_length=255, label="",
    widget=forms.PasswordInput(attrs={'name':'pw','placeholder': 'password', 'class':'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500'})
    )

    class Meta:
        model = BlogUser
        exclude = ('join','posts')