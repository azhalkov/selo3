# apps/dom/models
from django.db import models
from transliterate import slugify

from apps.articul.models import Articul


class Map(models.Model):
    """ Точка на карте Google """
    pass


class Adres(models.Model):
    """ Адрес объекта недвижимости"""
    art = models.ForeignKey(Articul, null=True, on_delete=models.SET_NULL, related_name='adress')
    vid = models.CharField("Статус", max_length=54, default='Продаю дом')
    krai = models.CharField("Край, область", max_length=54, default='Краснодарский край,')
    gorod = models.CharField("Населенный пункт", max_length=54, default='Павловская,')
    raion = models.CharField("Район", max_length=54, default='Павловский район,')
    mikroraion = models.CharField("Микрорайон", max_length=54, default='нет')
    ulica = models.CharField("Улица", max_length=54, default='Не указано,')
    nomer_doma = models.CharField("Номер дома", max_length=5, default='0')
    nomer_podezda = models.CharField("Номер подъезда", max_length=4, default='нет')
    nomer_kvartiri = models.CharField("Номер квартиры", max_length=4, default='нет,')
    is_activ = models.BooleanField('Опубликовано', default=False)
    date_pub = models.DateField('Дата публикации', null=True, blank=True)
    slug = models.SlugField('Ссылка', max_length=86, null=True, blank=True)

    def __str__(self):
        return '%s' % self.slug

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def save(self, *args, **kwargs):
        self.slug = '%s_%s_%s' % (self.vid, self.krai, self.gorod)
        self.slug = slugify(self.slug)
        super(Adres, self).save(*args, **kwargs)


class Komunikacii(models.Model):
    """Класс описания коммуникаций здания"""
    art = models.ForeignKey(Articul, null=True, on_delete=models.SET_NULL, )
    vodoprovod = models.CharField("Водопровод", max_length=54, default='Пластиковый')
    data_voda = models.DateField("Водопровод дата установки", null=True, blank=True)
    otoplenie = models.CharField("Отопление", max_length=54, default='Радиаторы,')
    data_otoplenie = models.DateField("Отопление дата установки", null=True, blank=True)
    kanalizacii = models.CharField("Канализация", max_length=54, default='Пластик,')
    data_kanalizacii = models.DateField("Канализация дата установки", null=True, blank=True)
    descreption = models.TextField('Заметки', max_length=3000, blank=True)

    def __str__(self):
        return '%s' % self.art

    class Meta:
        verbose_name = 'Комуникация'
        verbose_name_plural = 'Коммуникации'


class Dom(models.Model):
    # adres = models.ForeignKey(Adres)
      # xozjaindom = models.ForeignKey(Profile
    # menedjer = models.ForeignKey(Profile

    # god_postroiki
    # fundament
    # material_sten
    # tip_okon
    # map = models.Fo(Map)
    #
    pass


