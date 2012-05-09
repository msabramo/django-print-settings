import unittest


class ImportTest(unittest.TestCase):

    def test_import(self):
        from django_print_settings.management.commands.print_settings import Command

