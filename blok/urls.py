
from django.urls import path

from . import views

app_name = 'blok'
urlpatterns = [
                  path('', views.index),
                  path('about/', views.about),
                  path('<int:sportnews_id>', views.detail, name='detail'),
                  path('<int:sportnews_id>/l_comment', views.l_comment, name='l_comment')]
