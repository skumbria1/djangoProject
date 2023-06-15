from django import forms
from core.field_validators import ONLY_LETTERS_VALIDATOR
from core import models


GENDER_CHOICES = (
    (None, 'Не выбрано'),
    ('M', 'Мужской'),
    ('F', 'Женский'),
)


class ActorSearch(forms.Form):
    first_name = forms.CharField(
        label='Имя',
        required=False,
        max_length=255,
        validators=[
            [ONLY_LETTERS_VALIDATOR],
        ],
    )
    second_name = forms.CharField(
        label='Фамилия',
        required=False,
        max_length=255,
        validators=[
            [ONLY_LETTERS_VALIDATOR],
        ],
    )
    gender = forms.ChoiceField(
        label='Пол',
        required=False,
        choices=GENDER_CHOICES,
    )


class ActorForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Имя',
        required=True,
        max_length=255,
        validators=[
            ONLY_LETTERS_VALIDATOR,
        ],
    )
    second_name = forms.CharField(
        label='Фамилия',
        required=True,
        max_length=255,
        validators=[
            ONLY_LETTERS_VALIDATOR,
        ],
    )

    class Meta:
        model = models.Actor
        fields = '__all__'
        labels = {
            'actorid': 'ID-карта актера',
            'creativeteam': 'Творческая группа',
            'plays': 'Спектакли',
        }


class PlayForm(forms.ModelForm):
    class Meta:
        model = models.Play
        fields = '__all__'
