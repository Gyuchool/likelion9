from django.db import models

class Blog(models.Model): #models class 내의 method사용, id column auto create
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField() #글자 제한 없음

    def __str__(self):
        return self.title

