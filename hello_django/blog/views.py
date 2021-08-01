from django.views.generic import DetailView, ListView #subclasses dessas duas

from .models import Post

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
