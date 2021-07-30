try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ex47',
    'author': 'Sargarus',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'shagohod@list.ru',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': ['ex47\game.py'],
    'name': 'ex47'
}

setup(**config)
