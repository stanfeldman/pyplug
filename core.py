from abc import ABCMeta, abstractmethod
from sys import path
path.append("/home/stanislavfeldman/projects/python/putils/")
from putils.dynamics import Importer

class Plugin(object):
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def get_view():
		pass
	
class PluginLoader(object):
	def load_plugin(self, name):
		return Importer.import_class(name)
	
	def call_plugin(self, name):
		p = self.load_plugin(name)()
		print p.id
		print p.get_view()
		
if __name__ == "__main__":
	pl = PluginLoader()
	pl.call_plugin("plugins.plugin1.Plugin1")
