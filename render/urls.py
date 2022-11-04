from django.urls import path
from . import views

urlpatterns = [
     path("", views.Arithmetic.as_view(), name="operationans")
 ]