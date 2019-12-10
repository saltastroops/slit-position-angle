"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'astropy', 'astroquery', 'Click'
]

setup_requirements = ['pytest-runner']

test_requirements = ['pytest']

setup(
    author="SAAO/SALT",
    author_email='salt-software@saao.ac.za',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Calculate the position angle for a longslit observation.",
    install_requires=requirements,
    entry_points='''
        [console_scripts]
        spa=slit_position_angle.cli:cli
    ''',
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='position angle',
    name='slit_position_angle',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/saltastroops/slit_position_angle',
    version='0.1.0',
    zip_safe=False,
)
