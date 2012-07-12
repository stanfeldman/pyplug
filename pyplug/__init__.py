from putils.dynamics import Importer
from putils.filesystem import Dir
from types import FunctionType
import os
import mimetypes


class MetaPlugin(type):
	def __new__(metaclass, classname, bases, attrs):
		new_class = super(MetaPlugin, metaclass).__new__(metaclass, classname, bases, attrs)
		if "implements" in attrs:
			new_obj = new_class()
			for iface in attrs["implements"]:
				iface.implementors.append(new_obj)
		return new_class
	
	
class Plugin(object):
	__metaclass__ = MetaPlugin


class MetaInterface(type):
	def __new__(metaclass, classname, bases, attrs):
		new_class = super(MetaInterface, metaclass).__new__(metaclass, classname, bases, attrs)
		new_class.implementors = []
		for k, v in new_class.__dict__.iteritems():
			if type(v) is FunctionType:
				setattr(new_class, k, classmethod(MetaInterface.meta_method(k)))
		return new_class
	
	@staticmethod
	def meta_method(method_name):
		def wrapper(cls, *args, **kwargs):
			for impl in cls.implementors:
				method = getattr(impl, method_name)
				method(*args, **kwargs)
		return wrapper
		
		
class Interface(object):
	__metaclass__ = MetaInterface
	
	
class PluginLoader(object):
	@staticmethod
	def load(project_dir, plugin_dir):
		def cb(p):
			if mimetypes.guess_type(p)[0] == "text/x-python" and os.path.basename(p) != "__init__.py":
				Importer.import_module_by_path(p, project_dir)
		Dir.walk(plugin_dir, cb)
