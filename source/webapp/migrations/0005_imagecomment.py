# Generated by Django 2.2 on 2020-10-22 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_favoriteimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=400, verbose_name='Текст')),
                ('author', models.CharField(max_length=50, verbose_name='Автор')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='webapp.Image', verbose_name='Фотография')),
            ],
        ),
    ]
