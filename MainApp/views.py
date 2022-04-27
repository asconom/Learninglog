from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm
# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')

def topics(request):
    topics = Topic.objects.all()

    context = {'topics': topics} 
#use the key in the html file and value in the view file

    return render(request, 'MainApp/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    #-date added is descending

    context = {'topic': 'topic', 'entries':entries}

    return render(request, 'MainApp/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)

        if form.is_valid():
            new_topic = form.save()

            return redirect('MainApp:topics')
    context = {'form':form}
    return render(request, 'MainApp/new_topic.html',context)