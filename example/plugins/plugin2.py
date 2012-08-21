from pyplug import Plugin
from interface import MyInterface

class Plugin2(Plugin):
	implements = [MyInterface]
	
	attr = "hey from pl2"
	
	def name(self):
		return "plugin2"
	
	def do_smth(self):
		print "hi from plugin2"
		
	def get_smth(self):
		return "result from plugin2"
		
	@property
	def prop(self):
		return 555
