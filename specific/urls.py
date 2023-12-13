
from django.urls import path

from specific.views import *

app_name='specific'

urlpatterns = [
    path('simha/', simha ,name='simha'),
    path('simha2/',simha2,name='simha2'),
]