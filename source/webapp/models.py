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


class FavoriteImage(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name='favorite_image', verbose_name='Пользователь')
    image = models.ForeignKey('webapp.Image', on_delete=models.CASCADE,
                              related_name='favorites', verbose_name='Фотография')

    def __str__(self):
        return f'{self.user.username} - {self.image.description}'

    class Meta:
        verbose_name = 'Избранное'


class ImageComment(models.Model):
    text = models.TextField(null=False, blank=False, max_length=400, verbose_name='Текст')
    image = models.ForeignKey('webapp.Image', null=False, blank=False,
                              on_delete=models.CASCADE, verbose_name='Фотография', related_name='comments')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1,
                               related_name='comments', verbose_name='Автор')

    def __str__(self):
        return self.text[:20]