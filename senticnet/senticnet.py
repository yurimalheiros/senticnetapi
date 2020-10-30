from senticnet import senticnet6

class SenticNet(object):
    """
    Simple API to use SenticNet.
    """
    def __init__(self):
        self.data = senticnet6.senticnet

    # public methods

    def concept(self, concept):
        """
        Return all the information about a concept: polarity, sentics, moodtags, and semantics.
        """
        result = {}

        result["polarity_label"] = self.polarity_label(concept)
        result["polarity_value"] = self.polarity_value(concept)
        result["sentics"] = self.sentics(concept)
        result["moodtags"] = self.moodtags(concept)
        result["semantics"] = self.semantics(concept)

        return result

    def sentics(self, concept):
        """
        Return the sentics of a concept.
        """
        concept = concept.replace(" ", "_")
        concept_info = self.data[concept]

        sentics = {"introspection": concept_info[0],
                   "temper": concept_info[1],
                   "attitude": concept_info[2],
                   "sensitivity": concept_info[3]}

        return sentics

    def moodtags(self, concept):
        """
        Return the moodtags of a concept.
        """
        concept = concept.replace(" ", "_")
        concept_info = self.data[concept]

        return concept_info[4:6]

    def polarity_label(self, concept):
        """
        Return the polarity label of a concept.
        """
        concept = concept.replace(" ", "_")
        concept_info = self.data[concept]

        return concept_info[6]

    def polarity_value(self, concept):
        """
        Return the polarity value of a concept.
        """
        concept = concept.replace(" ", "_")
        concept_info = self.data[concept]

        return concept_info[7]

    def semantics(self, concept):
        """
        Return the semantics associated with a concept.
        """
        concept = concept.replace(" ", "_")
        concept_info = self.data[concept]

        return concept_info[8:]
