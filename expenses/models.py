from __future__ import unicode_literals
from django.db import models

class Expenses(models.Model):
  item = models.CharField(max_length=120)
  cost = models.CharField(max_length=120)
  date = models.DateTimeField(auto_now=True, auto_now_add=False)
  description = models.CharField(max_length=120)
  deleted = models.CharField(max_length=120)

  def __unicode__(self):
    return self.item

  def __str__(self):
    return self.item

  def get_absolute_url(self):
    return "/expenses/list/%s" % (self.id)

  def get_absolute_url_delete(self):
    return "/expenses/delete/%s" % (self.id)
