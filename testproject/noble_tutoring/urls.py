from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('courses/<int:course_id>/', views.detail, name='rooms')
]