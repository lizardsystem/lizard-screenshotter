lizard-screenshotter
==========================================

Introduction
------------

A django project intended to 'capture' screenshots of given urls and return them as images.


Live demo
---------
A live demo of lizard-screenshotter can be found at http://screenshotter.lizard.net/


Technology
----------

Uses PhantomJS to capture. PhantomJS is a Javascript wrapper around a headless Webkit engine.


Getting started
===============

Symlink a buildout configuration
--------------------------------

Initially, there's no ``buildout.cfg``. You need to make that a symlink to the
correct configuration. On your development machine, that is
``development.cfg`` (and ``staging.cfg`` or ``production.cfg``, for instance
on the server)::

    $ ln -s development.cfg buildout.cfg


Installation of packages on Ubuntu
----------------------------------

::
    sudo apt-get install build-essential python-dev python-psycopg2 python-matplotlib python-imaging python-gdal

Build the project
-----------------

    $ bin/buildout


Play
----

    $ bin/phantomjs --disk-cache=yes --ignore-ssl-errors=yes capture.js http://demo.lizard.net/ /tmp/map.png 1024 768
