# encoding=utf-8
from django.db import models
from core.models import TimeStampedModel

kinds = (
	(1, 'Твёрдое'),
	(2, 'Жидкость'),
	(3, 'Газ'),
	)


class Thing(TimeStampedModel):
	"""
	Модель сущностей
	"""
	title = models.TextField('Название', max_length=32)
	things_type = models.ForeignKey('ThingsType')

	def __unicode__(self):
		return u'{}, ({})'.format(self.name, self.things_type)

	def get_absolute_url(self):
		return u'things/{}/'.format(self.id)


class ThingsType(TimeStampedModel):
	"""
	Типы сущностей
	"""
	title = models.TextField('Название', max_length=32)
	kind = models.CharField('Состояние', max_length=2, choices=kinds)
	color = models.TextField('Цвет', max_length=32)

	def __unicode__(self):
		return u'{}'.format(self.title)
