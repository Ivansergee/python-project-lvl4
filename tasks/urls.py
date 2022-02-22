from django.urls import path
from . import views



urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('users/', views.UsersListView.as_view(), name='users_list'),
    path('users/create/', views.CreateUserView.as_view(), name='create_user'),
    # path('users/<int:pk>/update/', views.UpdateUserView.as_view(), name='change_user'),
    # path('users/<int:pk>/delete/', views.DeleteUserView.as_view(), name='delete_user'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout')
]
