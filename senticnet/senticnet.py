import urllib2
import rdflib
from rdflib.term import URIRef

class Senticnet(object):
    """
    Simple API to use Senticnet 3 without be bothered by RDF stuff.
    """
    def __init__(self):
        self.concept_base_uri = "http://sentic.net/api/en/concept/"
        self.senticapi_base_uri = "http://sentic.net"

    # public methods

    def concept(self, concept):
        """
        Return all the information about a concept: semantics,
        sentics and polarity.
        """
        graph = rdflib.Graph()
        parsed_graph = graph.parse(self.concept_base_uri+concept, format="xml")
        result = {}

        result["polarity"] = self.polarity(concept, parsed_graph)
        result["sentics"] = self.sentics(concept, parsed_graph)
        result["semantics"] = self.semantics(concept, parsed_graph)

        return result

    def semantics(self, concept, parsed_graph=None):
        """
        Return the semantics associated with a concept.
        If you pass a parsed graph, the method do not load the rdf again.
        """
        concept_semantics_uri = self.concept_base_uri+concept+"/semantics"
        semantics_predicate_uri = self.senticapi_base_uri+"semantics"

        if parsed_graph is None:
            g = rdflib.Graph()
            parsed_graph = g.parse(data=self._fix_rdf(concept_semantics_uri), format="xml")

        objects = parsed_graph.objects(predicate=URIRef(semantics_predicate_uri))
        return [self._last_uri_element(o.toPython()) for o in objects]
        
    def sentics(self, concept, parsed_graph=None):
        """
        Return sentics of a concept.
        If you pass a parsed graph, the method do not load the rdf again.
        """
        concept_sentics_uri = self.concept_base_uri+concept+"/sentics"
        sentics = {"pleasantness": 0, "attention": 0, "sensitivity": 0, "aptitude": 0}

        if parsed_graph is None:
            graph = rdflib.Graph()
            parsed_graph = graph.parse(data=self._fix_rdf(concept_sentics_uri), format="xml")

        for sentic in sentics.keys():
            sentics[sentic] = parsed_graph.objects(predicate=URIRef(self.senticapi_base_uri+sentic)).next().toPython()

        return sentics

    def polarity(self, concept, parsed_graph=None):
        """
        Return the polarity of a concept.
        If you pass a parsed graph, the method do not load the rdf again.
        """
        concept_polarity_uri = self.concept_base_uri+concept+"/polarity"
        predicate_uri = self.senticapi_base_uri+"polarity"

        if parsed_graph is None:
            graph = rdflib.Graph()
            parsed_graph = graph.parse(data=self._fix_rdf(concept_polarity_uri), format="xml")

        return parsed_graph.objects(predicate=URIRef(predicate_uri)).next().toPython()

    # private methods

    def _last_uri_element(self, uri):
        return uri.split("/")[-1]

    def _fix_rdf(self, concept_uri):
        return urllib2.urlopen(concept_uri).read().replace('http://w3.org','http://www.w3.org')
