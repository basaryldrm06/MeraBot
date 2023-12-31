import csv

def create_csv_file(file_path):
    # Başlıkları tanımla
    headers = ["state", "price", "macd_12", "macd_26", "ema_100", 
               "rsi_6", "opening_0", "closing_0", "min_0", "max_0",
               "opening_1", "closing_1", "min_1", "max_1", 
               "opening_2", "closing_2", "min_2", "max_2",
               "opening_3", "closing_3", "min_3", "max_3",
               "opening_4", "closing_4", "min_4", "max_4",
               "opening_5", "closing_5", "min_5", "max_5",
               "opening_6", "closing_6", "min_6", "max_6",
               "opening_7", "closing_7", "min_7", "max_7",
               "opening_8", "closing_8", "min_8", "max_8",
               "opening_9", "closing_9", "min_9", "max_9",
               "opening_10", "closing_10", "min_10", "max_10",
               "opening_11", "closing_11", "min_11", "max_11",
               "opening_12", "closing_12", "min_12", "max_12",
               "opening_13", "closing_13", "min_13", "max_13",
               "opening_14", "closing_14", "min_14", "max_14"]

    # CSV dosyasını oluştur ve başlıkları yaz
    with open(file_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(headers)

    print(f"CSV dosyası oluşturuldu: {file_path}")

# CSV dosyasının adını ve yolunu belirtin
csv_file_path = "./data/dataset-mera-1.csv"

# CSV dosyasını oluştur
create_csv_file(csv_file_path)
