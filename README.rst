django-print-settings
=====================

Adds a ``print_settings`` Django management command.


Setting it up
-------------

Install::

    pip install django-print-settings

Add ``django_print_settings`` to ``INSTALLED_APPS`` in your Django project's ``settings.py``::

    INSTALLED_APPS = (
        'django_print_settings',
        ...
    )


Usage
-----

Do::

    python manage.py print_settings

or::

    python manage.py print_settings --format=json

For help::

    python manage.py print_settings --help
