from django.shortcuts import render

from django.views.generic.base import View


class UserView(View):
    template_name = 'screen.html'

    def get(self, request):
        return render(request, self.template_name)
