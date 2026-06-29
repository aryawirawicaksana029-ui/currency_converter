import requests
from datetime import datetime

def get_rates(base_currency):
    # Ambil data dari API
    # Kita ubah base_currency menjadi uppercase untuk menghindari error case-sensitive
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency.upper()}"
    try:
        response = requests.get(url)
        response.raise_for_status() # Memastikan request berhasil (status 200)
        return response.json()
    except requests.exceptions.RequestException:
        return None

def convert(amount, from_currency, to_currency):
    # 1. Ambil rates berdasarkan mata uang asal (from_currency)
    data = get_rates(from_currency)
    
    if not data:
        print("❌ Gagal mengambil data kurs. Periksa koneksi internet Anda.")
        return None
        
    # 2. Ambil dictionary rates dan timestamp dari response API
    rates = data.get("rates", {})
    last_updated = data.get("time_last_updated", 0)
    
    # Ambil kode target mata uang (diubah ke uppercase)
    target = to_currency.upper()
    
    # 3. Hitung konversi jika mata uang tujuan ada di dalam data API
    if target in rates:
        exchange_rate = rates[target]
        converted_amount = amount * exchange_rate
        # Mengembalikan hasil konversi, nilai kurs, dan waktu update
        return converted_amount, exchange_rate, last_updated
    else:
        print(f"❌ Kode mata uang '{to_currency}' tidak ditemukan.")
        return None

def main():
    print("=== Aplikasi Currency Converter Real-Time ===")
    
    # 1. Input amount dengan validasi angka
    try:
        amount = float(input("Masukkan jumlah uang (nominal): "))
        if amount <= 0:
            print("❌ Jumlah uang harus lebih dari 0.")
            return
    except ValueError:
        print("❌ Input harus berupa angka nominal yang valid.")
        return
        
    # 2. Input mata uang asal dan tujuan
    from_currency = input("Dari mata uang (contoh: USD, IDR): ").strip()
    to_currency = input("Ke mata uang (contoh: IDR, JPY): ").strip()
    
    print("\n🔄 Sedang mengambil kurs terbaru...")
    
    # 3. Panggil fungsi konversi
    result = convert(amount, from_currency, to_currency)
    
    # 4. Tampilkan hasil jika konversi berhasil
    if result:
        converted_amount, exchange_rate, last_updated = result
        
        # Mengubah timestamp UNIX dari API menjadi format waktu yang bisa dibaca
        date_obj = datetime.fromtimestamp(last_updated)
        formatted_time = date_obj.strftime('%Y-%m-%d %H:%M:%S')
        
        print("\n" + "="*40)
        print(f"💰 Hasil Konversi: {amount:,.2f} {from_currency.upper()} = {converted_amount:,.2f} {to_currency.upper()}")
        print(f"📈 Kurs Saat Ini  : 1 {from_currency.upper()} = {exchange_rate:,.4f} {to_currency.upper()}")
        print(f"🕒 Terakhir Update: {formatted_time}")
        print("="*40)

if __name__ == "__main__":
    while True:
        main()
        again = input("\nConvert again? (y/n): ")
        if again.lower() == "n":
            print("Goodbye! 👋")
            break