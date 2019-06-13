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

    SELECT DISTINCT ?sex ?h ?y ?w
    WHERE { ?x a foaf:Person 
    ; foaf:gender ?sex 
    ; dbpedia:height ?h
    ; dbpedia:weight ?w
    ; prop:years ?y.
    FILTER (langMatches(lang(?sex), "EN"))
    FILTER(datatype(?y) = xsd:integer)
    }
""")

#Converting in a JSON file
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

#[creation of the dataset]
import numpy as np
X = []
y = []
X_void =[]
for result in results["results"]["bindings"]:
    X.append([
        float(result['h']['value']),
    float(result['y']['value'])])
    y.append(float(result['w']['value']))

X = np.array(X)
y = np.array(y)
print(f'total samples downloaded: {len(y)}')
features = [('https://cs.dbpedia.org/ontology/numberOfRooms','R'),
('https://cs.dbpedia.org/ontology/numberOfSuites','S'),('','')]
target = 'https://cs.dbpedia.org/ontology/floorCount'


evaluate(X,y,len(features))
'''
regr = DecisionTreeRegressor(criterion='friedman_mse',max_depth=len(features),min_samples_split=0.1)
regr.fit(X, y)
with open('rules_result.rules','w') as f:
   for rule in get_rules(regr,features,target):
      f.write(rule+'\n\n')
'''