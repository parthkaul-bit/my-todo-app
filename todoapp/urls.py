from django.urls import path,include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('todoitems', ToDoItemViewSet)


urlpatterns = [
    path('', include(router.urls)),

    # path('', ListToDoItems.as_view()),
    # path('create/', CreateToDoItem.as_view()),
    # path('<int:pk>/', RetrieveToDoItem.as_view()),
    # path('<int:pk>/update/', UpdateToDoItem.as_view()),
    # path('<int:pk>/delete/', DeleteToDoItem.as_view()),
]