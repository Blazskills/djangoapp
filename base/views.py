from django.db import models
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Task
# Create your views here.



class TaskList(ListView):
    model = Task
    template_name = "base/index.html"
    context_object_name = "tasks"


class TaskDetail(DetailView):
    model=Task
    context_object_name = "tasks"
    template_name = 'base/todo-detail.html'
    