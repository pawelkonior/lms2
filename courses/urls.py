from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.CourseView.as_view(), name='course-list'),
    path('update/<int:pk>', views.CourseUpdateView.as_view(), name='course-edit'),
    path('create/', views.CourseCreateView.as_view(), name='course-create'),
]
