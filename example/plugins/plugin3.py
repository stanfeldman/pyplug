from pyplug import Plugin
from interface import MyBaseInterface

class Plugin3(Plugin):
	implements = [MyBaseInterface]
	
	attr = "hey from pl3"
	
	def name(self):
		return "plugin3"
	
	def do_smth(self):
		print "hi from plugin3"

