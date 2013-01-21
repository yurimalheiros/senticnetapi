# Senticnet API

Ultra simple API to use Senticnet 2 without be bothered by RDF stuff.

## Install

```
$ pip install senticnet
```

## How to use

```python
from senticnet.senticnet import Senticnet

sn = Senticnet()
polarity = sn.polarity('love')
semantics = sn.semantics('love')
sentics = sn.sentics('love')
```
