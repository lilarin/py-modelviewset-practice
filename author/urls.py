from django.urls import path, include

from author.views import AuthorViewSet

list_view = AuthorViewSet.as_view(
    actions={
        "get": "list",
        "post": "create"
    }
)

detail_view = AuthorViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("actors/", list_view, name="manage-list"),
    path("actors/<int:pk>/", detail_view, name="manage-detail")
]

app_name = "author"
