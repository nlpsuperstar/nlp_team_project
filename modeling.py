import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier

from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

def make_predictions(model,train_data,X_test_data,y_train_data):
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(train_data)
    model.fit(vectors, y_train_data)
    vectors_test = vectorizer.transform(X_test_data)
    predictions = model.predict(vectors_test)
    return predictions

def cmatrix(y_true, y_pred):
    '''
    Takes in true and predicted values to create a confusion matrix,
    then ouputs dictionary holding the true pos, true, neg, false pos,
    and false neg rates discerned from the matrix
    Used in conjunction with model_report
    '''

    # define confusion matrix, convert to dataframe
    cmatrix = confusion_matrix(y_true, y_pred)
    cmatrix = pd.DataFrame(confusion_matrix(y_true, y_pred),
                           index=['True Retain', 'True Churn'],
                           columns=['Predict Retain', 'Predict Churn'])
    # assign TN, FN, TP, FP
    true_neg = cmatrix.iloc[0, 0]
    false_neg = cmatrix.iloc[0, 1]
    true_pos = cmatrix.iloc[1, 0]
    false_pos = cmatrix.iloc[1, 1]
    #do math to find rates
    tpr = true_pos / (true_pos + false_neg)
    tnr = true_neg / (true_neg + false_pos)
    fpr = 1 - tnr
    fnr = 1 - tpr
    cmatrix_dict = {'tpr':tpr, 'tnr':tnr, 'fpr':fpr, 'fnr':fnr}

    return cmatrix_dict

def model_report(y_true, y_pred):
    '''
    Takes in true and predicted values to create classificant report
    dictionary and uses cmatrix function to obtain positive and
    negative prediction rates, prints out table containing all metrics
    for the positive class of target
    '''

    # create dictionary for classification report and confusion matrix
    report_dict = classification_report(y_true, y_pred, output_dict=True)
    cmatrix_dict = cmatrix(y_true, y_pred)
    # print formatted table with desired information for model report
    print(f'''
            *** Model  Report ***  
            ---------------------              
 _____________________________________________
|   Positive Case: is javascript = 'true'    |
|   Negative Case: is javascript = 'false'     |
|---------------------------------------------|
|                 Accuracy: {report_dict['accuracy']:>8.2%}          |
|       True Positive Rate: {cmatrix_dict['tpr']:>8.2%}          |
|      False Positive Rate: {cmatrix_dict['fpr']:>8.2%}          |
|       True Negative Rate: {cmatrix_dict['tnr']:>8.2%}          |
|      False Negative Rate: {cmatrix_dict['fnr']:>8.2%}          |
|                Precision: {report_dict['True']['precision']:>8.2%}          |
|                   Recall: {report_dict['True']['recall']:>8.2%}          |
|                 F1-Score: {report_dict['True']['f1-score']:>8.2%}          |
|                                             |
|         Positive Support: {report_dict['True']['support']:>8}          |
|         Negative Support: {report_dict['False']['support']:>8}          |
|            Total Support: {report_dict['macro avg']['support']:>8}          |
|_____________________________________________|
''')
