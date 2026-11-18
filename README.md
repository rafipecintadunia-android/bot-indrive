# Bot inDrive (Area Surabaya)

Skrip otomatisasi berbasis **Python** untuk memantau dan mengambil orderan masuk secara otomatis berdasarkan filter koordinat wilayah Surabaya dan tarif minimum.

## Daftar File Utama
* `autobid_sby.py` - Skrip utama untuk filter area Surabaya dan eksekusi orderan otomatis.
* `latihan_api.py` - Skrip pengujian koneksi dan permintaan API.

## Fitur Utama
* **Filter Area Surabaya:** Memastikan titik lokasi orderan berada di dalam batas koordinat Surabaya (`SURABAYA_LAT_MIN/MAX` dan `SURABAYA_LON_MIN/MAX`).
* **Filter Tarif Minimum:** Mengatur nominal tarif terendah yang ingin diambil (default Rp 20.000).
* **Jeda Refresh Cepat:** Mengatur kecepatan pengecekan orderan dalam satuan detik (`JEDA_REFRESH`).

## Cara Menjalankan
1. Kloning repositori ini:
   ```bash
   git clone https://github.com
   cd bot-indrive
   ```
2. Buka file `autobid_sby.py`, lalu masukkan token akun Anda pada variabel `TOKEN_AKUN` dan sesuaikan pengaturan tarif.
3. Jalankan skrip utama:
   ```bash
   python3 autobid_sby.py
   ```

## Catatan Keamanan
* Pastikan untuk tidak mengunggah `TOKEN_AKUN` asli ke repositori publik demi keamanan akun.
