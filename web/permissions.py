from django.http import Http404


class SuperuserPermissionsMixin:
    def has_permission(self):
        return self.request.user.is_superuser

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class ManagerPermissionMixin(SuperuserPermissionsMixin):
    def has_permission(self):
        return super().has_permission() or self.request.user.type == 'manager'


class EmployeeManagerPermissionMixin(SuperuserPermissionsMixin):
    def has_permission(self):
        return super().has_permission() or self.request.user.type in ['manager', 'employee']
