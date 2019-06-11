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
                        stringa+=("\n?subject "+features[node][0]+" ge( ?"+features[node][1] + ', '+str(threshold[node]) + " )")
                        if left[node] != -1:
                                rulea = recurse (left, right, threshold, features,target,left[node],rules)
                                if len(rulea)==0:
                                        rulea = [stringa]
                                else:
                                        if len(rulea)==1:
                                                rulea[(len(rulea)-1)] = stringa  + ' '+rulea[(len(rulea)-1)]
                                        else:
                                                rulea[(len(rulea)-1)] = stringa  + ', '+rulea[(len(rulea)-1)]

                        stringb+=("\n?subject "+features[node][0]+" lessThan( ?"+features[node][1] + ', '+str(threshold[node]) + " )")
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
                        return [("\n->\n (?subject "+ target +' '+ str(value[node][0][0]))+')']
                        
        rules = recurse(left, right, threshold, features,target, 0,[])
        frules = []
        i = 0
        for rule in rules:
                frules.append(f'[r{i}:'+rule+']')
                i+=1
        return frules
