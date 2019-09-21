def backchain_to_goal_tree(rules, hypothesis):
    tree = OR(hypothesis)
    for rule in rules:
        bindings = match (rule.consequent(), hypothesis)
        if bindings != None:
            newhypothesis = populate(rule.antecedent(), bindings)
            if isinstance(newhypothesis, AND) == True:
                results = []
                for each in newhypothesis:
                    results.append(backchain_to_goal_tree(rules, each))
                tree.append(AND(results))
            elif isinstance(newhypothesis, OR) == True:
                results = []
                for each in newhypothesis:
                    results.append(backchain_to_goal_tree(rules, each))
                tree.append(OR(results))
            else:
                tree.append(backchain_to_goal_tree(rules, newhypothesis))
    return simplify(tree)


def backchain_to_goal_tree(rules, hypothesis):
    """
    Takes a hypothesis (string) and a list of rules (list
    of IF objects), returning an AND/OR tree representing the
    backchain of possible statements we may need to test
    to determine if this hypothesis is reachable or not.

    This method should return an AND/OR tree, that is, an
    AND or OR object, whose constituents are the subgoals that
    need to be tested. The leaves of this tree should be strings
    (possibly with unbound variables), *not* AND or OR objects.
    Make sure to use simplify(...) to flatten trees where appropriate.
    """
    goal_tree = []
    for rule in rules:
        var = match(rule.consequent(),hypothesis)
        if var: 
            sub_hypothesis = populate(rule.antecedent(), var)
            if isinstance(rule.antecedent(), OR):
                sub_tree = [backchain_to_goal_tree(rules, antecedent) for antecedent in sub_hypothesis]
                goal_tree.append(OR(sub_tree))

            elif isinstance(rule.antecedent(), AND):
                sub_tree = [backchain_to_goal_tree(rules, antecedent) for antecedent in sub_hypothesis]
                goal_tree.append(AND(sub_tree))
        
            else:
                goal_tree.append(backchain_to_goal_tree(rules, sub_hypothesis))
    
    return simplify(OR(hypotesis, goal_tree)
