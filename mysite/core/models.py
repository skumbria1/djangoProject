from django.db import models
from django.core.validators import ValidationError


class CreativeTeam(models.Model):
    name = models.CharField('Название группы', max_length=255)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Творческая группа'
        verbose_name_plural = 'Творческие группы'
        ordering = ('name',)


class Play(models.Model):
    title = models.CharField('Название', max_length=255)
    premiere_date = models.DateField('Дата премьеры')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Спектакль'
        verbose_name_plural = 'Спектакли'
        ordering = ('title',)


class ActorId(models.Model):
    number = models.CharField(
        'Номер', max_length=255, unique=True, primary_key=True
    )
    photo = models.CharField('Фото', max_length=255, null=True)

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = 'ID-карта'
        verbose_name_plural = 'ID-карты'
        ordering = ('number',)


class Actor(models.Model):
    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )
    first_name = models.CharField('Имя', max_length=255)
    second_name = models.CharField('Фамилия', max_length=255)
    gender = models.CharField(
        'Пол',
        max_length=255,
        choices=GENDER_CHOICES,
        default=GENDER_CHOICES[0]
    )
    actorid = models.OneToOneField(
        ActorId,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    creativeteam = models.ForeignKey(
        CreativeTeam,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='actors'
    )
    plays = models.ManyToManyField(Play, blank=True, related_name='actors')

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

    def clean(self):
        if self.plays is None:
            raise ValidationError('Plays cannot be None')

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'
        ordering = ('actorid',)
