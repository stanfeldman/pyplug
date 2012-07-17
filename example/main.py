from sys import path
path.append("/home/stanislavfeldman/projects/python/putils/")
path.append("/home/stanislavfeldman/projects/python/pyplug/")
import os
from pyplug import PluginLoader
from interface import MyInterface
		
		
if __name__ == "__main__":
	project_dir = os.path.dirname(os.path.abspath(__file__))
	plugin_dir = os.path.join(project_dir, "plugins")
	PluginLoader.load(project_dir, plugin_dir)
	for result in MyInterface.get_smth_get_all():
		print result
	MyInterface.do_smth_call_all()
	print MyInterface.get_smth()
	print MyInterface.plugins["plugin2"].get_smth()
