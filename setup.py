from __future__ import unicode_literals

from codecs import open as codecs_open
from setuptools import setup


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(name='adopy',
      version='0.0.3',
      description='',
      long_description=long_description,
      classifiers=[],
      keywords='',
      author='Jaeyeong Yang',
      author_email='jaeyeong.yang1125@gmail.com',
      url='https://github.com/JaeyeongYang/adopy',
      license='MIT',
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'typing',
          'numpy',
          'pandas',
          'scipy',
      ],
      extras_require={
          'dev': [
              'flake8',
              'mypy',
              'pytest',
              'yapf',
          ],
          'test': [
              'codecov',
              'pytest',
              'pytest-cov',
          ],
      }
      )
