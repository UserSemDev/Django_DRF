from django.db import models

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    """ Модель курса"""
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='course/image/', default='course/image/default_course.jpg', **NULLABLE,
                                verbose_name='Превью')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """Модель урока"""
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='lesson/image/', default='lesson/image/default_lesson.jpg', **NULLABLE,
                                verbose_name='Превью')
    url = models.CharField(max_length=350, **NULLABLE, verbose_name='Ссылка на видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
