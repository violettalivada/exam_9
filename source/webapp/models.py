from django.db import models


class Image(models.Model):
    image = models.ImageField(null=False, blank=False, upload_to='pics', verbose_name='Фотография')
    description = models.TextField(null=False, blank=False, max_length=2000, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.CharField(null=False, blank=False, max_length=50, verbose_name='Автор')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
