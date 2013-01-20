import rdflib
from rdflib.term import URIRef

class Senticnet(object):
    """
    Ultra simple API to use Senticnet without be bothered by RDF stuff.
    """
    def __init__(self):    
        self.concept_base_uri = "http://sentic.net/api/en/concept/"
        self.senticapi_base_uri = "http://sentic.net/api/"

    # public methods

    def concept(self, concept):
        graph = rdflib.Graph()
        parsed_graph = graph.parse(self.concept_base_uri+concept, format="xml")
        result = {}

        result["polarity"] = self._get_polarity(concept, parsed_graph)
        result["sentics"] = self._get_sentics(concept, parsed_graph)
        result["semantics"] = self._get_semantics(concept, parsed_graph)

        return result

    def polarity(self, concept):
        return self._get_polarity(concept)

    def sentics(self, concept):
        return self._get_sentics(concept)

    def semantics(self, concept):
        return self._get_semantics(concept)

    # private methods

    def _get_semantics(self, concept, parsed_graph=None):
        """Return the semantics associated with the concept"""
        concept_semantics_uri = self.concept_base_uri+concept+"/semantics"
        semantics_predicate_uri = self.senticapi_base_uri+"semantics"

        if parsed_graph is None:
            g = rdflib.Graph()
            parsed_graph = g.parse(concept_semantics_uri, format="xml")

        objects = parsed_graph.objects(predicate=URIRef(semantics_predicate_uri))
        return [self._last_uri_element(o.toPython()) for o in objects]

    def _get_sentics(self, concept, parsed_graph=None):
        """Return sentics of a concept"""
        concept_sentics_uri = self.concept_base_uri+concept+"/sentics"
        sentics = {"pleasantness" : 0, "attention" : 0, "sensitivity" : 0, "aptitude" : 0}

        if parsed_graph is None:
            graph = rdflib.Graph()
            parsed_graph = graph.parse(concept_sentics_uri, format="xml")

        for sentic in sentics.keys():
            sentics[sentic] = parsed_graph.objects(predicate=URIRef(self.senticapi_base_uri+sentic)).next().toPython()

        return sentics

    def _get_polarity(self, concept, parsed_graph=None):
        """Return the polarity of a concept"""
        concept_polarity_uri = self.concept_base_uri+concept+"/polarity"
        predicate_uri = self.senticapi_base_uri+"polarity"

        if parsed_graph is None:
            graph = rdflib.Graph()
            parsed_graph = graph.parse(concept_polarity_uri, format="xml")

        return parsed_graph.objects(predicate=URIRef(predicate_uri)).next().toPython()

    def _last_uri_element(self, uri):
        return uri.split("/")[-1]

