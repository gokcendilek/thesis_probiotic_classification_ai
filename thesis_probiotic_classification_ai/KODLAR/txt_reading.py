import pandas as pd
import re


file_path = '3b.txt'


with open(file_path, 'r') as file:
    lines = file.readlines()


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
                    data.append([x, y])
            except ValueError:
                
                continue

# DataFrame oluşturma
df = pd.DataFrame(data, columns=["X", "Y"])
df['Date'] = date if date else "Unknown"  
df['Time'] = time if time else "Unknown"  


output_file = 'extracted_data.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df.to_excel(writer, index=False, float_format="%.14E")  # Bilimsel formatı koruma

print(f"Veriler '{output_file}' dosyasına kaydedildi.")
output_file = 'extracted_data.csv'
df.to_csv(output_file, index=False, float_format="%.14E")
