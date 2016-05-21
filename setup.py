from setuptools import setup

setup(
    name = 'mcnotify',
    version = '1.0.0',
    author = 'Shusui Moyatani',
    author_email = 'syusui.s@gmail.com',
    url = 'https://github.com/syusui-s/mcnotify',
    license = ['MIT'],
    description = 'Minecraft status notifier',

    scripts = ['scripts/mcnotify_update'],
    install_requires = ['mcstatus>=2.1'],
)
