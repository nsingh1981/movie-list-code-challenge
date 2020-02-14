from django.urls import include, path, re_path
from . import views

urlpatterns = [
    re_path(r'^api/v1/movies/(?P<pk>[0-9]+)$',
               views.get_update_delete_movie.as_view(),
               name='get_update_delete_movie'
    ),
    path('api/v1/movies', views.get_post_movies.as_view(), name='get_post_movies')
]
