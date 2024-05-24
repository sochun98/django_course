from django.urls import path
from . import views


urlpatterns = [
    path("list/", views.todo_list),
    path("<int:pk>/", views.todo_detail),
    path("<str:name>/", views.todo_detail_name),
]