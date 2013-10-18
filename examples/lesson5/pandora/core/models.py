# encoding=utf-8
from django.db import models


class TimeStampedModel(models.Model):
	"""
	Абстрактный базовый класс,
	предоставляющий поля создания
	и обновления экземпляра
	"""
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True
