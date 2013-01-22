# Senticnet API

Ultra simple API to use Senticnet 2 (http://sentic.net/) without be bothered by RDF stuff.

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
