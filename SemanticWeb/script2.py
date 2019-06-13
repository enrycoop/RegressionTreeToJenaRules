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
   PREFIX dbpedia: <http://dbpedia.org/ontology/>
   SELECT DISTINCT ?HOTEL ?target ?rooms ?suites
   WHERE{
      ?HOTEL a dbpedia:Hotel.
      OPTIONAL{?HOTEL dbpedia:floorCount ?target.}
      ?HOTEL dbpedia:numberOfRooms ?rooms.
      ?HOTEL dbpedia:numberOfSuites ?suites.
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
with open('Hotels.n3','w') as f:
   for result in results["results"]["bindings"]:
      if 'target' not in result:
          """
         f.write('<'+result['HOTEL']['value']
         +'> <https://cs.dbpedia.org/ontology/numberOfRooms> '
          +result['rooms']['value']+'.\n')
         f.write('<'+result['HOTEL']['value']
         +'> <https://cs.dbpedia.org/ontology/numberOfSuites> '
         +result['suites']['value']+'.\n')
         """
      else:
         X.append([
         int(result['target']['value']),
         int(result['suites']['value'])])
         y.append(int(result['rooms']['value']))

X = np.array(X)
y = np.array(y)
print(f'total samples downloaded: {len(y)}')
features = [('https://cs.dbpedia.org/ontology/numberOfRooms','R'),
('https://cs.dbpedia.org/ontology/numberOfSuites','S')]
target = 'https://cs.dbpedia.org/ontology/floorCount'


evaluate(X,y,len(features))
'''
regr = DecisionTreeRegressor(criterion='friedman_mse',max_depth=len(features),min_samples_split=0.1)
regr.fit(X, y)
with open('rules_result.rules','w') as f:
   for rule in get_rules(regr,features,target):
      f.write(rule+'\n\n')
'''