from django.urls import path
from . import apis
from . import views


urlpatterns = [
    path("generics/", apis.TodoGenericsListCreateAPI.as_view()),
    path("generics/create/", apis.TodoGenericsCreateAPI.as_view()),
    path("generics/list/", apis.TodoGenericsListAPI.as_view()),
    path("generics/retrieve/<int:pk>/", apis.TodoGenericsRetrieveAPI.as_view()),
    path("generics/update/<int:pk>/", apis.TodoGenericsUpdateAPI.as_view()),
    path("generics/delete/<int:pk>/", apis.TodoGenericsDeleteAPI.as_view()),
    path("create/", apis.TodoCreateAPI.as_view()),
    path("list/", apis.TodoListAPI.as_view()),
    path("retrieve/<int:pk>/", apis.TodoRetrieveAPI.as_view()),
    path("update/<int:pk>/", apis.TodoUpdateAPI.as_view()),
    path("delete/<int:pk>/", apis.TodoDeleteAPI.as_view()),
    path("list/", views.todo_list),
    path("<int:pk>/", views.todo_detail),
    path("<str:name>/", views.todo_detail_name),
]