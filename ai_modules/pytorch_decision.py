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

def predict_state_pytorch(file_path, date, current_price, macd_12, macd_26, ema_100, rsi_6, list):
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

            df = pd.read_csv(file_path)
            columns = ["date", "price", "macd_12", "macd_26", "ema_100", "rsi_6"]
            for i in range(0, 15):
                columns.extend([
                    f"opening_{i}", f"closing_{i}",
                    f"min_{i}", f"max_{i}"
                ])

            X = df[columns].values

            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)

            X_tensor = torch.tensor(X_scaled, dtype=torch.float32)
            model = SimpleModel(input_size=X.shape[1])

            features = [date, current_price, macd_12, macd_26, ema_100, rsi_6]
            for i in range(15): 
                features.append(list[i][0])
                features.append(list[i][1])
                features.append(list[i][2])
                features.append(list[i][3])

            features_scaled = scaler.transform([features])
            features_tensor = torch.tensor(features_scaled, dtype=torch.float32)

            predicted_prob = model(features_tensor).item()

            predicted_state = "LONG" if predicted_prob >= 0.5 else "SHORT"

            return predicted_state

    except Exception as e:
        print("Error:", str(e))
        return None
