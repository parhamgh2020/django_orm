from django.db import models


class Authors(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=200,
                               null=True)
    zipcode = models.IntegerField(null=True)
    telephone = models.CharField(max_length=100,
                                 null=True)
    recommendedby = models.ForeignKey('Authors',
                                      on_delete=models.CASCADE,
                                      related_name='recommended_authors',
                                      related_query_name='recommended_authors',
                                      null=True)
    joindate = models.DateField()
    popularity_score = models.IntegerField()
    followers = models.ManyToManyField('Users',
                                       related_name='followed_authors',
                                       related_query_name='followed_authors')

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Books(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=200)
    price = models.IntegerField(null=True)
    published_date = models.DateField()
    author = models.ForeignKey('Authors',
                               on_delete=models.CASCADE,
                               related_name='books',
                               related_query_name='books')
    publisher = models.ForeignKey('Publishers',
                                  on_delete=models.CASCADE,
                                  related_name='books',
                                  related_query_name='books')

    def __str__(self):
        return self.title


class Publishers(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    recommendedby = models.ForeignKey('Publishers',
                                      on_delete=models.CASCADE,
                                      null=True)
    joindate = models.DateField()
    popularity_score = models.IntegerField()

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Users(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.username