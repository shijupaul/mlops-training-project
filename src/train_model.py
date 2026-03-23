import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def load_dataset(file_path) :
    return pd.read_csv(file_path)

def preprocess_data(df) :
    # machine_id is an identifier and does not contribute to the prediction, so we drop it
    df.drop('machine_id', axis = 1, inplace = True)
    
    correlation = df.corr()['failure'].sort_values(ascending = False)
    print(correlation)

    # Index(['failure', 'maintenance_history', 'temperature', 'vibration', 'runtime_hours'], dtype='str')
    important_features = correlation[abs(correlation) > 0.1].index
    print("Important features:\n", important_features)

    return df[important_features]

def train_model(classifier, X_train, y_train) :
    classifier.fit(X_train, y_train)
    return classifier

def predict_model(classifier, X_test) :
    return classifier.predict(X_test)

def print_metrics(y_test, y_pred) :
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))
    print("F1 Score:", f1_score(y_test, y_pred))

def get_model(file_path) :
    df = load_dataset(file_path)
    df = preprocess_data(df)
    
    X = df.loc[:, df.columns != 'failure']
    y = df['failure']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)
    classifier = RandomForestClassifier(n_estimators = 50, criterion = 'entropy', random_state = 0) 
    train_model(classifier, X_train, y_train)
    
    y_pred = predict_model(classifier, X_test)
    print_metrics(y_test, y_pred)

    return classifier



classifier = get_model('data/machine_failure_train.csv')    