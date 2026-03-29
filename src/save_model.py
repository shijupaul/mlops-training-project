import joblib
from train_model import get_model

def save_model(model, filename):
    joblib.dump(model, filename)
    print(f"Model saved to {filename}")

model = get_model('data/machine_failure_train.csv')
save_model(model, 'models/rf_model.pkl')

# apprunner to push the cloud ??
