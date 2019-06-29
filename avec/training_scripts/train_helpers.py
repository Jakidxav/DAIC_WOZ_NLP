import pandas as pd
import numpy as np

from sklearn.metrics import fbeta_score, accuracy_score, precision_score, recall_score
from sklearn.metrics import roc_curve, auc, confusion_matrix
from sklearn.metrics import mean_squared_error, r2_score


###classification methods

"""
classify_and_report() creates lists for accuracy, precision, recall, and fbeta score.
It also creates lists for false positive and true positive rates.
Given a sklearn model, the training and development sets, it creates k-fold training and dev sets.
The model is trained, and then metrics are reported and all lists are returned for further analysis.
"""
def classify_and_report(model, Xt, yt, Xd, yd, num):
    
    #for reporting metrics
    accuracy, precision, recall, fbeta = [], [], [], []

    #for roc curve
    fpr, tpr, threshold = [], [], []

    #for confusion matrix
    predictions = []
    ytest = []

    #shuffle indices of training and dev sets, get data splits
    X_train_list, y_train_list, X_test_list, y_test_list = shuffle_indices(Xt, yt, Xd, yd, num)

    #loop over n splits
    for i in range(num):
        #access lists that are holding our data subsets
        X_train, X_test = X_train_list[i], X_test_list[i]
        y_train, y_test = y_train_list[i], y_test_list[i]
    
        ytest.append(y_test)
    
        #fit and predict on training and test data
        preds = model.fit(X_train, y_train).predict(X_test)
        predictions.append(preds)
    
        #calculate scores and append to lists
        acc = accuracy_score(y_test, preds)
        accuracy.append(acc)
    
        pre = precision_score(y_test, preds)
        precision.append(pre)
    
        rec = recall_score(y_test, preds)
        recall.append(rec)
    
        fb = fbeta_score(y_test, preds, 0.5)
        fbeta.append(fb)
    
        #append false positive rate, true positive rate, and threshold values for roc curve
        fpr_roc, tpr_roc, thresh = roc_curve(y_test, preds)
        fpr.append(fpr_roc)
        tpr.append(tpr_roc)
        threshold.append(thresh)
        
        
    report_metrics_binary(accuracy, precision, recall, fbeta)
        
    return accuracy, precision, recall, fbeta, fpr, tpr, ytest, predictions



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


####regression methods

"""
regress_and_report() creates lists for root mean squared error and r2 score.
Given a sklearn model, the X and y data sets, it creates k-fold training and dev sets.
The model is trained, and then metrics are reported and all lists are returned for further analysis.
"""
def regress_and_report(model, Xt, yt, Xd, yd, num):
    #for reporting metrics
    mse, r2 = [], []

    #for confusion matrix
    predictions = []
    ytest = []

    #shuffle indices of training and dev sets, get data splits
    X_train_list, y_train_list, X_test_list, y_test_list = shuffle_indices(Xt, yt, Xd, yd, num)

    #loop over n splits
    for i in range(num):
        #access lists that are holding our data subsets
        X_train, X_test = X_train_list[i], X_test_list[i]
        y_train, y_test = y_train_list[i], y_test_list[i]
    
        ytest.append(y_test)
    
        #fit and predict on training and test data
        preds = model.fit(X_train, y_train).predict(X_test)
        predictions.append(preds)
    
        #calculate scores and append to lists
        mse_ = mean_squared_error(y_test, preds)
        mse.append(mse_)
    
        r2_ = r2_score(y_test, preds)
        r2.append(r2_)
        
    
    rmse = np.sqrt(mse)
    
    report_metrics_regress(rmse, r2)
        
    return rmse, r2, ytest, predictions



"""
This helper method takes in lists of root mean squared error and r2 score
It then outputs the mean score for each list.
"""
def report_metrics_regress(rmse, r2):
    #calculate means of scores for reporting
    mean_rmse = np.round(np.mean(rmse), 4)
    mean_r2 = np.round(np.mean(r2), 4)
    
    print('Mean rmse score: ', mean_rmse)
    print('Mean r2 score: ', mean_r2)



"""
Since we have pre-defined training and development sets, we can define our own cross-validation method. 4
This method is used by both the classification and regression training methods.
"""
def shuffle_indices(Xt, yt, Xd, yd, num):
    #lists that will hold our data splits
    Xt_list, yt_list, Xd_list, yd_list = [], [], [], []

    #get the indices of the training and dev set word embeddings
    indices_train = np.arange(len(Xt))
    indices_dev = np.arange(len(Xd))

    #now shuffle the indices
    np.random.shuffle(indices_train)
    np.random.shuffle(indices_dev)

    #loop over n splits
    for i in range(num):
        #get subsets of indices, stride by the number of folds
        idx_train = indices_train[i::num]
        idx_dev = indices_dev[i::num]

        X_train, X_dev = Xt[idx_train], Xd[idx_dev]
        y_train, y_dev = yt[idx_train], yd[idx_dev]

        Xt_list.append(X_train)
        yt_list.append(y_train)
        Xd_list.append(X_dev)
        yd_list.append(y_dev)

    return Xt_list, yt_list, Xd_list, yd_list


