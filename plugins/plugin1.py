from core import Plugin

class Plugin1(Plugin):
	id = "12423"
	name = "plugin1"
	version = "0.0.1"
	author = "Stanislav Feldman"
	description = "super plugin"
	dependencies = ["putils"]
	def get_view(self):
		return "hello from plugin1"
