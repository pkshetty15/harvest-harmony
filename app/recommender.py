import pickle

# Load the trained model
with open('models/RandomForestClassifier.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('models/cluster_data.pkl', 'rb') as f:
    cluster_data = pickle.load(f)