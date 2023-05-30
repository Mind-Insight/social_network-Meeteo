from django.db import models
from django.contrib.auth.models import User


class Publication(models.Model):
    title = models.CharField(
        "Заголовок",
        max_length=50,
    )
    main = models.TextField(
        "Основной контент",
        max_length=2000,
    )
    image = models.ImageField(
        "Изображение",
        upload_to="photos/%Y/%m/%d/",
        blank=True,
    )
    publication_date = models.DateTimeField(
        "Дата и время публикации",
        auto_now_add=True,
    )
    likes = models.PositiveSmallIntegerField(
        "Количество лайков публикации",
        null=True,
        default=0,
    )
    comments_amount = models.PositiveSmallIntegerField(
        "Количество комментариев",
        null=True,
        default=0,
    )
    views = models.PositiveIntegerField(
        "Количество просмотров публикации",
        null=True,
        default=0,
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name="Автор публикации",
    )
    is_public = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name="Автор комментария",
    )
    photo = models.ImageField(
        upload_to="comment_avatars/",
    )
    text = models.TextField(
        "Текст комментария",
        max_length=500,
    )
    comment_date = models.DateTimeField(
        "Дата комментария",
        auto_now_add=True,
    )
    likes = models.PositiveSmallIntegerField(
        "Количество лайков на комментарии",
        null=True,
        default=0,
    )
    publication = models.ForeignKey(
        "Publication",
        on_delete=models.CASCADE,
        verbose_name="Публикация",
    )

    def __str__(self):
        return f"Комментарий {self.author}"


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    photo = models.ImageField(
        "Аватарка",
        upload_to="profile_photos/",
    )
    birth_day = models.DateField(
        "Дата Рождения",
        null=True,
        blank=True,
    )
    about = models.TextField(
        "Описание профиля",
        max_length=200,
        null=True,
        blank=True,
    )
    friend = models.ManyToManyField(
        "Friend",
        verbose_name="Друг",
    )


class Friend(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Имя друга",
    )
    photo = models.ImageField(
        "Аватарка",
        upload_to="profile_photos/",
    )

    def __str__(self):
        return self.user
