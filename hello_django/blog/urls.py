from django.urls import path

from . import views

app_name = "blog" 

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"), #conectando a url com a view postlistview
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail"), #concectando a url slug com a view postdetailview
]