from django.conf.urls import url
from .views import new_post, PostListView, new_comment, like, share

urlpatterns = [
	url(r'^$', PostListView.as_view(), name="forum"),
	url(r'^new-post$', new_post, name="create-post"),
	url(r'^new-comment$', new_comment, name="add-comment"),
	url(r'^like$', like, name='like'),
	url(r'^share$', share, name='share'),
]

