from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('<int:history_pk>', views.history_edit, name='edit_history'),
]