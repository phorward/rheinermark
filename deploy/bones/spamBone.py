# -*- coding: utf-8 -*-
import random, logging
from server import session, translate
from server.bones import numericBone


class spamBone(numericBone):

	def __init__(self, required=True, precision=0, *args, **kwargs):
		super(spamBone, self).__init__(required=True, precision=0, *args, **kwargs)

	def _getRandomNumber(self):
		num = 0
		while num == 0:
			num = int(random.random() * 10)

		return num

	@property
	def descr(self):
		a = session.current.get("spamBone.a")
		b = session.current.get("spamBone.b")

		if a is None or b is None:
			a = session.current["spamBone.a"] =  self._getRandomNumber()
			b = session.current["spamBone.b"] = self._getRandomNumber()
			session.current.markChanged()

		return translate("spambone.confirm", a=translate("spambone.%d" % a), b=translate("spambone.%d" % b))

	@descr.setter
	def descr(self, value):
		pass

	def isInvalid(self, value):
		a = session.current.get("spamBone.a") or 0
		b = session.current.get("spamBone.b") or 0
		if a and b:
			del session.current["spamBone.a"]
			del session.current["spamBone.b"]
			session.current.markChanged()

			try:
				value = int(value)
			except:
				return False

		logging.info("a=%r, b=%r, value=%r, expecting=%r", a, b, value, a+b)
		if value != a + b:
			return _("spambone.invalid")
