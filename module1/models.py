from django.db import models
# Create your models here.
# 数据表和字段名

# python manage.py module1
# python manage.py makemigrations module1
# python manage.py migrate  module1
# 这里将创建表module1_test
# 并且创建了两个字段：id和name
class Test(models.Model):
    name=models.CharField(max_length=20)