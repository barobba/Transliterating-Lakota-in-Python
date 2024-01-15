
# Transliterating Lakota (Python)

Here is an example of using the ICU library to transliterate a Lakota string in Python.

---
### Requirements
**System**
- Python 3
- The "ICU4C" library

**Python Packages**
- icupy ([GitHub](https://github.com/miute/icupy), [PyPI](https://pypi.org/project/icupy/))

---
### Install

On a Mac (using Brew):
```
brew install icu4c
brew install cmake
export CMAKE_PREFIX_PATH="$(brew --prefix)/opt/icu4c"
pip install icupy
```
Note: [When installing the "icupy" Python package on a Mac, there is a bug finding the ICU4C files [SOLVED]](https://github.com/OpenRCT2/OpenRCT2/issues/8000#issuecomment-450967864)

---
### Run
`python program.py`

---
### Links
- [Lakota orthographies](https://www.languagegeek.com/siouan/lakota.html)
- [ICU Transliterator Class](https://unicode-org.github.io/icu-docs/apidoc/dev/icu4c/classicu_1_1Transliterator.html)