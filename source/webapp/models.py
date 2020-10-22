from django.contrib.auth import get_user_model
from django.db import models


class Image(models.Model):
    image = models.ImageField(null=False, blank=False, upload_to='pics', verbose_name='Фотография')
    description = models.TextField(null=False, blank=False, max_length=2000, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1,
                               related_name='images', verbose_name='Автор')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
