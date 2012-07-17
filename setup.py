from distutils.core import setup
try:
	from setuptools import setup
except:
	pass

setup(
    name = "pyplug",
    version = "0.1.2",
    author = "Stanislav Feldman",
    description = ("Python plugin framework"),
    url = "https://github.com/stanislavfeldman/pyplug",
    keywords = "plugin",
    packages=['pyplug'],
    install_requires = ["putils", "pev"],
    classifiers=[
        "Topic :: Software Development"
    ],
)
