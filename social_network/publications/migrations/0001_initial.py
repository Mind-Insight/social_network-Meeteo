# Generated by Django 4.2.1 on 2023-05-30 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Friend",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        upload_to="profile_photos/", verbose_name="Аватарка"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Имя друга",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Publication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, verbose_name="Заголовок")),
                ("slug", models.SlugField(unique=True, verbose_name="URL")),
                (
                    "main",
                    models.TextField(max_length=2000, verbose_name="Основной контент"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        upload_to="photos/%Y/%m/%d/",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "publication_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время публикации"
                    ),
                ),
                (
                    "likes",
                    models.PositiveSmallIntegerField(
                        default=0,
                        null=True,
                        verbose_name="Количество лайков публикации",
                    ),
                ),
                (
                    "comments_amount",
                    models.PositiveSmallIntegerField(
                        default=0, null=True, verbose_name="Количество комментариев"
                    ),
                ),
                (
                    "views",
                    models.PositiveIntegerField(
                        default=0,
                        null=True,
                        verbose_name="Количество просмотров публикации",
                    ),
                ),
                ("is_public", models.BooleanField(default=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор публикации",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        upload_to="profile_photos/", verbose_name="Аватарка"
                    ),
                ),
                (
                    "birth_day",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата Рождения"
                    ),
                ),
                (
                    "about",
                    models.TextField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Описание профиля",
                    ),
                ),
                (
                    "friend",
                    models.ManyToManyField(
                        to="publications.friend", verbose_name="Друг"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("photo", models.ImageField(upload_to="comment_avatars/")),
                (
                    "text",
                    models.TextField(max_length=500, verbose_name="Текст комментария"),
                ),
                (
                    "comment_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата комментария"
                    ),
                ),
                (
                    "likes",
                    models.PositiveSmallIntegerField(
                        default=0,
                        null=True,
                        verbose_name="Количество лайков на комментарии",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор комментария",
                    ),
                ),
                (
                    "publication",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="publications.publication",
                        verbose_name="Публикация",
                    ),
                ),
            ],
        ),
    ]
