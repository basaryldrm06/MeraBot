import numpy as np
import pandas as pd
import tensorflow as tf
import warnings

def predict_state_tensorflow(file_path, indicatorObject):
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
            y = df['state'].values

            # Define a simple neural network model
            model = tf.keras.Sequential([
                tf.keras.layers.Dense(64, activation='relu', input_shape=(X.shape[1],)),
                tf.keras.layers.Dense(1, activation='sigmoid')
            ])

            # Compile the model
            model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

            # Train the model
            model.fit(X, y, epochs=10, batch_size=32, verbose=0)

            # Prepare the features for prediction
            features = []
            for i in range(15): 
                features.append(indicatorObject[i * 15].date)
                features.append(indicatorObject[i * 15].price)
                features.append(indicatorObject[i * 15].macd_12)
                features.append(indicatorObject[i * 15].macd_26)
                features.append(indicatorObject[i * 15].ema_100)
                features.append(indicatorObject[i * 15].rsi_6)

            # Convert features to NumPy array
            features = np.array([features])

            # Make predictions
            predicted_prob = model.predict(features)[0, 0]

            # Convert probability to state (assuming a threshold of 0.5)
            predicted_state = 1 if predicted_prob >= 0.5 else 0

            return predicted_state

    except Exception as e:
        print("Error:", str(e))
        return None