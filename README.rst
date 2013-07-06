django-print-settings
=====================

.. image:: https://secure.travis-ci.org/msabramo/django-print-settings.png?branch=master
   :target: http://travis-ci.org/msabramo/django-print-settings

Adds a ``print_settings`` Django management command.


Setting it up
-------------

Install:

.. code-block:: bash

    pip install django-print-settings

Add ``django_print_settings`` to ``INSTALLED_APPS`` in your Django project's ``settings.py``:

.. code-block:: python

    INSTALLED_APPS = (
        'django_print_settings',
        ...
    )


Usage
-----

Do:

.. code-block:: bash

    python manage.py print_settings

or:

.. code-block:: bash

    python manage.py print_settings --format=json

For help:

.. code-block:: bash

    python manage.py print_settings --help


PyPI
----

https://pypi.python.org/pypi/django-print-settings


Issues
------

Send your bug reports and feature requests to https://github.com/msabramo/django-print-settings/issues
