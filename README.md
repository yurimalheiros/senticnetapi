# Senticnet API

Ultra simple API to use Senticnet 2 without be bothered by RDF stuff.

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
