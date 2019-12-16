from django import forms
from .models import Mguser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    #username = forms.CharField(max_length=32, label="사용자 이름")
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        },
        max_length=32,
        label="사용자 이름"
    )
    #password = forms.CharField(widget=forms.PasswordInput, label="비밀번호")
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput,
        label='비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean() # 기존 form안에 있는 clean
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            mguser = Mguser.objects.get(username=username)
            if not check_password(password, mguser.password):
                self.add_error('password', '비밀번호가 틀렸습니다')
            else: # view의 login에서 접근하기위해
                self.user_id = mguser.id
