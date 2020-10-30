from senticnet.senticnet import SenticNet
from senticnet.babelsenticnet import BabelSenticNet

print("Concept: 'love'")
sn = SenticNet()
print("polarity value:", sn.polarity_label("love"))
print("polarity intense:", sn.polarity_value("love"))
print("moodtags:", ", ".join(sn.moodtags("love")))
print("semantics:", ", ".join(sn.semantics("love")))
print("\n".join([key + ": " + str(value) for key, value in sn.sentics("love").items()]))

print("\n---------------------------------------------\n")

print("Concept: 'amor'")
bsn = BabelSenticNet("pt")
print("polarity value:", bsn.polarity_label("amor"))
print("polarity intense:", bsn.polarity_value("amor"))
print("moodtags:", ", ".join(bsn.moodtags("amor")))
print("semantics:", ", ".join(bsn.semantics("amor")))
print("\n".join([key + ": " + str(value) for key, value in bsn.sentics("amor").items()]))
