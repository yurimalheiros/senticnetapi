from senticnet.senticnet import Senticnet

sn = Senticnet()
polarity = sn.get_polarity("Friday night")
print polarity
