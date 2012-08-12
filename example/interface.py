from pyplug import Interface


class MyInterface(Interface):
	attr = None
	def do_smth(self):
		pass
	def get_smth(self):
		pass
	@property
	def prop(self):
		pass
