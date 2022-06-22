from django.db import models


def upload_location(instance, filename):
    return f'{instance.id}, {filename}'


class Articles(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              height_field='height_field',
                              width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    post = models.TextField()
    user = models.ForeignKey('auth.User',
                             on_delete=models.CASCADE,
                             # settings.AUTH_PASSWORD_VALIDATORS,
                             blank=True,
                             null=True
                             )
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return f'/news/detail/{self.id}'

    def __str__(self):
        return self.title
