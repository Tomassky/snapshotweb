from setuptools import setup, find_packages

setup(
    name='snapshotweb',  # Required
    version='1.0.0',  # Required
    description='Take a snapshot for the website and search it',  # Optional
    long_description=open('README.md').read(),  # Optional
    long_description_content_type='text/markdown',  # Optional, if using markdown for your README
    author='tomas.ma',  # Optional
    author_email='tomassky7.gmail.com',  # Optional
    license='MIT',  # Optional
    packages=find_packages(),  # Required
    install_requires=[
        # List all project dependencies here
        'anyio==4.2.0',
        'attrs==23.2.0',
        'beautifulsoup4==4.12.3',
        'blinker==1.7.0',
        'bs4==0.0.2',
        'certifi==2023.11.17',
        'click==8.1.7',
        'dominate==2.9.1',
        'exceptiongroup==1.2.0',
        'Flask==3.0.1',
        'Flask-Bootstrap==3.3.7.1',
        'gevent==23.9.1',
        'greenlet==3.0.3',
        'h11==0.14.0',
        'httpcore==1.0.2',
        'httpx==0.26.0',
        'idna==3.6',
        'iniconfig==2.0.0',
        'itsdangerous==2.1.2',
        'Jinja2==3.1.3',
        'MarkupSafe==2.1.4',
        'outcome==1.3.0.post0',
        'packaging==23.2',
        'pluggy==1.4.0',
        'PySocks==1.7.1',
        'pytest==8.0.0',
        'python-telegram-bot==20.8',
        'selenium==4.17.2',
        'sniffio==1.3.0',
        'sortedcontainers==2.4.0',
        'soupsieve==2.5',
        'tomli==2.0.1',
        'trio==0.24.0',
        'trio-websocket==0.11.1',
        'typing_extensions==4.9.0',
        'urllib3==2.1.0',
        'visitor==0.1.3',
        'Werkzeug==3.0.1',
        'wsproto==1.2.0',
        'xmltodict==0.13.0',
        'zope.event==5.0',
        'zope.interface==6.1',
    ],
    classifiers=[
        # Choose classifiers from https://pypi.org/classifiers/
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10.12',
    ],
)
