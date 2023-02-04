from django.urls import path
from . import views

urlpatterns = [
    path('get_api/', views.UserList.as_view(), name='api_get'),
    path('get_user/', views.UserSingle.as_view(), name='api_get'),

    path('post_api/', views.UserCreate.as_view(), name='post_get'),
    path('update_api/<int:pk>', views.UserPut.as_view(), name='update_get'),
    path('delete_api/<int:pk>', views.UserDelete.as_view(), name='delete_api'),

]