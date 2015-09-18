from setuptools import setup, find_packages

setup(
    name='vspkgenerator',
    packages=find_packages(exclude=['*tests*']),
    include_package_data=True,
    version='0.0.1',
    description='VSPK Generator',
    author='Christophe Serafin',
    author_email='christophe.serafin@nuagenetworks.net',
    url="https://github.com/nuagenetworks/monolithe",
    classifiers=[],
    install_requires=[line for line in open('requirements.txt')],
    entry_points={
        'console_scripts': [
            'generate-vspk = vspkgenerator:generate_vspk'
            'generate-vspkdoc = vspkgenerator:generate_vspkdoc'
            'generate-vspk-apidoc = vspkgenerator:generate_vspk_apidoc'
        ]
    }
)
