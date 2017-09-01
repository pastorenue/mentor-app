from django.conf.urls import url
from .views import new_post, PostListView, new_comment

urlpatterns = [
	url(r'^$', PostListView.as_view(), name="forum"),
	url(r'^new-post$', new_post, name="create-post"),
	url(r'^new-comment$', new_comment, name="add-comment"),
]

