import sys
from setuptools import setup, find_packages
from serviceweb import __version__


with open('requirements.txt') as f:
    deps = [dep for dep in f.read().split('\n') if dep.strip() != ''
            and not dep.startswith('-e')]
    install_requires = deps


setup(name='serviceweb',
      version=__version__,
      packages=find_packages(),
      description="Mozilla Service Book Web App",
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
      [console_scripts]
      serviceweb = serviceweb.server:main
      """)
