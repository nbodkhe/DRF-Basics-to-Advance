from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductListCreateAPIView.as_view()),
    path('create/', ProductListCreateAPIView.as_view()),
    path('<int:pk>/update/', ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete/', ProductDestroyAPIView.as_view()),
]
