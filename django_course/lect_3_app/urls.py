from django.urls import path
from .views import IndexView, YearView, post_detail

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('y/<int:year>/', YearView.as_view(), name='yearview'),
    path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
]
