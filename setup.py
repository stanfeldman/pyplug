from distutils.core import setup
try:
	from setuptools import setup
except:
	pass

setup(
    name = "pyplug",
    version = "0.2.1",
    author = "Stanislav Feldman",
    description = ("Python plugin framework"),
    url = "https://github.com/stanislavfeldman/pyplug",
    keywords = "plugin",
    packages=['pyplug'],
    install_requires = ["putils"],
    classifiers=[
        "Topic :: Software Development"
    ],
)
