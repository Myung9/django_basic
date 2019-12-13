from django import forms
from .models import Mguser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label="사용자 이름")
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and passworld:
            mguser = Mguser.objects.get(usernae=username)
            if not check_password(password, mguser.password):
                self.add_error('password', '비밀번호가 틀렸습니다')
