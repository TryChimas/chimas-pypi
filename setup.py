from setuptools import setup

with open('chimas/requirements.txt') as f:
    required = f.read().splitlines()

# https://packaging.python.org/distributing/#setup-args

setup(
    name='chimas',
    version='0.0.6dev14',
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
    packages=['chimas', 'chimas.core'],
    install_requires=required,
    #include_package_data = True,
    package_data={
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
