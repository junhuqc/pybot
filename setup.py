from os.path import join, dirname
from setuptools import setup, find_packages

__version__ = open(join(dirname(__file__), 'pybot/VERSION')).read().strip()

install_requires = (
    'requests>=2.4.0',
    'websocket-client>=0.22.0',
    'slacker>=0.5.5',
    'six>=1.10.0'
) # yapf: disable

excludes = (
    '*test*',
    '*local_settings*',
) # yapf: disable

setup(name='pybot',
      version=__version__,
      license='BSD',
      description='A simple slack bot for deploy, test report, and event message!',
      author='Wilson',
      author_email='blaise1190@gmail.com',
      url='https://github.com/junhuqc/pybot',
      platforms=['Any'],
      packages=find_packages(exclude=excludes),
      install_requires=install_requires,
      classifiers=['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5'])
