cd ~/bot-indrive
cat << 'EOF' > autobid_sby.py
#!/usr/bin/env python

import time
import requests

# Batas koordinat GPS wilayah Surabaya
SURABAYA_LAT_MIN = -7.3500
SURABAYA_LAT_MAX = -7.1800
SURABAYA_LON_MIN = 112.6000
SURABAYA_LON_MAX = 112.8500

# PENGATURAN PILIHAN ANDA
TARIF_MINIMUM = 20000          # Hanya ambil orderan Rp 20.000 ke atas
JEDA_REFRESH = 1               # Detik jeda cek orderan
TOKEN_AKUN = "TOKEN_AKUN_ANDA" # Masukkan token inDrive Anda di sini

API_URL = "https://indriver.com"

HEADERS = {
    "Authorization": f"Bearer {TOKEN_AKUN}",
    "Content-Type": "application/json"
}

def cek_wilayah_surabaya(lat, lon):
    """Memastikan koordinat masuk area Surabaya"""
    return SURABAYA_LAT_MIN <= lat <= SURABAYA_LAT_MAX and SURABAYA_LON_MIN <= lon <= SURABAYA_LON_MAX

def terima_orderan(order_id, tarif):
    """Mengirim perintah tembak/cocol orderan secara instan"""
    print(f"[⚡] Nyantol! Mencoba eksekusi Order ID: {order_id} | Tarif: Rp {tarif:,}")
    accept_url = f"{API_URL}/{order_id}/accept"
    
    try:
        # Pemicu ambil orderan otomatis ke server (aktifkan jika endpoint asli sudah diisi)
        # response = requests.post(accept_url, headers=HEADERS, timeout=3)
        print(f"[ SUCCESS ] Orderan {order_id} Berhasil Diambil! Segera meluncur ke lokasi.")
        return True
    except requests.exceptions.RequestException:
        print(f"[!] Gagal mengeksekusi ID {order_id} karena kendala sinyal di jalan.")
        return False

def monitor_orderan():
    print("[+] Bot Auto-Bid Aktif Sembari Melintas.")
    print(f"[+] Filter: Wilayah Surabaya | Tarif Min: Rp {TARIF_MINIMUM:,}")
    print("[+] Status: Menghubungkan jaringan & standby mencari orderan terdekat...")
    
    while True:
        try:
            # Simulasi data orderan masuk dari server real-time
            # response = requests.get(API_URL, headers=HEADERS, timeout=2).json()
            
            # Simulasi 3 Macam Orderan yang Masuk Bersamaan di Sistem
            orderan_masuk = [
                {"id": "2001", "lat": -7.2504, "lon": 112.7508, "tarif": 25000}, # Surabaya & Tarif Masuk
                {"id": "2002", "lat": -7.2600, "lon": 112.7400, "tarif": 12000}, # Tarif di bawah minimum
                {"id": "2003", "lat": -7.5500, "lon": 112.3000, "tarif": 60000}  # Luar Surabaya
            ]

            for order in orderan_masuk:
                lat = order["lat"]
                lon = order["lon"]
                tarif = order["tarif"]
                
                if cek_wilayah_surabaya(lat, lon):
                    if tarif >= TARIF_MINIMUM:
                        terima_orderan(order["id"], tarif)
                    else:
                        print(f"[-] Skip ID {order['id']}: Rp {tarif:,} di bawah batas minimum Rp {TARIF_MINIMUM:,}")
                else:
                    print(f"[-] Skip ID {order['id']}: Lokasi di luar jangkauan peta Surabaya.")

        except requests.exceptions.ConnectionError:
            print("[!] Sinyal HP tidak stabil di jalan. Menghubungkan kembali secara otomatis...")
            time.sleep(2)
            continue
        except Exception as e:
            print(f"[-] Sistem mendeteksi gangguan: {e}")
        
        time.sleep(JEDA_REFRESH)

if __name__ == "__main__":
    monitor_orderan()
EOF
