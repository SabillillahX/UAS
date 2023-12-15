from Librarymu.myclass import LibrarySaya
from gold33423322 import hitung_golden_ratio

def main():
    while True:
        print("\nMenu:")
        print("1. Operasi A")
        print("2. Operasi B")
        print("3. Operasi C")
        print("4. Operasi D")
        print("5. Keluar")
        choice = input("Pilih Menu (1-5): ")

        if choice == '1':
            uas_operasi_a()
        elif choice == '2':
            uas_operasi_b()
        elif choice == '3':
            uas_operasi_c()
        elif choice == '4':
            uas_operasi_d()
        elif choice == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def uas_operasi_a():
    print("Melakukan operasi A")

def uas_operasi_b():
    print("Melakukan operasi B")

def uas_operasi_c():
    print("Melakukan operasi C")

def uas_operasi_d():
    print("Melakukan operasi D")


# Golden Ratio
def main():
    a = float(input("Masukkan nilai a: "))
    b = float(input("Masukkan nilai b (b tidak boleh nol): "))

    try:
        hasil = hitung_golden_ratio(a, b)
        print(f"Nilai golden ratio (phi) untuk {a} dan {b} adalah: {hasil}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
