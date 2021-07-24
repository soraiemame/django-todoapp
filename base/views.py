from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm

from .models import Task


# Create your views here.
class IndexView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'base/index.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['madebyme'] = 'soraie'
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(completed=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__istartswith=search_input)
        context['search_input'] = search_input
        return context


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'base/login.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(CustomLoginView, self).get(*args, **kwargs)


class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'base/logout.html'


class CustomCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'base/create.html'
    success_url = reverse_lazy('login')

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(CustomCreateView, self).get(*args, **kwargs)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'base/task-create.html'
    context_object_name = 'form'
    fields = ("title", "description", "completed")
    # fields = '__all__'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'base/task-detail.html'
    context_object_name = 'task'


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'base/task-delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('index')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'base/task-update.html'
    # fields = '__all__'
    fields = ("title", "description", "completed")
    success_url = reverse_lazy('index')


