from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
    	return self.choice_text

class Article(models.Model):
	Name = models.CharField(max_length=1000)
	Link = models.CharField(max_length=1000)

	def __str__(self):
		return self.Name
