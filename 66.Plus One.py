def plusOne_algo(digits):
    """
    digits: List[int] — Her eleman bir basamaktır.
    return: List[int] — Sayıya 1 eklenmiş hali.
    """
    n = len(digits)
    
    # Sondan başa doğru git
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1  # Direkt artır
            return digits
        digits[i] = 0  # 9 ise 0 yap, elde var 1

    # Hepsi 9'duysa başa 1 ekle
    return [1] + [0] * n
print(plusOne_algo([1, 2, 3]))   # Çıktı: [1, 2, 4]
print(plusOne_algo([9, 9, 9]))   # Çıktı: [1, 0, 0, 0]