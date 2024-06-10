from django.urls import path, include
from . import views


# 127.0.0.1:8000/todo/
urlpatterns = [
    
    # VIEWS
    path("create/", views.TodoCreateView.as_view()),    # 127.0.0.1:8000/todo/create/
    path("list/", views.todo_list), # 127.0.0.1:8000/todo/list/
    path("<int:pk>/", views.todo_detail),   # 127.0.0.1:8000/todo/<int:pk>/
    path("<str:name>/", views.todo_detail_name),    # 127.0.0.1:8000/todo/<str:name>/
]