# -*- coding: utf-8 -*-

from distutils.core import setup
setup(
    name = 'dokuwiki',
    version = '0.2',
    author = 'François Ménabé',
    author_email = 'francois.menabe@gmail.com',
    url = 'http://github.com/francois.menabe/python-dokuwiki',
    download_url='https://github.com/fmenabe/python-clg',
    license='MIT License',
    description = 'Manage DokuWiki via XML-RPC API.',
    long_description=open('README.rst').read(),
    keywords=['xmlrpc', 'dokuwiki'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    py_modules = ['dokuwiki'],
)
