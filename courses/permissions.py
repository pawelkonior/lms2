from django.contrib.auth.mixins import AccessMixin


class AuthorManageMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        course = self.get_queryset().filter(pk=kwargs.get('pk'))
        if not len(course) or request.user != course.first().owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
