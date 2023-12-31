import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def predict_state(file_path, current_indicators, *old_indicators):
    try:
        df = pd.read_csv(file_path)

        data_list = []
        for i in range(14, len(df)):
            t_data = [current_indicators] + list(old_indicators)

            for j in range(14, 0, -1):
                t_data.append(
                    IndicatorData(
                        date=df['date'][i - j],
                        current_price=df['current_price'][i - j],
                        macd_12=df['macd_12'][i - j],
                        macd_26=df['macd_26'][i - j],
                        rsi_6=df['rsi_6'][i - j],
                        ema_100=df['ema_100'][i - j]
                    )
                )

            result = df['Result'][i]
            data_list.append(t_data + [result])

        column_names = ['current_indicators'] + [f'old_indicators{i+1}' for i in range(len(old_indicators))] + [f'IndicatorData(t-{i})' for i in range(14, 0, -1)] + ['Result']
        new_df = pd.DataFrame(data_list, columns=column_names)

        model = RandomForestClassifier()
        predicted_state = model.predict(new_df.iloc[:, :-1])

        return predicted_state[0]

    except Exception as e:
        return None

def test_model(file_path):
    # will be updated
    print("Hello World")