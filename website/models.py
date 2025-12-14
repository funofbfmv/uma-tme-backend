from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField("Название сайта/компании", max_length=255, default="Наша компания")
    logo = models.ImageField("Логотип", upload_to="logos/", blank=True, null=True)

    hero_title = models.CharField("Заголовок на главной", max_length=255, blank=True)
    hero_subtitle = models.TextField("Подзаголовок на главной", blank=True)

    phone = models.CharField("Телефон", max_length=50, blank=True)
    email = models.EmailField("Email", blank=True)
    address = models.CharField("Адрес", max_length=255, blank=True)

    whatsapp_link = models.URLField("Ссылка на WhatsApp", blank=True)
    telegram_link = models.URLField("Ссылка на Telegram", blank=True)

    footer_text = models.TextField("Текст в подвале", blank=True)

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self):
        return "Глобальные настройки"


class ServiceCategory(models.Model):
    title = models.CharField("Название категории", max_length=255)
    slug = models.SlugField("Слаг", unique=True)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Категория услуги"
        verbose_name_plural = "Категории услуг"

    def __str__(self):
        return self.title


class Service(models.Model):
    category = models.ForeignKey(
        ServiceCategory,
        related_name="services",
        on_delete=models.CASCADE,
        verbose_name="Категория",
    )
    title = models.CharField("Название услуги", max_length=255)
    short_description = models.TextField("Краткое описание", blank=True)
    full_description = models.TextField("Полное описание", blank=True)
    icon = models.ImageField("Иконка", upload_to="service_icons/", blank=True, null=True)
    is_featured = models.BooleanField("Показывать на главной", default=True)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title


class Lead(models.Model):
    name = models.CharField("Имя", max_length=255)
    phone = models.CharField("Телефон", max_length=50)
    email = models.EmailField("Email", blank=True)
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Интересующая услуга",
        related_name="leads",
    )
    message = models.TextField("Комментарий", blank=True)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    is_processed = models.BooleanField("Обработано", default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"{self.name} ({self.phone})"
