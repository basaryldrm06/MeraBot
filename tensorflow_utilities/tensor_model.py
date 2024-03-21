import tensorflow as tf
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, BatchNormalization, LeakyReLU
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
import numpy as np

class TensorModel:
    def __init__(self, file_path):
        
        df = pd.read_csv(file_path)
        if df.empty:
            raise ValueError("No data in csv file")

        self.columns = ["price", "macd_12", "macd_26", "ema_100", "rsi_6"]
        
        self.X = df[self.columns].values
        y = df['state'].values
        self.y = np.where(y == 'LONG', 1, 0)

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.1, random_state=42)

        self.model = Sequential([
            Dense(256, input_dim=self.X.shape[1]),
            LeakyReLU(alpha=0.01),
            BatchNormalization(),
            Dense(128),
            LeakyReLU(alpha=0.01),
            BatchNormalization(),
            Dense(64),
            LeakyReLU(alpha=0.01),
            BatchNormalization(),
            Dense(32),
            LeakyReLU(alpha=0.01),
            BatchNormalization(),
            Dense(2, activation='softmax')
        ])

        optimizer = Adam(learning_rate=0.01)
        self.model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        self.model.fit(self.X_train, self.y_train, epochs=32, batch_size=1, validation_split=0.2, verbose=0)
    
    def getAccuracy(self):
        _, test_acc = self.model.evaluate(self.X_test, self.y_test, verbose=0)
        return test_acc
    
    def predictResult(self, data_obj):
        features = [float(data_obj.price),
                    float(data_obj.macd_12), float(data_obj.macd_26),
                    float(data_obj.ema_100), float(data_obj.rsi_6)]

        new_data = np.array([features])

        prediction_probs = self.model.predict(new_data, verbose=0)
        predicted_class_index = np.argmax(prediction_probs, axis=1)[0]  # [0] ile tek bir tahmin için ilk sonucu al

        prediction = "LONG" if predicted_class_index == 0 else "SHORT"

        return prediction
    
    def process_model(self, data_obj):
        accuracy = self.getAccuracy()
        prediction = self.predictResult(data_obj)
        return accuracy, prediction

    