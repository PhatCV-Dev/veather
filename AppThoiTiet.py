import requests
import time, sys
#Khai bao mau
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"  
GRAY = "\033[90m"
BOLD = "\033[1m"
RESET = "\033[0m"
import time, sys

spinners = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
start_time = time.time()
i = 0

while time.time() - start_time < 5:  # Chạy tròn 5 giây
    char = spinners[i % len(spinners)]
    sys.stdout.write(f"\r{CYAN}▌{RESET} {BOLD}Dang tai du lieu...{RESET} {YELLOW}{char}{RESET}")
    sys.stdout.flush()
    time.sleep(0.08)
    i += 1

# Xoá dòng load để in ra kết quả cho sạch màn hình
print("\r" + " " * 60 + "\r", end="")
tinh_nguyco = {
    "dak lak": "Buon Ma Thuot", "đắk lắk": "Buon Ma Thuot", "daklak": "Buon Ma Thuot",
    "dak nong": "Gia Nghia", "đắk nông": "Gia Nghia",
    "lam dong": "Da Lat", "lâm đồng": "Da Lat",
    "gia lai": "Pleiku",
    "kien giang": "Rach Gia", "kiên giang": "Rach Gia",
    "an giang": "Long Xuyen",
    "binh thuan": "Phan Thiet", "bình thuận": "Phan Thiet",
    "ninh thuan": "Phan Rang", "ninh thuận": "Phan Rang",
    "ba ria vung tau": "Vung Tau", "vung tau": "Vung Tau",
    "tphcm": "Ho Chi Minh", "hcm": "Ho Chi Minh", "sai gon": "Saigon",
    "thua thien hue": "Hue", "hue": "Hue"
#Logo 
}
def tao_logo(text):
    lines = text.strip("\n").split("\n")
    total_lines = len(lines)
    for i, line in enumerate(lines):
    
        r = int(255 - (255 * (i / max(1, total_lines - 1))))
        g = int(230 - (30 * (i / max(1, total_lines - 1))))
        b = int(50 + (205 * (i / max(1, total_lines - 1))))
        
        ansi_color = f"\033[38;2;{r};{g};{b}m"
        print(f"{ansi_color}{line}\033[0m")
LOGO = r"""
 __      __           _   _                 
 \ \    / /          | | | |                
  \ \  / /___  __ _  | |_| |__   ___ _ __   
   \ \/ // _ \/ _` | | __| '_ \ / _ \ '__|  
    \  /|  __/ (_| | | |_| | | |  __/ |     
     \/  \___|\__,_|  \__|_| |_|\___|_|  v1.0
==============================================
"""
tao_logo(LOGO)


#Input

    #Khai bao Api va thuc hien input
api = "13499aea6e1827cc5ef89733cf310a16"
thanh_pho = input(f"\n{CYAN}▌{RESET} {BOLD}Nhap ten Thanh Pho{RESET} {GRAY}»{RESET} ")
text_thanhpho = thanh_pho.title()
thanh_pho = thanh_pho.lower()
thanh_pho = tinh_nguyco.get(thanh_pho, thanh_pho)
url = f"https://api.openweathermap.org/data/2.5/weather?q={thanh_pho}&appid={api}&units=metric&lang=vi"
    #Du lieu
data = requests.get(url).json()
if data.get("cod") == 200:
    lat = data['coord']['lat']
    lon = data['coord']['lon']
    pollution = requests.get(f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api}").json()
    chi_so_aqi = pollution['list'][0]['main']['aqi'] # 1: Tot, 5: Nguy hiem
    comp = pollution['list'][0]['components']
    chi_so_pm2_5 = pollution['list'][0]['components']['pm2_5']
    stats = ""
    def chamdiemchiso(aqi):
        if aqi == 1:
            stats = "Tot"
        elif aqi == 2:
            stats = "Kha"
        elif aqi == 3:
            stats = "Trung binh"
        elif aqi == 4:
            stats = "Kem"
        else:
            stats = "Nguy hai"
        return stats
    stats = chamdiemchiso(chi_so_aqi)
    #Output
    print()

    print(f"\n{BLUE}─────────── THOI TIET : {text_thanhpho} ─────────── {RESET}")
    print()
    print(f"{BOLD}{YELLOW}Thoi tiet{RESET}")
    print("Thoi tiet:", data['weather'][0]['description'])
    print("Nhiet do: ", data['main']['temp'], "C")
    print("Do am:    ", data['main']['humidity'], "%")
    print("Suc gio:  ", data['wind']['speed'], "m/s")

    print(f"\n{BOLD}{GREEN}Bui min{RESET}")
    print(f"AQI: {chi_so_aqi}, Chi so: {stats}")
    print(f"Bui min PM2.5: {chi_so_pm2_5} ug/m3")
    print(f"Bui to PM10:  {comp['pm10']} ug/m3")
    print(f"Khi CO:       {comp['co']} ug/m3 ")
    print(f"Khi NO2:      {comp['no2']} ug/m3 ")
    print(f"Khi SO2:      {comp['so2']} ug/m3")
    print(f"Ozone (O3):   {comp['o3']} ug/m3")
    print(f"\n{CYAN}─────────────────────────────────────────────  {RESET}\n")
else:
    print(f"{BOLD}{RED}Khong tim thay thanh pho {text_thanhpho} vui long thu lai{RESET}")   