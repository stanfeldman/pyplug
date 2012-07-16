from pyplug import Plugin
from interface import MyInterface

class Plugin2(Plugin):
	name = "plugin2"
	version = "0.0.1"
	author = "Stanislav Feldman"
	description = "super plugin2"
	implements = [MyInterface]
	dependencies = ["putils"]
	
	def do_smth(self):
		print "hi from plugin2"
		
	def get_smth(self):
		return "result from plugin2"
