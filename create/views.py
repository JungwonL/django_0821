from django.shortcuts import render
from django.views.generic import CreateView
from create.models import CreatePost
from django.urls import reverse_lazy

#ListView
class CreatePost(CreateView):
    model = CreatePost
    fields = ['title', 'content']
    success_url = reverse_lazy('create:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)