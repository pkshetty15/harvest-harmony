import pickle

# Load the trained model
with open('models/RandomForestClassifier.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('models/cluster_data.pkl', 'rb') as f:
    cluster_data = pickle.load(f)

def predict_crops(soil_data):
    sample = model.predict(scaler.transform([soil_data]))
    crops = cluster_data.loc[cluster_data['cluster'] == sample[0], 'label'].values
    return set(crops)
