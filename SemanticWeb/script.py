from SPARQLWrapper import SPARQLWrapper, JSON
import pandas
from sklearn.tree import _tree
from sklearn import tree
from utils_tree import *
from sklearn.externals.six import StringIO  
import pydotplus
from IPython.display import Image 



"""
DESCRIPTION OF TARGET 
"""

#data retrieving from dbpedia

sparql = SPARQLWrapper("http://dbpedia.org/sparql")

#execution of SPARQL query

sparql.setQuery("""
   PREFIX dbpedia: <http://dbpedia.org/ontology/>
   SELECT DISTINCT ?CelestialBody ?mag ?apoapsis ?periapsis ?escape ?rotPer ?orbitalPer ?albedo ?target
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
with open('Planets.n3','w') as f:
   for result in results["results"]["bindings"]:
      
      if 'target' not in result:
         f.write('<'+result['CelestialBody']['value']
         +'> <https://cs.dbpedia.org/ontology/Planet/absoluteMagnitude> '
          +result['mag']['value']+'.\n')
         f.write('<'+result['CelestialBody']['value']
         +'> <https://cs.dbpedia.org/ontology/Planet/apoapsis> '
         +result['apoapsis']['value']+'.\n')
         f.write('<'+result['CelestialBody']['value']
         +'> <https://cs.dbpedia.org/ontology/Planet/escapeVelocity> '
          +result['escape']['value']+'.\n')
         f.write('<'+result['CelestialBody']['value']
         +'> <https://cs.dbpedia.org/ontology/Planet/rotationPeriod> ' 
         +result['rotPer']['value']+'.\n')
         f.write('<'+result['CelestialBody']['value']
         +'> <https://cs.dbpedia.org/ontology/Planet/orbitalPeriod> '
          +result['orbitalPer']['value']+'.\n')
         f.write('<'+result['CelestialBody']['value']
         +'> <https://cs.dbpedia.org/ontology/Planet/periapsis> '
          +result['periapsis']['value']+'.\n')
         f.write('<'+result['CelestialBody']['value']
         +'> <https://cs.dbpedia.org/ontology/Planet/albedo> '
          +result['albedo']['value']+'.\n')
      else:
         X.append([float(result['mag']['value']),
         float(result['albedo']['value']),
         float(result['apoapsis']['value']),
         float(result['periapsis']['value']),
         float(result['escape']['value']),
         float(result['rotPer']['value']),
         float(result['orbitalPer']['value'])])
         y.append(float(result['target']['value']))
      

X = np.array(X)
y = np.array(y)
print(f'total samples downloaded: {len(y)}')
features = [('https://cs.dbpedia.org/ontology/Planet/absoluteMagnitude','M'),('https://cs.dbpedia.org/ontology/Planet/albedo','L'),('https://cs.dbpedia.org/ontology/Planet/periapsis','P'),('https://cs.dbpedia.org/ontology/Planet/apoapsis','A'),('https://cs.dbpedia.org/ontology/Planet/rotationPeriod','R'),('https://cs.dbpedia.org/ontology/Planet/escapeVelocity','E'),('https://cs.dbpedia.org/ontology/Planet/orbitalPeriod','O')]
target = 'https://cs.dbpedia.org/ontology/Planet/temperature'


#
# evaluate(X,y,features)

regr = DecisionTreeRegressor(criterion='friedman_mse',max_depth=len(features),min_samples_split=0.1)
regr.fit(X, y)
with open('rules_result.rules','w') as f:
   for rule in get_rules(regr,features,target):
      f.write(rule+'\n\n')

from subprocess import call
dot_file = "tree.dot"
with open(dot_file, 'w') as f:
    tree.export_graphviz(regr, out_file=f) 
call(['python','C:\\Users\\enric\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\graphviz\\dot.py', '-Tpdf', dot_file, '-o', "tree.pdf"])
