import rdflib
from rdflib.term import URIRef

class Senticnet(object):
    """
    Ultra simple API to use Senticnet without be bothered by RDF stuff.
    """
    def __init__(self):    
        self.base_url = "http://sentic.net/api/en/concept/"

    def concept(self, concept):
        graph = rdflib.Graph()
        parsed_graph = graph.parse(self.base_url+concept, format="xml")
        result = {}

        result["polarity"] =  self._get_polarity(concept, parsed_graph)
        result["sentics"] = self._get_sentics(concept, parsed_graph)
        result["semantics"] = self._get_semantics(concept, parsed_graph)

        return result

    def polarity(self, concept):
        return self._get_polarity(concept)

    def sentics(self, concept):
        return self._get_sentics(concept)

    def semantics(self, concept):
        return self._get_semantics(concept)

    def _get_semantics(self, concept, parsed_graph=None):
        """Return the semantics associated with the concept"""
        concept_semantics_uri = self.base_url+concept+"/semantics"
        semantics_predicate_uri = "http://sentic.net/api/semantics"

        if parsed_graph is None:
            g = rdflib.Graph()
            parsed_graph = g.parse(concept_semantics_uri, format="xml")

        objects = parsed_graph.objects(predicate=URIRef(semantics_predicate_uri))
        return [self._last_uri_element(o.toPython()) for o in objects]

    def _get_sentics(self, concept, parsed_graph=None):
        """Return sentics of a concept"""
        concept_sentics_uri = self.base_url+concept+"/sentics"
        senticnet_api_url = "http://sentic.net/api/"
        sentics = {"pleasantness" : 0, "attention" : 0, "sensitivity" : 0, "aptitude" : 0}

        if parsed_graph is None:
            graph = rdflib.Graph()
            parsed_graph = graph.parse(concept_sentics_uri, format="xml")

        for sentic in sentics.keys():
            sentics[sentic] = parsed_graph.objects(predicate=URIRef(senticnet_api_url+sentic)).next().toPython()

        return sentics

    def _get_polarity(self, concept, parsed_graph=None):
        """Return the polarity of a concept"""
        concept_polarity_uri = self.base_url+concept+"/polarity"
        senticnet_api_url = "http://sentic.net/api/"
        predicate_uri = senticnet_api_url+"polarity"

        if parsed_graph is None:
            graph = rdflib.Graph()
            parsed_graph = graph.parse(concept_polarity_uri, format="xml")

        return parsed_graph.objects(predicate=URIRef(predicate_uri)).next().toPython()

    def _last_uri_element(self, uri):
        return uri.split("/")[-1]


if __name__ == '__main__':
    sn = Senticnet()
    print sn.concept('love')
    print sn.polarity('love')
    print sn.sentics('love')
    print sn.semantics('love')
