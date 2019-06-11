from SPARQLWrapper import SPARQLWrapper, JSON
import pandas
from sklearn.tree import _tree
from utils_tree import *

#data retrieving from dbpedia

sparql = SPARQLWrapper("http://dbpedia.org/sparql")

#execution of SPARQL query

sparql.setQuery("""
   PREFIX dbpedia: <http://dbpedia.org/ontology/>
   SELECT DISTINCT ?mag ?apoapsis ?escape ?rotPer
   WHERE{
      ?CelestialBody a dbpedia:Planet.
      ?CelestialBody dbpedia:absoluteMagnitude ?mag.
      ?CelestialBody dbpedia:apoapsis ?apoapsis.
      ?CelestialBody dbpedia:escapeVelocity ?escape.
      ?CelestialBody dbpedia:rotationPeriod ?rotPer.
   } 
""")

#Converting in a JSON file
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

#now I'll create the dataset
#['mag']['value']
#['apoapsis']['value']
#['rotPer']['value']
#['escape']['value']

import numpy as np

X = []
y = []
for result in results["results"]["bindings"]:
   X.append([float(result['apoapsis']['value']),float(result['rotPer']['value']),float(result['escape']['value'])])
   y.append(float(result['mag']['value']))
X = np.array(X)
y = np.array(y)
features = [('dbpedia:apoapsis','A'),('dbpedia:rotationPeriod','R'),('dbpedia:escapeVelocity','E')]
target = 'dbpedia:absoluteMagnitude'
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

regr = DecisionTreeRegressor(max_depth=len(features)*2)
regr.fit(X, y)

print(regr.predict([[3.699, 4.66236e+05,6000]]))


with open('rules_result.rules','w') as f:
   for rule in get_rules(regr,features,target):
      f.write(rule+'\n\n')
         
