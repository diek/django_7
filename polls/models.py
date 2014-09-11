import datetime

from django.db import models
from django.utils import timezone



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):      # use __str__ for Python3
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):      # use __str__ for Python3
        return self.choice_text

# >>> q = Question(question_text="What's new?", pub_date=timezone.now())

# # Save the object into the database. You have to call save() explicitly.
# >>> q.save()

# # Create three choices.
# >>> q.choice_set.create(choice_text='Not much', votes=0)
