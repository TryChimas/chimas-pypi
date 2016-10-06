from setuptools import setup

with open('chimas/requirements.txt') as f:
    required = f.read().splitlines()

with open('version-counter') as vcounter:
    version_counter = vcounter.read().strip()

# https://packaging.python.org/distributing/#setup-args

setup(
    name='chimas',
    version='0.0.6dev{}'.format(version_counter),
    description='This is Chimas BBS server',
    url='https://github.com/TryChimas/chimas',
    author='Iacchus Mercurius',
    license='GNU GPL v.3',
    classifiers=[
        #https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='chimas bbs forum server',
    #packages=['chimas',''],
    package_dir={'':'chimas'},
    packages=['.', 'chimas.core'],
    install_requires=required,
    #include_package_data = True,
    package_data={
        '.' : ['version-counter'],
        'chimas' : ['requirements.txt','etc/*'],
    },
    #package_dir={'' : '.', 'chimas.core' : 'core/'},
    #package_dir={'' : '.'},
    #py_modules=['chimas_server'],
    #install_requires=[
    #    'Click',
    #],
    entry_points='''
        [console_scripts]
        chimas=chimas:run_chimas
        chimas-server=chimas:chimascli
    ''',
)
