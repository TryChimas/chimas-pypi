# i have a python 3 virtualenv relative to this repo at venv/

cd chimas
git pull origin master
cd -


. venv/bin/activate

rm -rf chimas.egg-info/
rm -rf dist/

python setup.py sdist bdist

twine upload dist/*
