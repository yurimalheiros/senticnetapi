from setuptools import setup

packages = ['senticnet']

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='senticnet',
      version='1.6',
      description='Access SenticNet data using Python',
      long_description_content_type='text/markdown',
      long_description=long_description,
      author=u'Yuri Malheiros',
      author_email='yuri@dcx.ufpb.br',
      url='https://github.com/yurimalheiros/senticnetapi',
      packages=packages,
      package_data={'': ['LICENSE', 'README.md'], 'senticnet': []},
      package_dir={'senticnet': 'senticnet'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries'],
)
