import data


class Senticnet(object):
    """
    Simple API to use Senticnet 4.
    """
    def __init__(self):
        self.data = data.senticnet

    # public methods

    def concept(self, concept):
        """
        Return all the information about a concept: semantics,
        sentics and polarity.
        """
        result = {}

        result["polarity"] = self.polarity(concept)
        result["sentics"] = self.sentics(concept)
        result["semantics"] = self.semantics(concept)

        return result

    def semantics(self, concept):
        """
        Return the semantics associated with a concept.
        """
        concept = concept.replace(" ", "_")
        concept_info = self.data[concept]

        return concept_info[7:]

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

    def polarity(self, concept):
        """
        Return the polarity of a concept.
        """
        concept = concept.replace(" ", "_")
        concept_info = self.data[concept]

        return concept_info[6]
