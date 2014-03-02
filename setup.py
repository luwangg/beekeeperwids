#!/usr/bin/python

try:
    from setuptools import setup
except ImportError:
    print("No setuptools found, attempting to use distutils instead.")
    from distutils.core import setup

setup(name='killerbeewids',
      version='0.1',
      description='Wireless Intrusion Detection System for 802.15.4/ZigBee',
      author='TBD',
      author_email='javier@riverloopsecurity.com',
      url='http://www.riverloopsecurity.com',
      packages=['killerbeewids',
                'killerbeewids.drone', 'killerbeewids.drone.plugins', 'killerbeewids.drone.plugins.capture',
                'killerbeewids.wids', 'killerbeewids.wids.modules',
                'killerbeewids.utils'],
      scripts=['cli/zbdrone', 'cli/zbwids'],
      # This is a *nix specific path and will need to provide for other options on different systems
      data_files=[('/opt/kbwids/',['./killerbeewids/wids/modules/modules.xml', './killerbeewids/drone/plugins/plugins.xml'])],
      # A version of KillerBee earlier than 2.5.0 may work, but has not been tested.
      install_requires=['flask', 'killerbee >= 2.5.0'],
      # Consider using Markdown such as in https://coderwall.com/p/qawuyq
      long_description = open('README.txt').read(),
     )
