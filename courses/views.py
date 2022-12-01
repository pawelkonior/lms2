from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DetailView

from . import models
from .permissions import AuthorManageMixin


class CourseView(ListView):
    template_name = 'courses/courses_list.html'
    model = models.Course
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    model = models.Course
    context_object_name = 'course'
    template_name = 'courses/course_detail.html'


class CourseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Course
    fields = ('title',)
    template_name = 'courses/course_create.html'
    login_url = reverse_lazy('users:login_view')
    success_url = reverse_lazy('courses:course-list')
    permission_required = 'courses.add_course'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CourseUpdateView(LoginRequiredMixin, AuthorManageMixin, UpdateView):
    model = models.Course
    fields = ('title',)
    template_name = 'courses/course_edit.html'
    success_url = reverse_lazy('courses:course-list')
    context_object_name = 'course'
    login_url = reverse_lazy('users:login_view')
