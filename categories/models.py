from django.db import models


class CategoryType(models.Model):
    name = models.CharField(max_length=161)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=161)
    code = models.IntegerField()
    category_type = models.ForeignKey(CategoryType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
