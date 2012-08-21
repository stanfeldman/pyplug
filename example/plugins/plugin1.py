from pyplug import Plugin
from interface import MyInterface

class Plugin1(Plugin):
	implements = [MyInterface]
	
	attr = "hey from pl1"
	
	def name(self):
		return "plugin1"
	
	def do_smth(self):
		print "hello from plugin1"
		
	def get_smth(self):
		return "result from plugin1"
		
	@property
	def prop(self):
		return "value from property in Plugin 1"
