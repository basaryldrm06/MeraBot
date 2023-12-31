import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from sklearn.preprocessing import StandardScaler
import warnings

class SimpleModel(nn.Module):
    def __init__(self, input_size):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(64, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.sigmoid(x)
        return x

def predict_state_pytorch(file_path, indicatorObject):
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

            df = pd.read_csv(file_path)
            columns = []
            for i in range(0, 15):
                columns.extend([
                    f"date_{i}", f"price_{i}",
                    f"macd_{i}_12", f"macd_{i}_26",
                    f"ema_{i}_100", f"rsi_{i}_6"
                ])

            X = df[columns].values

            # Standardize the features
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)

            # Convert NumPy arrays to PyTorch tensors
            X_tensor = torch.tensor(X_scaled, dtype=torch.float32)

            # Build the PyTorch model
            model = SimpleModel(input_size=X.shape[1])

            # Load trained weights if available
            # model.load_state_dict(torch.load('model_weights.pth'))

            # Prepare the features for prediction
            features = []
            for i in range(15): 
                features.append(indicatorObject[i * 15].date)
                features.append(indicatorObject[i * 15].price)
                features.append(indicatorObject[i * 15].macd_12)
                features.append(indicatorObject[i * 15].macd_26)
                features.append(indicatorObject[i * 15].ema_100)
                features.append(indicatorObject[i * 15].rsi_6)

            # Standardize the features for prediction
            features_scaled = scaler.transform([features])
            features_tensor = torch.tensor(features_scaled, dtype=torch.float32)

            # Make predictions
            predicted_prob = model(features_tensor).item()

            # Convert probability to state (assuming a threshold of 0.5)
            predicted_state = 1 if predicted_prob >= 0.5 else 0

            return predicted_state

    except Exception as e:
        print("Error:", str(e))
        return None
