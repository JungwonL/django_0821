from django.urls import path, re_path
from create.views import *

app_name = 'create'

urlpatterns = [
    path('', CreatePost.as_view()),
]