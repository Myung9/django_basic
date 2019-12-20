from django.shortcuts import render, redirect
from mguser.models import Mguser
from .models import Board
from .forms import BoardForm


# Create your views here.

def board_detail(request, pk): # 몇번째글인지 정보기 필요 -> pk로 설정
    # pk는 주소로 부터 입력받음
    # url에서 연결해줌
    board = Board.objects.get(pk=pk)
    return render(request, 'board_detail.html', {'board': board})

def board_write(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            mguser = Mguser.objects.get(pk=user_id)
            
            # cleaned_data로 가져올수 있음
            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = mguser
            board.save()
            return redirect('/board/list/')
    else:
        form = BoardForm
    return render(request, 'board_write.html', {'form': form})

def board_list(request):
    boards = Board.objects.all().order_by('-id') # 가져오면서 최신것을 가져오게 정렬
    return render(request, 'board_list.html', {'boards': boards})