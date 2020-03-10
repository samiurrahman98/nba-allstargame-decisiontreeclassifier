
import sys
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report
import graphviz

def import_data(src):
    data = pd.read_csv(src)
    return data

def get_position(path):
    file_name = path.split('/')[-1]
    return file_name.split('.')[0]

def split_dataset(data):
    num_features = len(data.columns)

    # feature = independent variable
    feature = pd.DataFrame(data.values[:, 1: num_features - 1])
    feature_names = ['Games Played', 'Minutes Played', 'Field Goals Made', 'Field Goals Attempted', 'Field Goal Percentage', 'Three Pointers Made', 'Three Pointers Attempted', 'Three Point Percentage', 'Free Throws Made', 'Free Throws Attempted', 'Free Throw Percentage', 'Offensive Rebounds', 'Defensive Rebounds', 'Total Rebounds', 'Assists', 'Steals', 'Blocks', 'Turnovers', 'Personal Fouls', 'Points', 'Game Score', 'Plus/Minus']

    # target = dependent variable
    target = pd.DataFrame(data.values[:, [num_features - 1]])
    target_names = ['Not selected', 'Selected']

    feature_train, feature_test, target_train, target_test = train_test_split(feature, target, test_size = 0.2, random_state = 100)
    feature_train.fillna(feature_train.mean(), inplace=True)
    feature_test.fillna(feature_test.mean(), inplace=True)
    target_train.fillna(target_train.mean(), inplace=True)
    target_test.fillna(target_test.mean(), inplace=True)
    return feature_names, target_names, feature_train, feature_test, target_train, target_test

'''
gini index: metric to measure how often a randomly chosen element would be incorrectly identified.
any feature attribute with lower gini index should be preferred
'''
def train_gini(feature_train, target_train):
    '''
    create classifier
    can specify max_depth (int, default = none) and min_samples_leaf (int or float, default = 1)
    '''
    clf_gini = tree.DecisionTreeClassifier(criterion='gini', random_state = 100)

    # train
    clf_gini.fit(feature_train, target_train)

    return clf_gini

'''
entropy: measure of uncertainty of a random variable, it characterizes the impurity of an arbitrary collection of examples
the higher the entropy the more the information content
'''
def train_entropy(feature_train, target_train):
    '''
    create classifier
    can specify max_depth (int, default = none) and min_samples_leaf (int or float, default = 1)
    '''
    clf_entropy = tree.DecisionTreeClassifier(criterion='entropy', random_state = 100)

    # train
    clf_entropy.fit(feature_train, target_train)

    return clf_entropy

def model(clf, feature_names, target_names, model_name, model_type):
    data = tree.export_graphviz(clf, out_file = None, feature_names = feature_names, class_names = target_names, filled = True, rounded = True, special_characters = True)
    graph = graphviz.Source(data)
    graph.render(model_name + '-' + model_type)

def prediction(feature_test, clf_obj):
    target_pred = clf_obj.predict(feature_test)
    return target_pred

def calc_accuracy(target_test, target_pred):
    print('Confusion Matrix:')
    print(confusion_matrix(target_test, target_pred))
    print('Accuracy: ',
            accuracy_score(target_test, target_pred))
    print('Report: ')
    target_names = ['Not selected', 'Selected']
    print(classification_report(target_test, target_pred, target_names = target_names))

def main(path):
    # Building Phase
    data = import_data(path)
    feature_names, target_names, feature_train, feature_test, target_train, target_test = split_dataset(data)

    model_name = get_position(path)

    clf_gini = train_gini(feature_train, target_train)
    model(clf_gini, feature_names, target_names, model_name=model_name, model_type = 'Gini')

    clf_entropy = train_entropy(feature_train, target_train)
    model(clf_entropy, feature_names, target_names, model_name=model_name, model_type = 'Entropy')

    # Operational Phase

    # Prediction using Gini
    print('Results using Gini: ')
    target_pred_gini = prediction(feature_test, clf_gini)
    calc_accuracy(target_test, target_pred_gini)

    # Prediction using Entropy
    print('Results using Entropy: ')
    target_pred_entropy = prediction(feature_test, clf_entropy)
    calc_accuracy(target_test, target_pred_entropy)

if __name__ == '__main__':
    main(sys.argv[1])