from SPARQLWrapper import SPARQLWrapper, JSON
import pandas
from sklearn.tree import _tree
from utils_tree import *
"""
DESCRIPTION OF TARGET 
"""

#data retrieving from dbpedia

sparql = SPARQLWrapper("http://dbpedia.org/sparql")

#execution of SPARQL query

sparql.setQuery("""
   PREFIX dbpedia: <http://dbpedia.org/ontology/>
   SELECT DISTINCT ?mag ?apoapsis ?periapsis ?escape ?rotPer ?orbitalPer ?albedo ?target
   WHERE{
      ?CelestialBody a dbpedia:Planet.
      ?CelestialBody dbpedia:absoluteMagnitude ?mag.
      ?CelestialBody dbpedia:apoapsis ?apoapsis.
      ?CelestialBody dbpedia:escapeVelocity ?escape.
      ?CelestialBody dbpedia:rotationPeriod ?rotPer.
      ?CelestialBody dbpedia:orbitalPeriod ?orbitalPer.
      ?CelestialBody dbpedia:periapsis ?periapsis.
      ?CelestialBody dbpedia:albedo ?albedo.
      OPTIONAL{
       ?CelestialBody dbpedia:temperature ?target.
      }
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
   
   if 'target' not in result:
      X_void.append([float(result['mag']['value']),float(result['albedo']['value']),float(result['apoapsis']['value']),float(result['periapsis']['value']),float(result['escape']['value']),float(result['rotPer']['value']),float(result['orbitalPer']['value'])])
   else:
      X.append([float(result['mag']['value']),float(result['albedo']['value']),float(result['apoapsis']['value']),float(result['periapsis']['value']),float(result['escape']['value']),float(result['rotPer']['value']),float(result['orbitalPer']['value'])])
      y.append(float(result['target']['value']))
      

X = np.array(X)
y = np.array(y)
print(f'total samples downloaded: {len(y)}')
features = [('dbpedia:absoluteMagnitude','M'),('dbpedia:albedo','L'),('dbpedia:periapsis','P'),('dbpedia:apoapsis','A'),('dbpedia:rotationPeriod','R'),('dbpedia:escapeVelocity','E'),('dbpedia:orbitalPeriod','O')]
target = 'dbpedia:temperature'

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
'''
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=33)

print(f"x_train:{len(y_train)}\nx_test:{len(y_test)}")
for i in range(len(features),len(features)*4):
   regr = DecisionTreeRegressor(max_depth=i,min_samples_split=0.1,criterion='friedman_mse')
   regr.fit(X_train, y_train)

   r_tests = regr.predict(X_test)
   tot = 0
   for j in range(0,len(r_tests)):
      tot += (abs(r_tests[j]-y_test[j]))
   tot/=len(r_tests)
   print(f"mse({i}): {tot}")
y = np.array(y_test)
print(f"max: {y.max()} - min: {y.min()} - mean: {y.mean()}")
'''

regr = DecisionTreeRegressor(criterion='friedman_mse',max_depth=len(features),min_samples_split=0.1)
regr.fit(X, y)
with open('rules_result.rules','w') as f:
   for rule in get_rules(regr,features,target):
      f.write(rule+'\n\n')
