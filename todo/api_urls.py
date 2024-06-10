from django.urls import path, include
from . import apis
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", apis.TodoViewSet)

# 127.0.0.1:8000/todo/
urlpatterns = [
    # APIS
    # 127.0.0.1:8000/todo/
    # 127.0.0.1:8000/todo/<int:pk>/
    path("", include(router.urls)),
    path("generics/", apis.TodoGenericsListCreateAPI.as_view()),
    path("generics/<int:pk>/", apis.TodoGenericsRetrieveUpdateDeleteAPI.as_view()),
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
]