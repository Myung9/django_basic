from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Mguser


# Create your views here.
def home(requset):
    user_id = requset.session.get('user')
    if user_id:
        mguser = Mguser.objects.get(pk=user_id)
        return HttpResponse(mguser.username)
    return HttpResponse('Home!')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

def login(request):
    if request.method == 'GET': # get으로오면 화면만 그냥 보여주고
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not (username and password):
            res_data['error'] = '모든 값을 입력하세요.'
        else:
            mguser = Mguser.objects.get(username=username)
            if check_password(password, mguser.password):
                #로그인 처리
                # 여기에 세션으로 로그인 처리
                # 1. 세션
                # 2. home으로 보내기 (redirect / shortcut의 redirect)
                request.session['user'] = mguser.id
                return redirect('/')
            else:
                #비밀번호 에러 처리
                res_data['error'] = '비밀번호가 틀렸습니다.'

        return render(request, 'login.html', res_data)

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