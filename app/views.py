from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Books, Authors, Publishers, Users
import datetime
from django.db.models import Count, Avg, Sum, Max, Min
from django.db.models import Q, F
from rest_framework import viewsets
from .serializers import (AuthorsSerializer,
                          BooksSerializer,
                          PublishersSerializer,
                          UsersSerializer)


class BooksViewset(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()


class AuthorsViewset(viewsets.ModelViewSet):
    serializer_class = AuthorsSerializer
    queryset = Authors.objects.all()


class PublishersViewset(viewsets.ModelViewSet):
    serializer_class = PublishersSerializer
    queryset = Publishers.objects.all()


class UsersViewset(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()


@api_view(['GET'])
def excer1(request):
    """Write a Query using Django ORM to fetch all the books objects from your database."""
    ans1 = Books.objects.all()
    return Response(ans1)


@api_view(['GET'])
def excer2(request):
    """
    Write a Query using Django ORM to fetch title and
    published_date of all books from the database.
    """
    ans2 = Books.objects.all().values_list('title', 'published_date')
    return Response(ans2)


@api_view(['GET'])
def excer3(request):
    """
    Fetch first name and last name of all the new authors
    ( Authors with popularity_score = 0 are new authors ).
    """
    ans3 = Authors.objects.all().filter(popularity_score=0).values_list('firstname',
                                                                        'lastname')
    return Response(ans3)


@api_view(['GET'])
def excer4(request):
    """
    Fetch first name and popularity score of all authors whose
    first name starts with A and popularity score is greater than or equal to 8.
    """
    ans4 = Authors.objects.all().filter(firstname__startswith='a',
                                        popularity_score__gte=8)
    ans4 = ans4.values_list('firstname',
                            'popularity_score')
    return Response(ans4)


@api_view(['GET'])
def excer5(request):
    """
    Fetch first name of all the authors with aa case insensitive in their first name.
    """
    ans5 = Authors.objects.all().filter(
        firstname__icontains='aa').values_list('firstname')
    return Response(ans5)


@api_view(['GET'])
def excer6(request):
    """
    Fetch list of all the authors whose ids are in the list = [1, 3, 23, 43, 134, 25].
    """
    ans6 = Authors.objects.all().filter(pk__in=[1, 3, 23, 43, 134, 25])
    return Response(ans6)


@api_view(['GET'])
def excer7(request):
    """
    Fetch list of all the publishers who joined after or in September 2012,
    output list should only contain first name and join date of publisher. Order by join date.
    """
    ans7 = Authors.objects.all().filter(joindate__gte=datetime.date(year=2012,
                                                                    month=9,
                                                                    day=1))
    ans7 = ans7.order_by('joindate').values_list('firstname', 'joindate')
    return Response(ans7)


@api_view(['GET'])
def excer8(request):
    """
    Fetch ordered list of first 10 last names of Publishers, list must not contain duplicates.
    """
    ans8 = Publishers.objects.all().order_by(
        'lastname').values_list('lastname').distinct()[:10]
    return Response(ans8)


@api_view(['GET'])
def excer9(request):
    """
    Get the signup date for the last joined Author and Publisher.
    """
    ans9 = [Authors.objects.all().order_by('joindate').last(),
            Publishers.objects.all().order_by('-joindate').first()]
    return Response(ans9)


@api_view(['GET'])
def excer10(request):
    """
    Get the first name, last name and join date of the last author who joined.
    """
    ans10 = Authors.objects.all().order_by('-joindate').values_list(
        'firstname',
        'lastname',
        'joindate').first()
    return Response(ans10)


@api_view(['GET'])
def excer11(request):
    """
    Fetch list of all authors who joined after or in year 2013
    """
    ans11 = Authors.objects.all().filter(joindate__year__gte=2013)
    return Response(ans11)


@api_view(['GET'])
def excer12(request):
    """
    Fetch total price of all the books written by authors with popularity score 7 or higher.
    """
    ans12 = Books.objects.all().filter(
        author__popularity_score__gte=7).aggregate(total_book_price=Sum('price'))
    return Response(ans12)


@api_view(['GET'])
def excer13(request):
    """
    Fetch list of titles of all books written by authors whose first name starts with ‘A’.
    The result should contain a list of the titles of every book. Not a list of tuples.
    """
    ans13 = Books.objects.all().filter(
        author__firstname__contains='a').values_list('title', flat=True)
    return Response(ans13)


@api_view(['GET'])
def excer14(request):
    """
    Get total price of all the books written by author with pk in list [1, 3, 4]
    """
    ans14 = Books.objects.all().filter(
        author__pk__in=[1, 3, 4]).aggregate('price')
    return Response(ans14)


@api_view(['GET'])
def excer15(request):
    """
    Produce a list of all the authors along with their recommender.
    """
    ans15 = Authors.objects.all().values_list(
        'firstname', 'recommendedby__firstname')
    return Response(ans15)


@api_view(['GET'])
def excer16(request):
    """
    Produce list of all authors who published their book by publisher pk = 1, output list should be ordered by first name.
    """
    ans16 = Authors.objects.all().filter(books__publisher__pk=1)
    return Response(ans16)


@api_view(['GET'])
def excer17(request):
    """
    Create three new users and add in the followers of the author with pk = 1.
    """
    user1 = Users.objects.create(username='user1', email='user1@test.com')
    user2 = Users.objects.create(username='user2', email='user2@test.com')
    user3 = Users.objects.create(username='user3', email='user3@test.com')
    ans17 = Authors.objects.get(pk=1).followers.add(user1, user2, user3)
    return Response(ans17)


@api_view(['GET'])
def excer18(request):
    """
    Set the followers list of the author with pk = 2, with only one user.
    """
    ans18 = Authors.objects.get(pk=2).followers.set(user1)
    return Response(ans18)


@api_view(['GET'])
def excer19(request):
    """
    Add new users in followers of the author with pk = 1.
    """
    ans19 = Authors.objects.get(pk=1).followers.add(user1)
    return Response(ans19)


@api_view(['GET'])
def excer20(request):
    """
    Remove one user from the followers of the author with pk = 1.
    """
    ans20 = Authors.objects.get(pk=1).followers.remove(user1)
    return Response(ans20)


@api_view(['GET'])
def excer21(request):
    """
    Get first names of all the authors, whose user with pk = 1 is following. ( Without Accessing Author.objects manager )
    """
    ans21 = Users.objects.get(pk=1).followed_authors.all(
    ).values_list('firstname', flat=True)
    return Response(ans21)


@api_view(['GET'])
def excer22(request):
    """
    Fetch list of all authors who wrote a book with “tle” as part of Book Title.
    """
    ans22 = Authors.objects.all().filter(books__title__icontains='tle')
    return Response(ans22)


@api_view(['GET'])
def excer23(request):
    """
    Fetch the list of authors whose names start with ‘A’ case insensitive, 
    and either their popularity score is greater than 5 or they have joined after 2014.
    with Q objects.
    """
    ans23 = Authors.objects.all().filter(Q(firstname__istartswith='a') and (
        Q(popularity_score__gt=5) or Q(joindate__year__gt=2014)))
    return Response(ans23)


@api_view(['GET'])
def excer24(request):
    """
    Retrieve a specific object with primary key= 1 from the Author table.
    """
    ans24 = Authors.objects.all().get(pk=1)


@api_view(['GET'])
def excer25(request):
    """
    Retrieve the first N=10 records from an Author table.
    """
    ans25 = Authors.objects.all()[:10]


@api_view(['GET'])
def excer26(request):
    """
    Retrieve records from a table that match this condition, 
    popularity score = 7. And get the first and last record of that list.
    """
    qs = Authors.objects.all().filter(popularity_scre=7)
    author1 = qs.first()
    author2 = qs.last()
    ans26 = [author1, author2]


@api_view(['GET'])
def excer27(request):
    """
    Retrieve all authors who joined after or in the year 2012, 
    popularity score greater than or equal to 4, join date after or with date 12, 
    and first name starts with ‘a’ (case insensitive) without using Q objects.
    """
    ans27 = Authors.objects.all().filter(joindate__year__gte=2012,
                                         popularity_score__gte=4, joindate__day__gte=12, firstame__istartswith='a')


@api_view(['GET'])
def excer28(request):
    """
    Retrieve all authors who did not join in 2012.
    """
    ans28 = Authors.objects.all().exclude(joindate__year=2012)


@api_view(['GET'])
def excer29(request):
    """
    Retrieve Oldest author, Newest author, Average popularity score of authors, 
    sum of price of all books in database.
    """
    oldest_author = Authors.objects.all().aggregate(Min('joindate'))
    newest_author = Authors.objects.all().aggregate(Max('joindate'))
    avg_pop_score = Authors.objects.all().aggregate(Avg('popularity_score'))
    sum_price = Books.objects.all().aggregate(Sum('price'))
    ans29 = [oldest_author, newest_author, avg_pop_score, sum_price]


@api_view(['GET'])
def excer30(request):
    """
    Retrieve all authors who have no recommender, recommended by field is null.
    """
    ans30 = Authors.objects.all().filter(recommendedby__isnull=True)


@api_view(['GET'])
def excer31(request):
    """
    Retrieve the books that do not have any authors, where the author is null. Also, 
    retrieve the books whose authors are present, but do not have a recommender, 
    where the author is not null and the author’s recommender is null. 
    (Note that if the condition for the author not being null is not specified and
    only the condition for the recommender being null is mentioned, 
    all books with both author null and author’s recommender null will be retrieved.)
    """
    one = Books.objects.all().filter(author__isnull=False)
    two = Books.objects.all().filter(author__isnull=False,
                                     author__recommender__isnull=True)
    ans31 = [one, two]


@api_view(['GET'])
def excer32(request):
    """
    Total price of books written by author with primary key = 1.
    ( Aggregation over related model ), oldest book written by author with pk = 1, 
    latest book written by author with pk = 1.
    """
    ans32 = Books.objects.all().filter(author__pk=1).aggregate(Sum('price'))


@api_view(['GET'])
def excer33(request):
    """
    Among the publishers in the Publishers table 
    what is the oldest book any publisher has published.
    """
    ans33 = Books.objects.all().order_by('published_date').last().title


@api_view(['GET'])
def excer34(request):
    """
    Average price of all the books in the database.
    """
    ans34 = Books.objects.all().aggregate(Avg('price'))


@api_view(['GET'])
def excer35(request):
    """
    Maximum popularity score of publisher among all the publishers 
    who published a book for the author with pk = 1. (Reverse Foreign Key hop)
    """
    ans35 = Publishers.objects.filter(
        books__author__pk=1).aggregate(Max('popularity_score'))


@api_view(['GET'])
def excer36(request):
    """
    Count the number of authors who have written a book 
    which contains the phrase ‘ab’ case insensitive.
    """
    ans36 = Authors.objects.filter(books__title__icontains='ab').count()


@api_view(['GET'])
def excer37(request):
    """
    Get all the authors with followers more than 216.
    """
    ans37 = Authors.objects.annotate(
        f_count=Count('followers')).filter(f_count__gt=216)


@api_view(['GET'])
def excer38(request):
    """
    Get average popularity score of all the authors who joined after 20 September 2014.
    """
    ans38 = Authors.objects.filter(joindate__gt=datetime.date(
        year=2014, month=9, day=20)).aggregate(Avg('popularity_score'))


@api_view(['GET'])
def excer39(request):
    """
    Generate a list of books whose author has written more than 10 books.
    """
    ans39 = Books.objects.all().annotate(bk_count=Count(
        'author__books')).filter(bk_count__gt=10).distinct()


@api_view(['GET'])
def excer40(request):
    """
    Get the list of books with duplicate titles.
    """
    ans40 = Books.objects.all().annotate(
        count_title=Count('title')).filter(count_title__gt=1)
