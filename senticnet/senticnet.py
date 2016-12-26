import importlib

class Senticnet(object):
    """
    Simple API to use Senticnet 4.
    """
    def __init__(self, language="en"):
        data_module = importlib.import_module("senticnet.babel.data_" + language)
        self.data = data_module.senticnet

    # public methods

    def concept(self, concept):
        """
        Return all the information about a concept: semantics,
        sentics and polarity.
        """
        result = {}

        result["polarity_value"] = self.polarity_value(concept)
        result["polarity_intense"] = self.polarity_intense(concept)
        result["moodtags"] = self.moodtags(concept)
        result["sentics"] = self.sentics(concept)
        result["semantics"] = self.semantics(concept)

        return result

    def semantics(self, concept):
        """
        Return the semantics associated with a concept.
        """
        concept = concept.replace(" ", "_")
        concept_info = self.data[concept]

        return concept_info[8:]

    def sentics(self, concept):
        """
        Return sentics of a concept.
        """
        concept = concept.replace(" ", "_")
        concept_info = self.data[concept]

        sentics = {"pleasantness": concept_info[0],
                   "attention": concept_info[1],
                   "sensitivity": concept_info[2],
                   "aptitude": concept_info[3]}

        return sentics

    def polarity_value(self, concept):
        """
        Return the polarity value of a concept.
        """
        concept = concept.replace(" ", "_")
        concept_info = self.data[concept]

        return concept_info[6]

    def polarity_intense(self, concept):
        """
        Return the polarity intense of a concept.
        """
        concept = concept.replace(" ", "_")
        concept_info = self.data[concept]

        return concept_info[7]

    def moodtags(self, concept):
        """
        Return the moodtags of a concept.
        """
        concept = concept.replace(" ", "_")
        concept_info = self.data[concept]

        return concept_info[4:6]
