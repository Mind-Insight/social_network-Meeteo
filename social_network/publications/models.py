from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Publication(models.Model):
    title = models.CharField(
        "Заголовок",
        max_length=256,
        blank=False,
    )
    description = models.TextField(
        "Описание",
        blank=True,
    )
    publication_date = models.DateTimeField(
        "Дата и время публикации",
        auto_now_add=True,
        blank=False,
    )
    likes = models.PositiveSmallIntegerField(
        "Количество лайков публикации",
        null=True,
        blank=False,
        default=0,
    )
    comments_amount = models.PositiveSmallIntegerField(
        "Количество комментариев",
        null=True,
        blank=False,
        default=0,
    )
    views = models.PositiveIntegerField(
        "Количество просмотров публикации",
        null=True,
        blank=False,
        default=0,
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name="Автор публикации",
    )
    comments = models.OneToOneField(
        to="Comment",
        on_delete=models.CASCADE,
        blank=False,
        verbose_name="Комментарии",
    )


class Comment(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING,
        blank=False,
        verbose_name="Автор комментария",
    )
    text = models.TextField(
        "Текст комментария",
        max_length=500,
        blank=False,
    )
    comment_date = models.DateTimeField(
        "Дата комментария",
        auto_now_add=True,
        blank=False,
    )
    likes = models.PositiveSmallIntegerField(
        "Количество лайков на комментарии",
        null=True,
        blank=False,
        default=0,
    )
