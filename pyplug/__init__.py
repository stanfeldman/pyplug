from putils.dynamics import Importer, Introspector
from putils.filesystem import Dir
from types import FunctionType
import os, sys
import mimetypes
from copy import copy


class MetaPlugin(type):
	def __new__(metaclass, classname, bases, attrs):
		new_class = super(MetaPlugin, metaclass).__new__(metaclass, classname, bases, attrs)
		new_obj = new_class()
		if "implements" in attrs:
			for iface in attrs["implements"]:
				iface._plugins.append(new_obj)
		return new_class
	
	
class Plugin(object):
	"""
	Plugin must inherit from this class.
	This class register itself as implementation of some interfaces.
	"""
	__metaclass__ = MetaPlugin


class MetaInterface(type):
	def __new__(metaclass, classname, bases, attrs):
		new_class = super(MetaInterface, metaclass).__new__(metaclass, classname, bases, attrs)
		new_class._plugins = []
		new_class.plugins = classmethod(MetaInterface.plugins)
		new_class.plugin = classmethod(MetaInterface.plugin)
		for k, v in attrs.iteritems():
			if type(v) is FunctionType:
				setattr(new_class, k+"_get_all", classmethod(MetaInterface.meta_method_get_all(k)))
				setattr(new_class, k+"_call_all", classmethod(MetaInterface.meta_method_call_all(k)))
				setattr(new_class, k, classmethod(MetaInterface.meta_method_call_first(k)))
			else:
				setattr(new_class, k+"_get_all", classmethod(MetaInterface.meta_property_all(k)))
				setattr(new_class, k, classmethod(MetaInterface.meta_property_first(k)))
		return new_class
		
	@staticmethod
	def plugins(cls):
		results = set()
		for pl in cls._plugins:
			results.add(pl)
		for subclass in Introspector.all_subclasses(cls):
			for spl in subclass._plugins:
				results.add(spl)
		return list(results)
		
	@staticmethod
	def plugin(cls, name, fullname=True, ignorecase=False):
		"""
		Find plugin by class name
		"""
		for pl in cls.plugins():
			pl_name = Introspector.classname(pl, full=fullname)
			if ignorecase:
				name = name.lower()
				pl_name = pl_name.lower()
			if name == pl_name:
				return pl
		raise IndexError("There is no plugin with name %s" % name)
	
	@staticmethod
	def meta_method_get_all(method_name):
		def wrapper(cls, *args, **kwargs):
			for impl in cls.plugins():
				if hasattr(impl, method_name):
					method = getattr(impl, method_name)
					yield method(*args, **kwargs)
		return wrapper
		
	@staticmethod
	def meta_method_call_all(method_name):
		def wrapper(cls, *args, **kwargs):
			for impl in cls.plugins():
				if hasattr(impl, method_name):
					method = getattr(impl, method_name)
					method(*args, **kwargs)
		return wrapper
		
	@staticmethod
	def meta_method_call_first(method_name):
		def wrapper(cls, *args, **kwargs):
			for impl in cls.plugins():
				if hasattr(impl, method_name):
					method = getattr(impl, method_name)
					return method(*args, **kwargs)
		return wrapper
		
	@staticmethod
	def meta_property_all(method_name):
		def wrapper(cls):
			for impl in cls.plugins():
				if hasattr(impl, method_name):
					yield getattr(impl, method_name)
		return wrapper
		
	@staticmethod
	def meta_property_first(method_name):
		def wrapper(cls):
			for impl in cls.plugins():
				if hasattr(impl, method_name):
					return getattr(impl, method_name)
		return wrapper
		
		
class Interface(object):
	"""
	Derive from this class to create plugin interface.
	Then you can call all plugins or get some by name.
	"""
	__metaclass__ = MetaInterface
	
	
class PluginLoader(object):
	@staticmethod
	def load(plugin_path):
		try:
			plugin_path = Importer.module_path(plugin_path) # maybe plugin_path is module name
		except:
			pass
		def cb(p):
			if mimetypes.guess_type(p)[0] == "text/x-python":
				Importer.import_module_by_path(p)
		Dir.walk(plugin_path, cb)
