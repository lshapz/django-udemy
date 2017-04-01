from django.db import models


class Post(models.Model):
  title = models.CharField(max_length=250)
  pub_date = models.DateTimeField()
  image = models.ImageField(upload_to='media/')
  body = models.TextField()

  def __str__(self):
    return self.title

  def pretty_pub_date(self):
    return self.pub_date.strftime('%B %d %Y')

  def summary(self):
    return self.body[:100]
# Create your models here.
