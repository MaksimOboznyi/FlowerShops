from django.db import models

class Occasion(models.Model):
    name = models.CharField('Название события', max_length=255, unique=True)
    slug = models.SlugField('Слаг', max_length=100, unique=True) #это название букета в ссылке
    
    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        
    def __str__(self):
        return self.name


class Bouquet(models.Model):
    title = models.CharField('Название букета', max_length=255)
    slug = models.SlugField('Слаг', max_length=255, unique=True)
    occasion = models.ForeignKey(
        Occasion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='bouquets',
        verbose_name='Событие',
    )
    description = models.TextField('Описание')
    composition = models.TextField('Состав букета', blank=True)
    price = models.PositiveIntegerField('Цена')
    image = models.ImageField('Изображение', upload_to='bouquets/')
    is_active = models.BooleanField('Активен', default=True)
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлен', auto_now=True)

    class Meta:
        verbose_name = 'Букет'
        verbose_name_plural = 'Букеты'
        ordering = ['price', 'title']

    def __str__(self):
        return self.title


class Order(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'Новый'
        IN_PROGRESS = 'in_progress', 'В обработке'
        DELIVERING = 'delivering', 'Доставляется'
        COMPLETED = 'completed', 'Завершён'
        CANCELED = 'canceled', 'Отменён'
    
    class DeliveryTime(models.TextChoices):
        FAST = 'fast', 'Как можно скорее'
        T10_12 = '10_12', 'с 10:00 до 12:00'
        T12_14 = '12_14', 'с 12:00 до 14:00'
        T14_16 = '14_16', 'с 14:00 до 16:00'
        T16_18 = '16_18', 'с 16:00 до 18:00'
        T18_20 = '18_20', 'с 18:00 до 20:00'

    customer_name = models.CharField('Имя клиента', max_length=150)
    phone = models.CharField('Телефон', max_length=30)
    address = models.CharField('Адрес доставки', max_length=255)
    bouquet = models.ForeignKey(
        Bouquet,
        on_delete=models.PROTECT,
        related_name='orders',
        verbose_name='Букет'
    )
    delivery_time = models.CharField(
        'Время доставки',
        max_length=20,
        choices=DeliveryTime.choices,
        default=DeliveryTime.FAST
    )
    
    status =models.CharField(
        'Статус',
        max_length=20,
        choices=Status.choices,
        default=Status.NEW
    )
    
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    
    class Meta:
        verbose_name ='Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Заказ №{self.pk} - {self.customer_name}'
    

class ConsultationRequest(models.Model):
    customer_name = models.CharField('Имя клиента', max_length=150, blank=True)
    phone = models.CharField('Телефон', max_length=30)
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    is_processed = models.BooleanField('Обработано', default=False)
    
    class Meta:
        verbose_name = 'Заявка на консультацию'
        verbose_name_plural = 'Заявки на консультации'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Консультация №{self.pk} - {self.customer_name} - {self.phone}'