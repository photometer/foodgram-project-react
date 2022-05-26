from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    password = models.CharField(
        'Пароль',
        max_length=150,
        validators=[RegexValidator(
            regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])\
                  [A-Za-z\d@$!%*#?&]{8,}',
            message=[
                'Пароль может содержать только латинские буквы, цифры и '
                'спецсимволы (@$!%*#?&), от 8 до 150 знаков. Должна '
                'присутствовать хотя бы 1 строчная и 1 заглавная буквы, '
                '1 цифра и 1 спецсимволов.'
            ]
        )]
    )
    first_name = models.CharField('Имя', max_length=150)
    last_name = models.CharField('Фамилия', max_length=150)
    followers = models.ManyToManyField(
        to='self',
        symmetrical=False,
        verbose_name='Подписчики',
        blank=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
