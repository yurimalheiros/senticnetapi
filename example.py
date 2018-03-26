from senticnet.senticnet import SenticNet

sn = SenticNet()
print("polarity value:", sn.polarity_value("love"))
print("polarity intense:", sn.polarity_intense("love"))
print("moodtags:", ", ".join(sn.moodtags("love")))
print("semantics:", ", ".join(sn.semantics("love")))
print("\n".join([key + ": " + str(value) for key, value in sn.sentics("love").items()]))
