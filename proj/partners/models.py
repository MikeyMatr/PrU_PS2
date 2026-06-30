from django.db import models

class Category(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100, verbose_name="Название категории")
    order = models.PositiveIntegerField(null=True, blank=True, default=0, verbose_name="Порядок сортировки")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['order']

    def __str__(self):
        return self.name

class PartnerOffer(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200, verbose_name="Заголовок")
    partner_name = models.CharField(null=True, blank=True, max_length=100, verbose_name="Имя партнера")
    short_description = models.TextField(null=True, blank=True, verbose_name="Краткое описание (в карточке)")
    full_description = models.TextField(null=True, blank=True, verbose_name="Подробное описание (в модалке)")
    link = models.URLField(null=True, blank=True, verbose_name="Ссылка на сайт партнера")
    start_date = models.DateField(null=True, blank=True, verbose_name="Дата начала")
    end_date = models.DateField(null=True, blank=True, verbose_name="Дата окончания")
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name="offers", 
        verbose_name="Категория"
    )
    count = models.PositiveIntegerField(null=True, blank=True, default=0, verbose_name="Количество предложений")
    image = models.ImageField(null=True, blank=True, upload_to="offers/", verbose_name="Изображение")
    
    class Meta:
        verbose_name = "Партнерское предложение"
        verbose_name_plural = "Партнерские предложения"

    def __str__(self):
        return f"{self.title} ({self.count})"