from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import (BooksViewset,
                    AuthorsViewset,
                    PublishersViewset,
                    UsersViewset,)


urlpatterns = [
    path(eval(f'excer{i}'), eval(f'views.excer{i}')) for i in range(1, 41)
]


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', BooksViewset.as_view(), basename="book")
router.register(r'snippets', AuthorsViewset.as_view(), basename="author")
router.register(r'snippets', PublishersViewset.as_view(), basename="publisher")
router.register(r'snippets', UsersViewset.as_view(), basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns += [
    path('', include(router.urls)),
]
