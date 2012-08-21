from pyplug import Interface

class MyBaseInterface(Interface):
	attr = None
	def name(self):
		pass
	def do_smth(self):
		pass

class MyInterface(MyBaseInterface):
	def get_smth(self):
		pass
	@property
	def prop(self):
		pass
