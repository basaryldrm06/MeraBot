import csv

def create_csv_file(file_path):
    header = ["state"]

    # Adding columns for numbers from 1 to 14
    for i in range(0, 15):
        header.extend([
            f"date_{i}", f"price_{i}",
            f"macd_{i}_12", f"macd_{i}_26",
            f"ema_{i}_100", f"rsi_{i}_6"
        ])

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

# Örnek kullanım
csv_file_path = "./data/dataset-mera-2.csv"
create_csv_file(csv_file_path)
print(f"{csv_file_path} oluşturuldu.")