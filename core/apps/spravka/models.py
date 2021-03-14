# apps/spravka/models
from django.db import models
# from transliterate import slugify
from taggit.managers import TaggableManager

from apps.articul.models import Articul
from apps.dom.models import Adres


class Kontakt(models.Model):
    name_firm = models.CharField("Название фирмы", max_length=128, default='Бренд')
    name_uslug = models.CharField("Название", max_length=128, default='Введите название и вид услуг')
    phone1 = models.CharField("Телефон", max_length=128, default='Введите номер телефона')
    phone_video = models.CharField("Видеосвязь", max_length=128, default='Введите номер телефона для видеосвязи')
    app_video = models.CharField("Приложение для видео связи", max_length=128, default='whatsapp')
    descrip = models.TextField("Заметки", max_length=2000, default='Заметок еще нет')

    def __str__(self):
        return '%s' % self.name_uslug

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Phonespravka(models.Model):
    template = 'spravka.html'
    kontakti = models.ForeignKey(Kontakt, null=True, on_delete=models.SET_NULL,)
    art = models.ForeignKey(Articul, null=True, on_delete=models.SET_NULL,)
    mesto = models.CharField("Населенный пункт", max_length=54,
                             default='Введите название населенного пункта')
    adres = models.ForeignKey(Adres, null=True, on_delete=models.SET_NULL,)
    tags = TaggableManager('Теги', blank=True)
    # slug = models.SlugField('Ссылка', max_length=86, null=True, blank=True)

# class Adres(models.Model):
#     """ Адрес объекта недвижимости"""
#     art = models.ForeignKey(Articul, null=True, on_delete=models.SET_NULL, )
#     vid = models.CharField("Статус", max_length=54, default='Продаю дом')
#     krai = models.CharField("Край, область", max_length=54, default='Краснодарский край,')
#     gorod = models.CharField("Населенный пункт", max_length=54, default='Павловская,')
#     raion = models.CharField("Район", max_length=54, default='Павловский район,')
#     mikroraion = models.CharField("Микрорайон", max_length=54, default='нет')
#     ulica = models.CharField("Улица", max_length=54, default='Не указано,')
#     nomer_doma = models.CharField("Номер дома", max_length=5, default='0')
#     nomer_podezda = models.CharField("Номер подъезда", max_length=4, default='нет')
#     nomer_kvartiri = models.CharField("Номер квартиры", max_length=4, default='нет,')
#     is_activ = models.BooleanField('Опубликовано', default=False)
#     date_pub = models.DateField('Дата публикации', null=True, blank=True)
#     slug = models.SlugField('Ссылка', max_length=86, null=True, blank=True)

    def __str__(self):
        return '%s' % self.mesto

    class Meta:
        verbose_name = 'Справка'
        verbose_name_plural = 'Справки'
