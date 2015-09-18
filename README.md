# Senticnet API

[![Image](https://zenodo.org/badge/doi/10.5281/zenodo.9805.png "DOI") ](http://dx.doi.org/10.5281/zenodo.9805 "DOI")

Simple API to use Senticnet 3 (http://sentic.net/) without be bothered by RDF stuff.

## ====== NOTE ======

The official Senticnet RDF is currently experiencing some problem, so this API is not working correctly.
The creators of Senticnet told me that they will fix the RDF problem soon. However, @tanayz gently coded a workaround to solve this temporary problem, so, if you need to use the Python Senticnet API now, please use this code: https://github.com/tanayz/senticnetapi


## Install

Using pip:

```
$ pip install senticnet
```

Using the repository code:

```
$ python setup.py install
```

## How to use

```python
from senticnet.senticnet import Senticnet

sn = Senticnet()
concept_info = sn.concept('love')
polarity = sn.polarity('love')
semantics = sn.semantics('love')
sentics = sn.sentics('love')
```

## About Senticnet

SenticNet is an initiative conceived at the MIT Media Laboratory in 2010 within an industrial Cooperative Awards in Science and Engineering (CASE) research project, funded by the UK Engineering and Physical Sciences Research Council (EPSRC) and born from the collaboration between the University of Stirling, the Media Lab, and Sitekit Labs.

Please acknowledge the authors by citing the Sentic Computing book in any research work or presentation containing results obtained in whole or in part through the use of the API.
