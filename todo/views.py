from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
import operator
# Create your views here.
from .models import Task
from .forms import TaskForm


def todo_view(request, id, *args, **kwargs):
    task = get_object_or_404(Task, id=id)
    context = {'object': task}
    return render(request, 'todo_detail.html', context)


def todo_delete(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        print(task)
        task.delete()
        return redirect('../../')
    context = {'object': task,
               }
    return render(request, 'todo_delete.html', context)


def todo_create(request, *args, **kwargs):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TaskForm()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, 'todo_create.html', context)


def todo_list_view(request, *args, **kwargs):
    queryset = Task.objects.all()
    print(queryset)
    queryset= sorted(queryset,key=operator.attrgetter('date','time'))
    # queryset.sort(key=lambda x : x.time)
    context = {
        'object_list': queryset
    }
    return render(request, 'todo_list.html', context)


def todo_update(request, id, *args, **kwargs):
    task = get_object_or_404(Task, id=id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        form = TaskForm()
        return redirect('../../')

    context = {
        'form': form
    }
    return render(request, 'todo_create.html', context)
