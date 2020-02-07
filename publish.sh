#!/usr/bin/env sh

# Go to script directory
cd `(dirname $0)`

# Cleanup
rm -rf dist/
rm -rf build/
rm -rf *.egg-info

# Generate
python setup.py sdist bdist_wheel

# Upload
twine upload dist/*