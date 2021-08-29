from django.db import models



class Sportnews(models.Model):
    title = models.CharField(max_length=50, verbose_name='наименование')
    content = models.TextField(blank=True, verbose_name='описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата публкации')
    photo = models.ImageField(upload_to='photos/%y/%m/%d', verbose_name='фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering = ['-created_at']


class Comment(models.Model):
    post = models.ForeignKey(Sportnews, on_delete=models.CASCADE)
    user = models.CharField(max_length=20, verbose_name='автор')
    comments = models.TextField(blank=True, verbose_name='коментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата публкации')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
