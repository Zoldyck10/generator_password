import random
import string

def generate_password(length):
    """Menghasilkan kata sandi acak"""
    if length < 6:
        return "Panjang kata sandi minimal 6 karakter."
    
    # Gabungan karakter: huruf besar, huruf kecil, angka, dan simbol
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Menghasilkan kata sandi
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Generator Kata Sandi")
    try:
        # Meminta panjang kata sandi dari pengguna
        length = int(input("Masukkan panjang kata sandi: "))
        password = generate_password(length)
        
        # Menampilkan hasil kata sandi
        print(f"Kata sandi acak: {password}")
    except ValueError:
        print("Harap masukkan angka yang valid.")
