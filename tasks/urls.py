from django.urls import path
from . import views



urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('users/', views.UsersListView.as_view(), name='users_list'),
    path('users/create/', views.CreateUserView.as_view(), name='create_user'),
    path('users/<int:pk>/update/', views.UpdateUserView.as_view(), name='change_user'),
    path('users/<int:pk>/delete/', views.DeleteUserView.as_view(), name='delete_user'),

    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),

    path('statuses/', views.StatusesListView.as_view(), name='statuses_list'),
    path('statuses/create/', views.CreateStatusView.as_view(), name='create_status'),
    path('statuses/<int:pk>/update/', views.UpdateStatusView.as_view(), name='change_status'),
    path('statuses/<int:pk>/delete/', views.DeleteStatusView.as_view(), name='delete_status'),

    path('tasks/', views.TasksListView.as_view(), name='tasks_list'),
    path('tasks/create/', views.CreateTaskView.as_view(), name='create_task'),
    path('tasks/<int:pk>/update/', views.UpdateTaskView.as_view(), name='change_task'),
    path('tasks/<int:pk>/delete/', views.DeleteStatusView.as_view(), name='delete_task'),
    path('tasks/<int:pk>', views.StatusesListView.as_view(), name='task'),
]
