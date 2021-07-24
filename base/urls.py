from django.urls import path
from .views import IndexView, CustomLoginView, CustomLogoutView, CustomCreateView, TaskCreateView, TaskDeleteView, TaskUpdateView, TaskDetailView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('create/', CustomCreateView.as_view(), name='create'),
    path('', IndexView.as_view(), name='index'),

    path('task-create/', TaskCreateView.as_view(), name='task-create'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task-detail/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

]