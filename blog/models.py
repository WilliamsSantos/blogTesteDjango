from django.db import models
from django.utils import timezone


#declara a class Post com a biblioteca models.Model
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_data = models.DateTimeField(blank=True, null=True)

#Criado o metodo publish(self) aonde ele atribui um construtor timezone.now(
#dentro do campo published_date    

    def publish(self):
        self.published_date = timezone.now()
        self.save()


#retorna uma string nesse caso o proprio titulo do model Post
    def __str__(self):
        return self.title    