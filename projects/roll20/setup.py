try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Sargarus',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'shagohod@list.ru',
    'version': '0.1',
    'install_requires':'nose',
    'packages': 'roll20',
    'scripts': 'bin\roll.py',
    'name': 'roll.py'
}

setup(**config)
