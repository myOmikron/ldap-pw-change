from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        new_password = request.POST["new_password"]
        new_password_2 = request.POST["new_password_2"]

        if new_password != new_password_2:
            return render(request, "referer.html", {"message": "Password doesn't match repeated password"})

        #TODO: Add template
        return render(request, "referer.html", {"message": "Password changed successfully"})
