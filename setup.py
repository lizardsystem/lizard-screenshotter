from setuptools import setup

version = '0.1dev'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CREDITS.rst').read(),
    open('CHANGES.rst').read(),
    ])

install_requires = [
    'Django',
    'django-celery',
    'django-extensions',
    'django-nose',
    'gunicorn',
    # 'lizard-map',
    # 'lizard-ui >= 4.0b5',
    'python-memcached',
    'raven',
    'werkzeug',
    'sorl-thumbnail',
    ],

setup(name='lizard-screenshotter',
      version=version,
      description="PhantomJS wrapper",
      long_description=long_description,
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Programming Language :: Python',
                   'Framework :: Django',
                   ],
      keywords=[],
      author='Gijs Nijholt',
      author_email='gijs.nijholt@nelen-schuurmans.nl',
      url='',
      license='GPL',
      packages=['lizard_screenshotter'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points={
          'console_scripts': [
          ]},
      )
