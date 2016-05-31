# !/usr/bin/env python
#
# setup.py script
#
# copyright 2016 anirban roy das <anirban.nick@gmail.com>
#
#

# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
import codecs
import os


# ############## general config ##############


NAME = "mosquittoChat"

VERSION = '1.0'


PACKAGES = ["mosquittoChat", "mosquittoChat.apps", "mosquittoChat.apps.main", "mosquittoChat.apps.mosquitto"]

PROJECT_URL = 'https://github.com/anirbanroydas/mosquittoChat'

AUTHOR = 'Anirban Roy Das'

EMAIL = 'anirban.nick@gmail.com'

KEYWORDS = "chat server amqp protocol rabbitmq message broker via sockjs websocket tornado with sockjs-tornado and amqp python client library Pika"

CLASSIFIERS = [

    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 4 - Beta',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',

    # Pick your license as you wish (should match "license" above)
    'License :: OSI Approved :: MIT License',

    # Specify the Natural Language
    'Natural Language :: English',

    # Specify the operating systems it can work on
    'Operating System :: OS Independent',
    # Specify the Python versions you support here. In particular, ensure that
    # you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: Implementation :: CPython',

]

INSTALL_REQUIRES = ["tornado >= 2.2.1",
                    "sockjs-tornado",
                    "paho-mqtt",
                    "setuptools >= 0.7.0", ]

EXTRAS_REQUIRE = {}

PACKAGE_DATA = {
    # data files need to be listed both here (which determines what gets
    # installed) and in MANIFEST.in (which determines what gets included
    # in the sdist tarball)
    "mosquittoChat": ["static/css/*.css",
                   "static/js/*.js",
                   "templates/*.html",
                   ],

}

# DATA_FILES =[]

HERE = os.path.abspath(os.path.dirname(__file__))

# ############  End of basic config ###########



# Get the long description from the README file
with codecs.open(os.path.join(HERE, 'README.rst'), 'rb', 'utf-8') as f:
    LONG_DESCRIPTION = f.read()




# ### The main setup function ######
setup(
    name=NAME,

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=VERSION,

    description='A Chat Server based on MQTT protocol using Mosquitto (broker a C implementation of MQTT),\
                websocket, sockjs javascript library on client(browser) side, sockjs-tornado, tornado,\
                and paho-mqtt (mqtt python client library)',
    long_description=LONG_DESCRIPTION,

    # The project's main homepage.
    url=PROJECT_URL,

    # Author details
    author=AUTHOR,
    author_email=EMAIL,

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=CLASSIFIERS,

    # What does your project relate to?
    keywords=KEYWORDS,

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=PACKAGES,

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=INSTALL_REQUIRES,

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require=EXTRAS_REQUIRE,

    # If set to True, this tells setuptools to automatically include
    # any data files it finds inside your package directories that
    # are specified by your MANIFEST.in file.
    # include_package_data = True


    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data=PACKAGE_DATA,

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=DATA_FILES,

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'mosquittoChat=mosquittoChat.server:main',
        ],
    },
)
