from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок сортировки")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['order']

    def __str__(self):
        return self.name

class PartnerOffer(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    partner_name = models.CharField(max_length=100, verbose_name="Имя партнера")
    short_description = models.TextField(verbose_name="Краткое описание (в карточке)")
    full_description = models.TextField(verbose_name="Подробное описание (в модалке)")
    link = models.URLField(verbose_name="Ссылка на сайт партнера")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name="offers", 
        verbose_name="Категория"
    )
    count = models.PositiveIntegerField(default=0, verbose_name="Количество предложений")
    image = models.ImageField(upload_to="offers/", verbose_name="Изображение")
    
    class Meta:
        verbose_name = "Партнерское предложение"
        verbose_name_plural = "Партнерские предложения"

    def __str__(self):
        return f"{self.title} ({self.count})"