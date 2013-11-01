from box.models import *

gold = ThingsType(title="Золото", kind=2, color="Жёлтый")
gold.save()

ferrum = ThingsType(title="Железо", kind=2, color="Чёрный")
ferrum.save()

ring = Thing(title="Кольцо", things_type=gold)
ring.save()

hammer = Thing(title="Молоток", things_type=ferrum)
hammer.save()
