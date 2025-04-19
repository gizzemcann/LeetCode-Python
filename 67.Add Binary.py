def addBinary_algo(a: str, b: str) -> str:
    
    result = []         # Sonucu ters olarak tutacağız
    carry = 0           # Elde (taşıma)
    i, j = len(a) - 1, len(b) - 1

    # Her iki string bitene kadar dön
    while i >= 0 or j >= 0 or carry:
        total = carry

        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1

        result.append(str(total % 2))  # Binary basamak (0 veya 1)
        carry = total // 2             # Elde varsa 1 olur

    return ''.join(reversed(result))   # Ters çevirerek sonucu döndür