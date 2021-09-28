from django.db import models

# models are a database think it as a spreadsheet.
# it will contains the feild like columns
# here it's give two fields  search and created so both will be a columns and searched data will be stored.'
# Create your models here.


class Search(models.Model):
    search = models.CharField(max_length=500)  # search field
    created = models.DateTimeField(auto_now=True)

    # whenever you make this field in your model make sure you have to migrate this using
    # 1) in terminal write  python manage.py makemigrations
    # your migration done.

  # migration are used for generating database table
  # models for pullout data from database and put it to the users

    def __str__(self):
        return '{}'.format(self.search)  # for changing the bydefault serach object(1)  to searched key.

    class Meta:
        verbose_name_plural = 'Searches'