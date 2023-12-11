from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField,AuthenticationForm
from django.utils.translation import gettext_lazy as ul
from django.contrib.auth import authenticate

from .models import SUser, UserManager


class EmailAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(label='Email',required=True)
    password = forms.CharField(label='Password', widget= forms.PasswordInput)

    class Meta:
        model = SUser
        fields = ('email', 'password')
    
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid email or password')

#유저 회원가입
class RegisterForm(forms.ModelForm):
    email = forms.EmailField(
        label=ul('Email'),
        required=True, 
    )
    nickname = forms.CharField(
        label=ul('Nickname'),
        required=True,
    )
    password1 = forms.CharField(
        label = ul("비밀번호"),
    )
    password2 = forms.CharField(
        label = ul('비밀번호 확인'),
    )
    class Meta:
        model = SUser
        fields = ('email','nickname',)
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 !=password2:
            raise forms.ValidationError("입력한 비밀번호가 일치하지 않습니다.")
        return password2    
    
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = UserManager.normalize_email(self.cleaned_data['email'])
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
class SUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label = ul('Password')
    )
    class Meta:
        model=SUser
        fields = ('password',)
    def clean_password(self):
        return self.initial['password']
    def save(self, commit=True):
        user = SUser.objects.get()
        user.set_password(self.cleaned_data['Password'])
        if commit:
            user.save()
        return user