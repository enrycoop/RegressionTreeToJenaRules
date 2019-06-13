from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import numpy as np

def get_rules(tree, feature_names,target):
        left      = tree.tree_.children_left
        right     = tree.tree_.children_right
        threshold = tree.tree_.threshold
        features  = [feature_names[i] for i in tree.tree_.feature]
        value = tree.tree_.value

        def recurse(left, right, threshold, features,target, node,rules):
                stringa = ""
                stringb = ""
                if (threshold[node] != -2):
                        stringa+=("\n(?subject <"+features[node][0]+"> ?"+features[node][1]+") ge( ?"+features[node][1] + ', '+str(threshold[node]) + " )")
                        if left[node] != -1:
                                rulea = recurse (left, right, threshold, features,target,left[node],rules)
                                if len(rulea)==0:
                                        rulea = [stringa]
                                else:
                                        if len(rulea)==1:
                                                rulea[(len(rulea)-1)] = stringa  + ' '+rulea[(len(rulea)-1)]
                                        else:
                                                rulea[(len(rulea)-1)] = stringa  + ', '+rulea[(len(rulea)-1)]

                        stringb+=("\n( ?subject <"+features[node][0]+"> "+features[node][1]+") lessThan( ?"+features[node][1] + ', '+str(threshold[node]) + " )")
                        if right[node] != -1:
                                ruleb = recurse (left, right, threshold, features,target,right[node],rules)
                                if(len(ruleb)==0):
                                        ruleb = [stringb]
                                else:
                                        if len(ruleb)==1:
                                                ruleb[(len(ruleb)-1)] = stringb +' '+ruleb[(len(ruleb)-1)]
                                        else:
                                                ruleb[(len(ruleb)-1)] = stringb +', '+ruleb[(len(ruleb)-1)]
                        return rulea+ruleb
                else:
                        return [("\n->\n (?subject <"+ target +'> '+ str(value[node][0][0]))+')']
                        
        rules = recurse(left, right, threshold, features,target, 0,[])
        frules = []
        i = 0
        for rule in rules:
                frules.append(f'[rule{i}:'+rule+']')
                i+=1
        return frules

def evaluate(X,y,l):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=0)
        print(f"x_train:{len(y_train)}\nx_test:{len(y_test)}")
        for i in range(1,l*4):
                regr = DecisionTreeRegressor(max_depth=i,min_samples_split=0.1,criterion='friedman_mse')
                regr.fit(X_train, y_train)

                r_tests = regr.predict(X_test)
                tot = 0
                for j in range(0,len(r_tests)):
                        tot += (abs(r_tests[j]-y_test[j]))
                tot/=len(r_tests)
                #print(str(i)+";"+str(tot).replace('.',','))
                print(f"mae({i}): {tot}")
        y = np.array(y_test)
        print(f"max: {y.max()} - min: {y.min()} - mean: {y.mean()}")

