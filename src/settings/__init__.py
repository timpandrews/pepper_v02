from src.settings.base import *


try:
	from src.settings.local import *
except:
	pass


try:
	from src.settings.production import *
except:
	pass