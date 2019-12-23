from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Mguser
from .forms import LoginForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # 기본 유효성검사 = 값의 유무
        # form.py에 추가사항 
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
            
        
    else:
        form = LoginForm() # 빈 클래스 변수 생성
    return render(request, 'Login.html', {'form': form})
    

def register(request):
    # 레지스터로 들어오는 요청이 2개있음
    # 접속 / 등록을 눌러서
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        

        res_data = {}

        if not (username and password and re_password):
            res_data['error'] = '모든 값을 입력하세요'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'
        else:
            mguser = Mguser(
                username=username,
                useremail=useremail,
                password=make_password(password),
            )
            mguser.save()

        return render(request, 'register.html', res_data)