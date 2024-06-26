from django.urls import path
from .views import (
    IndexView,
    YearView,
    post_detail,
    TemplIf,
    TemplFor,
    AuthorPostsView,
    PostFullView,
)

urlpatterns = [
    path("if/", TemplIf.as_view(), name="if"),
    path("for/", TemplFor.as_view(), name="if"),
    path("y/<int:year>/", YearView.as_view(), name="yearview"),
    path("posts/<int:year>/<int:month>/<slug:slug>/", post_detail, name="post_detail"),
    path('author/<int:author_id>/', AuthorPostsView.as_view(), name='author_posts'),
    path('post/<int:post_id>/', PostFullView.as_view(), name='post_full'),
]
