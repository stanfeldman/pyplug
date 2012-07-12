from pyplug import Plugin
from interface import MyInterface

class Plugin1(Plugin):
	id = "12423"
	name = "plugin1"
	version = "0.0.1"
	author = "Stanislav Feldman"
	description = "super plugin"
	implements = [MyInterface]
	dependencies = ["putils"]
	
	def do_smth(self):
		print "hello from plugin1"
