from django.shortcuts import render,redirect
from django.http import  HttpResponse
from .models import Board
from django.contrib import messages




def home(request):
    boards = Board.objects.all()
    return render(request,'home.html',{'boards':boards})
    # boards_name = list()
    # for board in boards:
    #     boards_name.append(board.name)

    # response_html = '<br>'.join(boards_name)
    # return HttpResponse(response_html)


def delete_board(request):
    board = Board.objects.get(pk= request.GET["t"] )
    board.delete()
    messages.success(request,'Registro eliminado con exito')
    return redirect('home')

def new_board(request):
    return render(request,'new_board.html')