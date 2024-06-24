# Generated by Django 5.0.6 on 2024-06-24 23:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_course_owner_lesson_owner'),
        ('users', '0006_payments_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='materials.course', verbose_name='курс'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]