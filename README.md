# Senticnet API

[![Image](https://zenodo.org/badge/doi/10.5281/zenodo.9805.png "DOI") ](http://dx.doi.org/10.5281/zenodo.9805 "DOI")

Simple API to use Senticnet 4 (http://sentic.net/).


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
polarity_value = sn.polarity_value('love')
polarity_intense = sn.polarity_intense('love')
moodtags = sn.moodtags('love')
semantics = sn.semantics('love')
sentics = sn.sentics('love')
```

Also, you can use other languages:

```python
from senticnet.senticnet import Senticnet

sn = Senticnet('pt')
concept_info = sn.concept('amor')
polarity_value = sn.polarity_value('amor')
polarity_intense = sn.polarity_intense('amor')
moodtags = sn.moodtags('amor')
semantics = sn.semantics('amor')
sentics = sn.sentics('amor')
```

You can find all supported languages here: http://sentic.net/api/

## About Senticnet

SenticNet is an initiative conceived at the MIT Media Laboratory in 2010 within an industrial Cooperative Awards in Science and Engineering (CASE) research project, funded by the UK Engineering and Physical Sciences Research Council (EPSRC) and born from the collaboration between the University of Stirling, the Media Lab, and Sitekit Labs.

Currently, both the SenticNet knowledge base and the SenticNet framework are being maintained and further developed by the Sentic Team, a multidisciplinary research group based at the School of Computer Engineering of Nanyang Technological University in Singapore, but also by many other sentic enthusiasts around the world.

Please acknowledge the authors by citing SenticNet 4 in any research work or presentation containing results obtained in whole or in part through the use of the API:

*E. Cambria, S. Poria, R. Bajpai, and B. Schuller. SenticNet 4: A semantic resource for sentiment analysis based on conceptual primitives. In: COLING, pp. 2666-2677, Osaka (2016)*
