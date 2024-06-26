# Generated by Django 5.0.6 on 2024-06-04 21:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(auto_now=True, verbose_name='дата оплаты')),
                ('payment_amount', models.PositiveIntegerField(verbose_name='сумма платежа')),
                ('payment_method', models.CharField(choices=[('Наличные', 'Наличные'), ('Карта', 'Карта')], default='Наличные', verbose_name='способ оплаты')),
                ('paid_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.course', verbose_name='оплаченный курс')),
                ('paid_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.lesson', verbose_name='оплаченный урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'платеж',
                'verbose_name_plural': 'платежи',
                'ordering': ['-payment_date'],
            },
        ),
    ]
