from SPARQLWrapper import SPARQLWrapper, JSON
import pandas
from sklearn.tree import _tree
from sklearn import tree
from utils_tree import *

"""
DESCRIPTION OF TARGET 
"""

#data retrieving from dbpedia
sparql = SPARQLWrapper("http://dbpedia.org/sparql")

#execution of SPARQL query
sparql.setQuery("""
   PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>
    PREFIX dbpedia: <http://dbpedia.org/ontology/>
    PREFIX prop: <http://dbpedia.org/property/>

    SELECT DISTINCT ?x ?sex ?h ?target ?y
    WHERE { ?x a foaf:Person .
    ?x foaf:gender ?sex .
    ?x dbpedia:height ?h.
    OPTIONAL{?x dbpedia:weight ?target}
    ?x prop:years ?y.
    FILTER (langMatches(lang(?sex), "EN"))
    FILTER(datatype(?y) = xsd:integer)
    FILTER(datatype(?target) = xsd:double)
    }
""")

#Converting in a JSON file
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

#[creation of the dataset]
import numpy as np
X = []
y = []

i = 0
with open('People.n3','w') as f:
    for result in results["results"]["bindings"]:
        if i<150:
            f.write('<'+result['x']['value']
            +'> <https://cs.dbpedia.org/ontology/height> '
            +result['h']['value']+'.\n')
            f.write('<'+result['x']['value']
            +'> <https://cs.dbpedia.org/property/years> '
            +result['y']['value']+'.\n')
        X.append([
        float(result['h']['value']),
        float(result['y']['value'])])
        y.append(float(result['target']['value']))
        i += 1

X = np.array(X)
y = np.array(y)
print(f'total samples downloaded: {i}')
features = [('https://cs.dbpedia.org/property/years','Y'),('https://cs.dbpedia.org/ontology/height','S')]
target = 'https://cs.dbpedia.org/ontology/weight'

evaluate(X,y,len(X[0]))

regr = DecisionTreeRegressor(criterion='friedman_mse',max_depth=len(features),min_samples_split=0.1)
regr.fit(X, y)
with open('rules_people_weight.rules','w') as f:
   for rule in get_rules(regr,features,target):
      f.write(rule+'\n\n')
