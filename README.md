# 🔐 Android PIN Brute Force (ADB Based)

Script Python ini mencoba menebak PIN 4 digit pada perangkat Android menggunakan **ADB (Android Debug Bridge)** dengan cara brute force.

> ⚠️ **Peringatan**: Hanya gunakan script ini untuk keperluan edukasi, riset keamanan, atau perangkat milik sendiri. Penyalahgunaan bisa melanggar hukum dan etika.

## 💡 Fitur

- Brute force PIN 4 digit (0000 - 9999)
- Kirim input langsung ke perangkat Android via ADB
- Delay antar percobaan untuk mencegah deteksi terlalu cepat
- Gak ada cek status, jadi fokus brute full-swing

## 📦 Requirements

- Python 3.x
- ADB (Android Debug Bridge) sudah terinstall dan bisa diakses lewat terminal/command prompt

## 🛠 Cara Pakai

1. Pastikan USB Debugging aktif di perangkat Android
2. Sambungkan perangkat ke PC/laptop lewat USB
3. Jalankan script dengan:

```bash
python bruteforce.py
``` 

## 🔧 Customization
bisa di ganti delay nya
```bash
brute_force_pin(delay=6)  # Delay 6 detik antar input
```