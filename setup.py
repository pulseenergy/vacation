from setuptools import setup

setup(name='vacation',
      version='0.1',
      description='Track your vacation days.',
      long_description='Handy little app to help you keep track of your accumulated and remaining vacation days.',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Topic :: Utilities',
      ],
      url='https://github.com/pulseenergy/vacation',
      author='Enernoc',
      author_email='supermitch@gmail.com',
      licence='GPL2',
      packages=['vacation'],
      include_package_data=True,
      zip_safe=False)
