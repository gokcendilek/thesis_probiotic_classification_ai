import pandas as pd
import re
import os


folder_path = '/Users/gokcendilekalak/Desktop/tez_proje/Enterococcus_Faecium'  
output_excel = 'Enterococcus_Faecium.xlsx'  
output_csv = 'Enterococcus_Faecium.csv'  


all_data = []


for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Tarih ve saat bilgilerini bulma
        date = None
        time = None
        data = []

        # Tarih ve saat bilgilerini satır satır arayalım
        for line in lines:
            if re.match(r"\d{1,2}\.\d{1,2}\.\d{4}", line.strip()):  # Tarih formatı: DD.MM.YYYY
                date = line.strip()
            if re.match(r"\d{1,2}:\d{2}", line.strip()):  # Saat formatı: HH:MM
                time = line.strip()

        # x ve y verilerini bulma
        for i, line in enumerate(lines):
            if "_x\t_y" in line:  # Verilerin başladığı yer
                start_index = i + 2  # "_x\t_y" satırından 2 satır aşağıda
                for data_line in lines[start_index:]:
                    try:
                        parts = data_line.split()
                        if len(parts) == 2:  # İki kolonlu satırlar
                            x = float(parts[0])
                            y = float(parts[1])
                            data.append([file_name, date, time, x, y])
                    except ValueError:
                        # Sayısal olmayan satırları atla
                        continue

        # Tüm verileri listeye ekle
        all_data.extend(data)

# DataFrame oluşturma
df = pd.DataFrame(all_data, columns=["File Name", "Date", "Time", "X", "Y"])

# Excel ve CSV dosyasına kaydetme
with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
    df.to_excel(writer, index=False, float_format="%.14E")  # Bilimsel format
print(f"Veriler '{output_excel}' dosyasına kaydedildi.")

df.to_csv(output_csv, index=False, float_format="%.14E")  # CSV formatı
print(f"Veriler '{output_csv}' dosyasına kaydedildi.")
