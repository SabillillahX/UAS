def hitung_golden_ratio(a, b):
    if b == 0:
        raise ValueError("Nilai b tidak boleh nol.")
    
    phi = (a + b) / b
    return phi
