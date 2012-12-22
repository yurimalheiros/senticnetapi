import rdflib

class Senticnet(object):
    """
    Ultra simple API to use Senticnet without be bothered by RDF stuff.
    """
    def __init__(self):    
        graph = rdflib.Graph()
        self.senticnet = graph.parse("senticnet.rdf.xml")

    def get_polarity(self, text):
        """
        Get the polarity of a text using Senticnet. If the word is not defined
        in the Senticnet the function returns zero.
        """
        subject_uri = "http://openmind.media.mit.edu/api/en/concept/%s" % text.replace(" ", "%20")
        polarity_uri = "http://www.semedia.dibet.univpm.it/heo/heo#polarity"

        obj = self.senticnet.value(subject=rdflib.term.URIRef(subject_uri),
                                   predicate=rdflib.term.URIRef(polarity_uri))

        return float(obj.title()) if obj is not None else 0
