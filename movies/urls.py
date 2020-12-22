from django.urls import path
from . import views

urlpatterns = {
    path("", views.MovieViw.as_view())
}
