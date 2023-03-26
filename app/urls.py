from pprint import pprint
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import (BooksViewset,
                    AuthorsViewset,
                    PublishersViewset,
                    UsersViewset,)


urlpatterns = [
    path(f'excer{i}/', eval(f'views.excer{i}')) for i in range(1, 41)
]


router = DefaultRouter()
router.register(r'book', BooksViewset, basename="book")
router.register(r'author', AuthorsViewset, basename="author")
router.register(r'publisher', PublishersViewset, basename="publisher")
router.register(r'user', UsersViewset, basename="user")

urlpatterns += [
    path('entity/', include(router.urls)),
]
