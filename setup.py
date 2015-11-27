from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='vacation',
      version='0.3',
      description='Track your vacation days.',
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
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
      install_requires=[
          'holidays',
          'workdays',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False,
      entry_points={
          'console_scripts': ['vacation=vacation.vacation:main'],
      },)
