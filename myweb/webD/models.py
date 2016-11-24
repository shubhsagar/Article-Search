from django.db import models

# Create your models here.
class Article(models.Model):
    article_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.article_name


class Word(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    word_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)

    def __str__(self):
    	return self.word_text

class Person(models.Model):
    username = models.CharField(max_length=30)
    emailID = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

