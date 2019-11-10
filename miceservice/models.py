from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class PassengerTraffic(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(verbose_name=_('Год'))
    traffic = models.FloatField(verbose_name=_('Траффик'))

    class Meta:
        verbose_name = _('Статистика пассажирский траффик')
        verbose_name_plural = _('Статистики пассажирского траффика')

    def __str__(self):
        return f'Год: {self.year} - Траффик: {self.traffic}'


class AttractionType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name=_('Наименование'))

    class Meta:
        verbose_name = _('Вид достопримечательности')
        verbose_name_plural = _('Виды достопримечательностей')

    def __str__(self):
        return self.name


class District(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name=_('Название'))

    class Meta:
        verbose_name = _('Район')
        verbose_name_plural = _('Районы')

    def __str__(self):
        return self.name


class Attraction(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name=_('Название'))
    type = models.ForeignKey(AttractionType, on_delete=models.CASCADE, verbose_name=_('Вид достопримечательности'))
    description = models.TextField(blank=True, verbose_name=_('Описание'))
    address = models.CharField(max_length=100, verbose_name=_('Адрес'))
    operating_mode = models.CharField(blank=True, max_length=200, verbose_name=_('Режим работы'))
    ticket_price = models.CharField(blank=True, max_length=100, verbose_name=_('Цена билета'))
    phone_number = models.CharField(blank=True, max_length=100, verbose_name=_('Номер телефона'))
    site = models.URLField(blank=True, verbose_name=_('Ссылка на сайт'))
    email = models.EmailField(blank=True, verbose_name=_('Почта'))
    insta = models.URLField(blank=True, verbose_name=_('Instagram'))
    fb = models.URLField(blank=True, verbose_name=_('Facebook'))
    vk = models.URLField(blank=True, verbose_name=_('ВК'))

    class Meta:
        verbose_name = _('Достопримечательность')
        verbose_name_plural = _('Достопримечательности')

    def __str__(self):
        return f'{self.type} {self.name}'


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.CharField(max_length=100, verbose_name=_('Дата'))
    name = models.TextField(verbose_name=_('Наименование'))
    place = models.CharField(max_length=300, verbose_name=_('Место'))

    class Meta:
        verbose_name = _('Мероприятие')
        verbose_name_plural = _('Мероприятия')

    def __str__(self):
        return self.name


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name=_('Название'))
    address = models.CharField(max_length=200, verbose_name=_('Адрес'))
    phone_number = models.CharField(max_length=12, verbose_name=_('Номер телефона'))
    number_of_rooms = models.IntegerField(verbose_name=_('Число комнат'))
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name=_('Район'))

    class Meta:
        verbose_name = _('Отель')
        verbose_name_plural = _('Отели')

    def __str__(self):
        return self.name


class Monument(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name=_('Название'))
    address = models.CharField(max_length=200, verbose_name=_('Адрес'))
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name=_('Район'))

    class Meta:
        verbose_name = _('Монумент')
        verbose_name_plural = _('Монументы')

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name=_('Название'))
    address = models.CharField(max_length=200, verbose_name=_('Адрес'))
    contacts = models.CharField(max_length=200, verbose_name=_('Контакты'))
    site = models.URLField(verbose_name=_('Ссылка на сайт'))
    operating_mode = models.CharField(max_length=200, verbose_name=_('Режим работы'))
    type_of_cuisine = models.CharField(max_length=200, verbose_name=_('Кухня'))
    number_of_seats = models.IntegerField(verbose_name=_('Число мест'))

    class Meta:
        verbose_name = _('Ресторан')
        verbose_name_plural = _('Рестораны')

    def __str__(self):
        return self.name


class TourismStatistic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, verbose_name=_('Наименование'))
    year = models.IntegerField(verbose_name=_('Год'))
    quantity = models.FloatField(verbose_name=_('Объем'))

    class Meta:
        verbose_name = _('Статистика туризма')
        verbose_name_plural = _('Статистики туризма')

    def __str__(self):
        return f'{self.name} {self.year} {self.quantity}'
