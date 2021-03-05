from django.http import Http404
from django.views import View
from django.core.exceptions import PermissionDenied

class MyView(View):
    def index(self):
        raise Http404

class MyView(View):
    def index(self):
        if not self.request.user.is_authenticated:
            raise PermissionDenied
