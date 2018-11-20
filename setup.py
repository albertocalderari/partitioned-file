"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
import versioneer

setup(
    name='partitioned-file',
    version=versioneer.get_version(),
    mdclass=versioneer.get_cmdclass(),
    versionfile_build='partitioned_file/_version.py',
    versionfile_source='src/partitioned_file/_version.py',
    description='A python file object to write partitioned files',
    long_description='A python file object to write partitioned files. This is ideal for '
                     'writing data which is destined to be loaded into a distributed'
                     'system. At the moment local and GCS file systems supported.',
    url='https://github.com/albertocalderari/partitioned-file',
    author='Alberto Calderari',
    author_email='alerto.calderari@gmail.com',
    license='public',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: FIle Tools',
        'License :: Public',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='partitioned file gzip gcs',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['gcsfs==0.1.2', 'dask==0.20.0', 'toolz==0.9.0'],
    extras_require={
        'dev': ['setuptools==40.6.2', 'versioneer==0.18'],
        'test': ['unittest', 'coverage'],
    },
    package_data={},
    entry_points={},
)