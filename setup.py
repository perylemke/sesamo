from os import environ
from pathlib import Path
from setuptools import setup
from shutil import copyfile


try:
    config_dir = Path(environ['$XDG_CONFIG_HOME']) / 'sesamo'
except KeyError:
    config_dir = Path.home() / '.config' / 'sesamo'

config_dir.mkdir(exist_ok=True)
current_dir = Path(__file__).parent
copyfile(current_dir / 'config.ini.example',
         config_dir / 'config.ini')

setup(
    name='sesamo',
    py_modules=['sesamo'],
    entry_points={
        'console_scripts': [
            'sesamo = sesamo:main',
        ],
    },
)
