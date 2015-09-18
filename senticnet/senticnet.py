import rdflib
import urllib2

class Senticnet(object):
    """
    Simple API to use Senticnet 3 without be bothered by RDF stuff.
    """
    def __init__(self):
        self.concept_base_uri = "http://sentic.net/api/en/concept/"
        self.senticapi_base_uri = "http://sentic.net/api"

    # public methods

    def concept(self, concept):
        """
        Return all the information about a concept: semantics,
        sentics and polarity.
        """
        #graph = rdflib.Graph()
        #parsed_graph = graph.parse(self.concept_base_uri+concept, format="xml")
        parsed_graph=None
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
        _,result=self.output(concept_semantics_uri)

        return [str(self._last_uri_element(x)) for x in result]

    def sentics(self, concept, parsed_graph=None):
        """
        Return sentics of a concept.
        If you pass a parsed graph, the method do not load the rdf again.
        """
        concept_sentics_uri = self.concept_base_uri+concept+"/sentics"
        sentics = {"pleasantness": 0, "attention": 0,
                   "sensitivity": 0, "aptitude": 0}

        if parsed_graph is None:
            graph = rdflib.Graph()
            parsed_graph = graph.parse(concept_sentics_uri, format="xml")
        
        result,_=self.output(concept_sentics_uri)

        sentics["pleasantness"]=result[3]
        sentics["attention"]= result[0]
        sentics["sensitivity"]= result[1]
        sentics["aptitude"]=result[2]

        return sentics

    def polarity(self, concept, parsed_graph=None):
        """
        Return the polarity of a concept.
        If you pass a parsed graph, the method do not load the rdf again.
        """
        concept_polarity_uri = self.concept_base_uri+concept+"/polarity"
    
        if parsed_graph is None:
            try:
                graph = rdflib.Graph()
                parsed_graph = graph.parse(concept_polarity_uri, format="xml")
                result,_=self.output(concept_polarity_uri)
                return result[0]
    
            except Exception:
                return 0

    # private methods

    def _last_uri_element(self, uri):
        return uri.split("/")[-1]

    def output(self,url):
        """
        Downloads and returns the output avoiding w3.org error
        """
        response = urllib2.urlopen(url)
        html = response.read()        
        html=html.replace('w3.org','www.w3.org')        
                
        graph = rdflib.Graph()
        parsed_graph = graph.parse(data=html, format="xml")      
        
        result = [];stresult=[]
         
        for s, p, o in parsed_graph:
             if type(o) == rdflib.term.Literal:
                 result.append(o.toPython()) 
             else:
                 stresult.append(o.toPython())
         
        return result,stresult
