from senticnet.senticnet import Senticnet

sn = Senticnet()
print "polarity:", sn.polarity("love")
print "semantics:", ", ".join(sn.semantics("love"))
print "\n".join([key + ": " + str(value) for key, value in sn.sentics("love").items()])
