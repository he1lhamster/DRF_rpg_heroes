from django.db import models


class PCharacter(models.Model):

    name = models.CharField(max_length=120)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_cast_spells = models.BooleanField(default=False)
    p_class = models.ForeignKey('PClass', on_delete=models.PROTECT, null=True)
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class PClass(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
