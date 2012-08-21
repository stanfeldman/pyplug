from sys import path
path.append("/home/stanislavfeldman/projects/python/putils/")
path.append("/home/stanislavfeldman/projects/python/pyplug/")
import os
from pyplug import PluginLoader, Interface
from interface import MyInterface, MyBaseInterface
from putils.dynamics import Importer, Introspector
		
		
if __name__ == "__main__":
	project_dir = os.path.dirname(os.path.abspath(__file__))
	plugin_dir = os.path.join(project_dir, "plugins")
	#PluginLoader.load("/home/stanislavfeldman/projects/python/pyplug/example/plugins")
	PluginLoader.load("plugins")
	for result in MyInterface.get_smth_get_all():
		print result
	MyInterface.do_smth_call_all()
	print MyInterface.get_smth()
	print MyInterface.prop()
	for res in MyBaseInterface.attr_get_all():
		print res
	for res in MyBaseInterface.name_get_all():
		print res
	#print MyInterface.attr()
	print MyInterface.plugins["Plugin2"].get_smth()
	print MyBaseInterface.__subclasses__()
