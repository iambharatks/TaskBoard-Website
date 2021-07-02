from django.urls import path
from .views import(
    todo_list_view,
    todo_view,
    todo_create,
    todo_delete,
    todo_update
)

app_name = 'todo'
urlpatterns = [
    path('', todo_list_view, name='todo-list'),
    path('create/', todo_create, name='todo-create'),
    path('update/<int:id>/', todo_update, name='todo-update'),
    path('delete/<int:id>/', todo_delete, name='todo-delete'),
    path('<int:id>/', todo_view, name='todo-detail'),
]
