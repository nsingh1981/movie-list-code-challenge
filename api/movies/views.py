from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Movie
from .serializers import MovieSerializer


class get_update_delete_movie(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return
        return movie

    # retrieve a movie
    def get(self, request, pk):
        movie = self.get_queryset(pk)
        if movie:
            serializer = MovieSerializer(movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
        content = {
            'status': 'Not Found'
        }
        return Response(content, status=status.HTTP_404_NOT_FOUND)


    # update a movie
    def put(self, request, pk):
        movie = self.get_queryset(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # delete a movie
    def delete(self, request, pk):
        movie = self.get_queryset(pk)
        movie.delete()
        content = {
            'status': 'NO CONTENT'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)


class get_post_movies(ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        movies = Movie.objects.all()
        return movies

    # get all movies
    def get(self, request):
        movies = self.get_queryset()
        serializer = self.serializer_class(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # create a new movie
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





