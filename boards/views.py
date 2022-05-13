from django.http import FileResponse, Http404, StreamingHttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.db.models import Count
from .forms import NewTopicForm
from .models import Board, Topic


# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    queryset = board.topics.order_by('last_update').annotate(replies=Count('message') - 1)
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 20)

    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        topics = paginator.page(1)
    except EmptyPage:
        topics = paginator.page(paginator.num_pages)

    return render(request, 'topics.html', {'board': board, 'topics': topics})


def file_download(request, file_path):
    response = FileResponse(open("files/" + file_path, 'rb'))
    return response


@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = NewTopicForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            file = form.cleaned_data['file']

            topic = Topic()
            topic.subject = subject
            topic.message = message
            topic.file = file
            topic.file_path = file.__str__().split("/")[-1]
            topic.board = board
            topic.starter = request.user
            topic.save()

            return redirect('board_topics', pk=board.pk)
    else:
        form = NewTopicForm()

    return render(request, 'new_topic.html', {'board': board, 'form': form})
