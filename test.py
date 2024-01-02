import csv

def create_csv_file(file_path):
    header = ["state", "date", "price", "macd_12", "macd_26", "ema_100", "rsi_6"]

    # Adding columns for numbers from 1 to 14
    for i in range(0, 15):
        header.extend([
            f"opening_{i}", f"closing_{i}",
            f"min_{i}_12", f"max_{i}_26"
        ])

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

# Örnek kullanım
csv_file_path = "./data/dataset-mera-2.csv"
create_csv_file(csv_file_path)
print(f"{csv_file_path} oluşturuldu.")