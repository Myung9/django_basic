from django.shortcuts import render
from .models import Board


# Create your views here.

def board_list(request):
    boards = Board.objects.all().order_by('-id') # 가져오면서 최신것을 가져오게 정렬
    return render(request, 'board_list.html', {'boards': boards})