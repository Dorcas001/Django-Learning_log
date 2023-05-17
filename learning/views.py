from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

@login_required
def topic(request):
    topic = Topic.objects.filter(author=request.user).order_by('-date_created')
    context = {'topic':topic}
    return render(request, 'learning/topic.html', context)

@login_required
def new_topic(request):
    if request.method !='POST':
        # if no data is submitted, create a blank form
        form = TopicForm()
    else:
        form = TopicForm(request.POST) 
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.author = request.user
            new_topic.save()
            return redirect('topic')

    context = {'form': form} 
    return render(request, 'learning/new_topic.html', context)

@login_required
def topic_details(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.author != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_created')
    context = {'topic' : topic, 'entries': entries}
    return render(request, 'learning/detail.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # no data submitted create ablank post
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST) 
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('detail', topic_id=topic_id )
    context = {'topic':topic, 'form':form}         
    return render(request, 'learning/new_entries.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method !='POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('topic')

    context = {'form':form, 'topic':topic, 'entry':entry}
    return render(request, 'learning/edit.html', context)

def home(request):
    return render(request, 'learning/home.html')
def about(request):
    return render(request, 'learning/about.html')

