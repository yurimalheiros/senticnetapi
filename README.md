# SenticNet API

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1246573.svg)](https://doi.org/10.5281/zenodo.1246573)

Simple API to use SenticNet (http://sentic.net/).


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
from senticnet.senticnet import SenticNet

sn = SenticNet()
concept_info = sn.concept('love')
polarity_label = sn.polarity_label('love')
polarity_value = sn.polarity_value('love')
moodtags = sn.moodtags('love')
semantics = sn.semantics('love')
sentics = sn.sentics('love')
```

Also, you can use other languages:

```python
from senticnet.babelsenticnet import BabelSenticNet

bsn = BabelSenticNet('pt')
concept_info = sn.concept('amor')
polarity_label = sn.polarity_label('amor')
polarity_value = sn.polarity_value('amor')
moodtags = sn.moodtags('amor')
semantics = sn.semantics('amor')
sentics = sn.sentics('amor')
```

You can find all supported languages here: http://sentic.net/api/

## About SenticNet

SenticNet is an initiative conceived at the MIT Media Laboratory in 2010 within an industrial Cooperative Awards in Science and Engineering (CASE) research project, funded by the UK Engineering and Physical Sciences Research Council (EPSRC) and born from the collaboration between the University of Stirling, the Media Lab, and Sitekit Labs.

Currently, both the SenticNet knowledge base and the SenticNet framework are being maintained and further developed by the Sentic Team, a multidisciplinary research group based at the School of Computer Engineering of Nanyang Technological University in Singapore, but also by many other sentic enthusiasts around the world.

Please acknowledge the authors by citing SenticNet 6 in any research work or presentation containing results obtained in whole or in part through the use of the API:

*E Cambria, Y Li, F Xing, S Poria, K Kwok. SenticNet 6: Ensemble application of symbolic and subsymbolic AI for sentiment analysis. In: CIKM, 105-114 (2020)*
