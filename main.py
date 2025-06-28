import requests
from datetime import datetime

# Ganti ini dengan API key kamu
api_key = "sk-SuBHy5oSmlFpiZK2imgV0BkXpl9S9T3CAFGJ5wOfutBfOWvF"

# Deskripsi gambar
prompt = input("Masukkan prompt: ")

# Nama file berdasarkan waktu biar gak numpuk
filename = f"D:/00. Kuliah/-- My Project --/OngImage_ModAI/output_generate/gambar_{datetime.now().strftime('%Y%m%d_%H%M%S')}.webp"

# Kirim request ke Stability AI
response = requests.post(
    "https://api.stability.ai/v2beta/stable-image/generate/sd3",
    headers={
        "authorization": f"Bearer {api_key}",
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": prompt,
        "output_format": "png",
    },
)

# Simpan hasil kalau sukses
if response.status_code == 200:
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"✅ Gambar berhasil disimpan ke: {filename}")
else:
    print("❌ Gagal:", response.status_code, response.text)
