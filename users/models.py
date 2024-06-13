from django.contrib.auth.models import AbstractUser
from django.db import models
from materials.models import Course, Lesson
from django.utils.translation import gettext as _

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """Модель пользователя"""
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name='Телефон')
    city = models.CharField(max_length=100, **NULLABLE, verbose_name='Город')
    avatar = models.ImageField(upload_to='users/avatars/', default='users/avatars/no_avatar.png', **NULLABLE,
                               verbose_name='Аватар')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Payments(models.Model):
    """Модель платежей"""
    class PaymentMethodChoices(models.TextChoices):
        CASH = "Наличные", _("Наличные")
        CARD = "Карта", _("Карта")

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    payment_date = models.DateTimeField(auto_now=True, verbose_name='дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='оплаченный урок')
    payment_amount = models.PositiveIntegerField(verbose_name='сумма платежа')
    payment_method = models.CharField(default=PaymentMethodChoices.CASH, choices=PaymentMethodChoices,
                                      verbose_name='способ оплаты')

    def __str__(self):
        return (f"{self.user} | {self.payment_date} | {self.payment_amount} | {self.payment_method} | "
                f"{self.paid_course if self.paid_course else self.paid_lesson}")

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
        ordering = ['-payment_date', ]


class Subscription(models.Model):
    """Модель подписки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="курс")

    def __str__(self):
        return f"{self.user} | {self.course}"

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
