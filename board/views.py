from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from mguser.models import Mguser
from tag.models import Tag
from .models import Board
from .forms import BoardForm


# Create your views here.

def board_detail(request, pk): # 몇번째글인지 정보기 필요 -> pk로 설정
    # pk는 주소로 부터 입력받음
    # url에서 연결해줌
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist: # pylint 문법오류 / 실행 O
    #except Board.ObjectDoesNotExist:
        raise Http404('게시글을 찾을수 없습니다')
    return render(request, 'board_detail.html', {'board': board})

def board_write(request):
    if not request.session.get('user'):
        #세션 접근할때 로그인 사용자가 없으면 로그인으로
        return redirect('/mguser/login/')

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            mguser = Mguser.objects.get(pk=user_id)
            
            tags = form.cleaned_data['tags'].split(',')
            
            # cleaned_data로 가져올수 있음
            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = mguser
            board.save()

            for tag in tags:
                if not tag:
                    continue
                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect('/board/list/')
    else:
        form = BoardForm
    return render(request, 'board_write.html', {'form': form})

def board_list(request):
    all_boards = Board.objects.all().order_by('-id') # 가져오면서 최신것을 가져오게 정렬
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 4)
    #paginator를써서 쿼리셋에서 변경
    boards = paginator.get_page(page)

    return render(request, 'board_list.html', {'boards': boards})