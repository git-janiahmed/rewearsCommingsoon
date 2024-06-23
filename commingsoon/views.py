from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

from .models import AwaitingUser

# Create your views here.


class CommingSoonRegister(CreateView):
    model = AwaitingUser
    template_name = "commingsoon/index.html"
    fields = ["email"]

    success_url = reverse_lazy("commingSucess")


class CommingSoonSucess(TemplateView):
    template_name = "commingsoon/thankyou.html"
