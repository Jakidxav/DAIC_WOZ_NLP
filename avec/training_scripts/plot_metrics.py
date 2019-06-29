import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

from sklearn.metrics import roc_curve, auc, confusion_matrix


###classification methods

"""
This helper method takes in lists of accuracy, precision, recall, and fbeta score.
It then outputs the mean score for each list.
"""
def report_metrics_binary(acc, pre, rec, fb):
    #calculate means of scores for reporting
    mean_accuracy = np.round(np.mean(acc), 4)
    mean_precision = np.round(np.mean(pre), 4)
    mean_recall = np.round(np.mean(rec), 4)
    mean_fbeta = np.round(np.mean(fb), 4)
    
    print('Mean accuracy score: ', mean_accuracy)
    print('Mean precision score: ', mean_precision)
    print('Mean recall score: ', mean_recall)
    print('Mean fbeta score: ', mean_fbeta)



"""
Plot accuracy, precision, recall, and fbeta score across k-splits to see how they vary.
"""
def plot_metrics_binary(acc, pre, rec, fb):
    plt.plot(acc, label='acc', color='r')

    plt.plot(pre, label='prec', color='g')

    plt.plot(rec, label='rec', color='b')

    plt.plot(fb, label='fb', color='purple')

    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.title('How Metrics Vary Across Stratified Splits')
    plt.show()



"""
Plot the ROC curve, needs false positive and true positive rate arrays as input.
"""
def plot_roc(fpr, tpr):
    #roc curve
    plt.plot([0, 1], [0, 1], 'k--')

    for i, x in enumerate(fpr):
        plt.plot(fpr[i], tpr[i])

    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')

    plt.show()


"""
This method returns the confusion matrix for a given test case.
"""
def plot_cm(ytest, preds, idx):
    cm = confusion_matrix(ytest[idx], preds[idx])
    heatmap = sns.heatmap(cm, annot=True, fmt="d")

    heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), ha='right', fontsize=12)
    heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), ha='right', fontsize=12)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.title('Confusion Matrix for Case {}'.format(idx))
    plt.show()



####regression methods
"""
Plot root mean squared error and r2 score score across k-splits to see how they vary.
"""
def plot_metrics_regress(rmse):
    plt.plot(rmse, label='rmse', color='r')

    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.title('How Regression Metrics Vary Across Stratified Splits')
    
    plt.xlabel('Split Number K')
    plt.ylabel('Root Mean Squared Error')

    plt.show()


