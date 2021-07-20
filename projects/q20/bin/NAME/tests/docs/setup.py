try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sonfig = {
    'description': 'My Project',
    'author': 'Serj Kru',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'shagohod@list.ru',
    'version': '0.1',
    'install_requires':['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
