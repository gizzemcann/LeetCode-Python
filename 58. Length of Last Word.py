def lengthOfLastWord_algo(s: str) -> int:
    """
    Strip ve split kullanmadan, doğrudan karakterleri kontrol ederek çözüm.
    """
    length = 0
    i = len(s) - 1

    # Sondaki boşlukları atla
    while i >= 0 and s[i] == ' ':
        i -= 1

    # Son kelimeyi say
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1

    return length