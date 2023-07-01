from django.db import models

status_choices = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class Guest(models.Model):
    author_name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Имя автора записи",
                                   default="Неизвестный")
    author_email = models.EmailField(max_length=50, null=False, blank=False, verbose_name="Почта автора записи")
    text = models.TextField(max_length=2000, verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    status = models.CharField(max_length=50, null=False, blank=False, verbose_name="Статус", choices=status_choices,
                              default=status_choices[0][0])

    def __str__(self):
        return f"{self.pk} {self.author_name}"

    class Meta:
        db_table = "guests"
        verbose_name = "гость"
        verbose_name_plural = "гости"
