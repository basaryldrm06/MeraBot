import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import warnings

def predict_state_scikit(file_path, date, current_price, macd_12, macd_26, ema_100, rsi_6, list):
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

            X = df[columns]
            y = df['state']

            clf = RandomForestClassifier()
            clf.fit(X, y)

            features = [date, current_price, macd_12, macd_26, ema_100, rsi_6]
            for i in range(15): 
                features.append(list[i][0])
                features.append(list[i][1])
                features.append(list[i][2])
                features.append(list[i][3])
                
            predicted_state = clf.predict(features)

            return predicted_state[0]

    except Exception as e:
        print("Hata:", str(e))
        return None

# TODO: Update here
def test_model(file_path):
    try:
        df = pd.read_csv(file_path)
        
        columns = []
        for i in range(0, 15):
            columns.extend([
                f"date_{i}", f"price_{i}",
                f"macd_{i}_12", f"macd_{i}_26",
                f"ema_{i}_100", f"rsi_{i}_6"
            ])
        
        X = df[columns]
        y = df['state']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        clf = RandomForestClassifier()
        clf.fit(X_train, y_train)

        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        return  "%" + str(accuracy * 100)

    except Exception as e:
        return "Hata:"+ str(e)