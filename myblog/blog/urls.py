from django.urls import path
from . import views

# пустые кавычки - главная стр нашего сайта
urlpatterns = [path('', views.PostView.as_view()),
               path('<int:pk>/', views.PostDetail.as_view()),
               path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments')]
