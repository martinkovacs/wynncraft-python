if [ -z "$1" ]; then
    echo "No version number"
    exit
fi

python3 -m pip install --user --upgrade setuptools wheel twine
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/wynncraft-$1*
