# Nerd Font icons for python

## Installation 

```{.sh}
pip install nerdfont
```

## Usage 

```{.py}
import nerdfont as nf

print(nf.icons['fa-thumbs_up'])
>>> 
```

## Build 

```{.sh}
# Run the generate script to download nerd font's character mapping
# and generate a python-formatted version of it.  Save this file as icons.py
# in the nerdfont subdirectory.  Note that this pulls the latest revision
# on the master branch.  You can easily change this  with the --revision flag.

python3 ./nerdfont/generate.py > ./nerdfont/icons.py

rm -r build dist nerdfont.egg-info && \
python3 -m build && \
python3 -m pip install . && \
python3 -m twine --repository testpypi upload dist/*
```

## License

The code in this repository is licensed under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

The character codes included with this package are part of the [Nerd Font project](https://github.com/ryanoasis/nerd-fonts).
