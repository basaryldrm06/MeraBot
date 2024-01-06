import numpy as np
import pandas as pd
import tensorflow as tf
import warnings

def predict_state_tensorflow(file_path, indicatorDataObj):
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

            # One-hot encode the labels
            y_onehot = tf.keras.utils.to_categorical(y, num_classes=2)

            model = tf.keras.Sequential([
                tf.keras.layers.Dense(64, activation='relu', input_shape=(X.shape[1],)),
                tf.keras.layers.Dense(2, activation='softmax')  # Two classes for binary classification
            ])

            model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
            model.fit(X, y_onehot, epochs=10, batch_size=32, verbose=0)

            features = [indicatorDataObj.date, indicatorDataObj.price, 
                        indicatorDataObj.macd_12, indicatorDataObj.macd_26, 
                        indicatorDataObj.ema_100, indicatorDataObj.rsi_6]
            for bar in indicatorDataObj.bar_list:
                for element in bar: 
                    features.append(element)

            features = np.array([features])

            predicted_prob = model.predict(features)[0, 1]  # Probability for the "LONG" class
            predicted_state = "LONG" if predicted_prob >= 0.5 else "SHORT"

            return predicted_state

    except Exception as e:
        print("Error:", str(e))
        return None
