"""
Based on ``setup.py`` from django-extensions.
"""
import os
import sys
from distutils.command.install_data import install_data
from distutils.command.install import INSTALL_SCHEMES
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


class osx_install_data(install_data):
    # On MacOS, the platform-specific lib dir is at:
    #   /System/Library/Framework/Python/.../
    # which is wrong. Python 2.5 supplied with MacOS 10.5 has an Apple-specific
    # fix for this in distutils.command.install_data#306. It fixes install_lib
    # but not install_data, which is why we roll our own install_data class.

    def finalize_options(self):
        # By the time finalize_options is called, install.install_lib is set to
        # the fixed directory, so we set the installdir to install_lib. The
        # install_data class uses ('install_data', 'install_dir') instead.
        self.set_undefined_options('install', ('install_lib', 'install_dir'))
        install_data.finalize_options(self)

if sys.platform == "darwin":
    cmdclasses = {'install_data': osx_install_data}
else:
    cmdclasses = {'install_data': install_data}


def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

# Tell distutils to put the data_files in platform-specific installation
# locations. See here for an explanation:
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)
extensions_dir = 'django_print_settings'

for dirpath, dirnames, filenames in os.walk(extensions_dir):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

version = __import__('django_print_settings').__version__

setup(
    name='django-print-settings',
    version=version,
    description="print_settings management command for Django",
    long_description=read('README.rst'),
    author='Marc Abramowitz',
    author_email='marc@marc-abramowitz.com',
    url='http://github.com/msabramo/django-print-settings',
    license='New BSD License',
    platforms=['any'],
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    package_data={'': ['README.rst']},
    cmdclass=cmdclasses,
    data_files=data_files,
    tests_require=['Django>=1.3.1'],
    test_suite='tests.test_import',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Utilities',
    ],
)
