from typing import List, Dict, Tuple, Union
import numpy
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree._tree import Tree


def rules_from_tree(cart, feature_names: list) -> List[Tuple[Dict[str, Tuple[float, float]], int]]:
    """Extract rules from the features of a sklearn.tree.DecisionTreeClassifier.
    Adapted from https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html

    Returns:
        The list of axis-parallel rules encoded by the `cart` Decision Tree
    """
    paths_in_tree = __all_paths(cart.tree_)
    paths_in_tree = list(filter(lambda path: len(path) > 1, paths_in_tree))
    features_per_path = [numpy.array(list(map(lambda node: cart.tree_.feature[abs(node)], path[:-1])))
                          for path in paths_in_tree]
    # features_per_path = [item for sublist in features_per_path for item in sublist]  # flatten list of lists
    thresholds_per_path = [numpy.array(list(map(lambda node: cart.tree_.threshold[abs(node)], path[:-1])))
                            for path in paths_in_tree]
    leaves = [i for i in range(cart.tree_.node_count) if
              cart.tree_.children_left[i] == cart.tree_.children_right[i]]
    labels = {leaf: (cart.tree_.value[leaf][0]).argmax() for leaf in leaves}

    cart_rules = list()
    for signed_features_in_path, thresholds, path in zip(features_per_path, thresholds_per_path, paths_in_tree):
        if abs(path[-1]) not in leaves:
            continue

        rule_premises = {}
        features_in_path = abs(signed_features_in_path)
        rule_label = labels[abs(path[-1])]

        indices_per_feature = {
            feature: numpy.argwhere(features_in_path == feature).flatten()
            for feature in features_in_path
        }
        directions_per_feature = {
            # the sign of a split is given by its child
            f: [numpy.sign(path[k + 1]) for k in indices_per_feature[f] if k < len(path) - 1]
            for f in features_in_path
        }

        for feature in features_in_path:
            if len(indices_per_feature[feature]) == 1:
                threshold = thresholds[indices_per_feature[feature][0]]
                rule_premises[feature_names[feature.item()]] = (-numpy.inf, threshold.item()) if directions_per_feature[feature][0] < 0 \
                                                                               else (threshold.item(), numpy.inf)
            else:
                lower_bounds_idx = [index for index, direction in zip(indices_per_feature[feature],
                                                                      directions_per_feature[feature])
                                    if direction > 0]
                upper_bounds_idx = [index for index, direction in zip(indices_per_feature[feature],
                                                                      directions_per_feature[feature])
                                    if direction < 0]
                lower_bounds, upper_bounds = (
                    numpy.array([thresholds[lower_idx] for lower_idx in lower_bounds_idx]),
                    numpy.array([thresholds[upper_idx] for upper_idx in upper_bounds_idx])
                )

                if lower_bounds.shape[0] > 0 and upper_bounds.shape[0] > 0:
                    rule_premises[feature_names[int(feature.item())]] = (max(lower_bounds).item(), min(upper_bounds).item())
                elif lower_bounds.shape[0] == 0:
                    rule_premises[feature_names[int(feature.item())]] = (-numpy.inf, min(upper_bounds).item())
                elif upper_bounds.shape[0] == 0:
                    rule_premises[feature_names[int(feature.item())]] = (max(lower_bounds).item(), +numpy.inf)

        cart_rules.append((rule_premises, rule_label.item()))

    return cart_rules

def __all_paths(tree: Tree) -> Union[List[Tuple], List[List[int]]]:
    """Retrieve all the possible paths in @tree.

    Arguments:
        tree: The decision tree internals.

    Returns:
        A list of lists of indices:[path_1, path_2, .., path_m] where path_i = [node_1, node_l].
    """
    paths = [[0]]
    left_child = tree.children_left[0]
    right_child = tree.children_right[0]

    if tree.capacity == 1:
        return paths

    paths = paths + \
            __rec_all_paths(tree, right_child, [0], +1) + \
            __rec_all_paths(tree, left_child, [0], -1)
    paths = sorted(set(map(tuple, paths)), key=lambda p: len(p))

    return paths

def __rec_all_paths(tree: Tree, node: int, path: List, direction: int):
    """Recursive call for the @all_paths function.

    Arguments:
        tree: The decision tree internals.
        node: The node whose path to expand.
        path: The path root-> `node`.
        direction:  +1 for right child, -1 for left child. Used to store the actual traversal.

    Returns:
        The enriched path.
    """
    # Leaf
    if tree.children_left[node] == tree.children_right[node]:
        return [path + [node * direction]]
    else:
        path_ = [path + [node * direction]]
        l_child = tree.children_left[node]
        r_child = tree.children_right[node]

        return path_ + \
            __rec_all_paths(tree, r_child, path_[0], +1) + \
            __rec_all_paths(tree, l_child, path_[0], -1)