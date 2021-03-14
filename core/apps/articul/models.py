# apps/articul/models
from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
from apps.user.models import User


class Articul(models.Model):
    """Кажому объекту присуждается уникальный артикул """
    id = models.IntegerField('ID', primary_key=True)
    userartikul = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="Пользователь",
                                    help_text='Укажите владельца артикула')
    artikuls = models.CharField('Артикул', max_length=64, blank=True)
    nomer = models.CharField('Номер', max_length=64, null=True)
    status = models.CharField('Статус', max_length=3, default='000')
    kod_phone = models.CharField('Телефонный код', max_length=5, default=86191, help_text='Код стационарного'
                                 'номера телефона населенного пункта, 5 цифр.')
    data_vidan = models.DateTimeField('Дата выдачи', blank=True, null=True)
    slug = models.SlugField('Ссылка', null=True)
    is_oplata = models.BooleanField('Оплачено', default=False)
    zametki = models.TextField('Для заметок', max_length=2000, blank=True)
    # tags = TaggableManager('Теги', blank=True, )

    def nomernew(self):
        nomer = []
        for x in str(self.id):
            nomer.append(x)

        while nomer:
            if len(nomer) < 6:
                nomer.insert(0, '0')
            if len(nomer) == 6:
                nomer = ''.join(nomer)
                break
        return '%s' % nomer

    def __str__(self):
        return self.artikuls

    def save(self, *args, **kwargs):
        self.nomer = Articul.nomernew(self)
        self.artikuls = '%s%s%s' % (self.kod_phone, self.status, self.nomer)
        self.slug = self.artikuls
        if self.is_oplata:
            self.status = '001'

        super(Articul, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Артикул'
        verbose_name_plural = 'Артикулы'
        ordering = ["-artikuls"]

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('people.views.details', args=[str(self.id)])



