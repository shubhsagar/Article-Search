from django.db import models

# # Create your models here.
# class Article(models.Model):
#     article_name = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

#     def __str__(self):
#         return self.article_name


# class Word(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     word_text = models.CharField(max_length=200)
#     #votes = models.IntegerField(default=0)

#     def __str__(self):
#     	return self.word_text

class Student(models.Model):
    Username = models.CharField(max_length=30)
    EmailID = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    def __str__(self):
        return self.Username

class Articles(models.Model):
    Name = models.CharField(max_length=1000)
    Link = models.CharField(max_length=1000)

    def __str__(self):
        return self.Name
