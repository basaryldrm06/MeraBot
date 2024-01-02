import numpy as np
import pandas as pd
import tensorflow as tf
import warnings

def predict_state_tensorflow(file_path, date, current_price, macd_12, macd_26, ema_100, rsi_6, list):
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
            y = df['state'].values

            model = tf.keras.Sequential([
                tf.keras.layers.Dense(64, activation='relu', input_shape=(X.shape[1],)),
                tf.keras.layers.Dense(1, activation='sigmoid')
            ])

            model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
            model.fit(X, y, epochs=10, batch_size=32, verbose=0)

            features = [date, current_price, macd_12, macd_26, ema_100, rsi_6]
            for i in range(15): 
                features.append(list[i][0])
                features.append(list[i][1])
                features.append(list[i][2])
                features.append(list[i][3])

            features = np.array([features])

            predicted_prob = model.predict(features)[0, 0]
            predicted_state = "LONG" if predicted_prob >= 0.5 else "SHORT"

            return predicted_state

    except Exception as e:
        print("Error:", str(e))
        return None