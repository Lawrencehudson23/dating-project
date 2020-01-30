from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    birthday = models.DateField()
    gender = models.CharField(max_length=200)
    city = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "<User: {} {}>".format(self.first_name, self.last_name)

    def __repr__(self):
       return self.__str__()




class Like(models.Model):
    likes = models.ForeignKey(User, related_name="likes", on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User, related_name="liked_by", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Match(models.Model):
    user1 = models.ForeignKey(User, related_name="match1", on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name="match2", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
