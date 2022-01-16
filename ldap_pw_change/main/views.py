from django.shortcuts import render
from django.views.generic import TemplateView

import utils.ldap


class IndexView(TemplateView):
    template_name = "index.html"

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        new_password = request.POST["new_password"]
        new_password_2 = request.POST["new_password_2"]

        if new_password != new_password_2:
            return render(request, "referer.html", {"message": "Password doesn't match repeated password"})

        ret = utils.ldap.change_pw(username, password, new_password)
        if not ret:
            return render(request, "referer.html", {"message": "Password change was not successful"})
        return render(request, "referer.html", {"message": "Password changed successfully"})
