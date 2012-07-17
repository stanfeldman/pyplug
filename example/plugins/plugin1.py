from pyplug import Plugin
from interface import MyInterface

class Plugin1(Plugin):
	name = "plugin1"
	version = "0.0.1"
	author = "Stanislav Feldman"
	description = "super plugin"
	implements = [MyInterface]
	events = {
		"app.started": "on_event1"
	}
	#dependencies = ["putils"]
	
	def do_smth(self):
		print "hello from plugin1"
		
	def get_smth(self):
		return "result from plugin1"
		
	def on_event1(self, msg):
		print "on event1:", msg
