from django.db import models

# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length=30)
    emailID = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.username

class AllArticles(models.Model):
    Name = models.CharField(max_length=500)
    Link = models.CharField(max_length=500)
    def __str__(self):
        return self.Name









########################################################################
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

class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
########################################################################