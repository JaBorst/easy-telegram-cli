from setuptools import setup

setup(
    name='tbot',
    version='0.1',
    packages=['tbot'],
    url='',
    license='',
    author='Janos Borst',
    author_email='borst@informatik.uni-leipzig.de',
    description='A very simple Python Wrapper around the Telegram API for sending Text messages from a python program and from Commandline.',
    scripts = ["scripts/tbot-message", "scripts/tbot-document", "scripts/tbot-image"],
    install_requires = ["python-telegram-bot"]
)
