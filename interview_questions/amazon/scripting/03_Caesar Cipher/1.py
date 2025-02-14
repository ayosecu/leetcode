def encrypt_caesar_cipher(text: str, shift: int) -> str:
    """
    Given a string 'text', encrypt it using Caesar Cipher with a given shift value.
    The function should preserve the case of letters and ignore non-alphabetic characters.

    Example:
    caesar_cipher("Hello, World!", 3) -> "Khoor, Zruog!"
    """
    A_ASCII = ord("A")
    Z_ASCII = ord("Z")
    a_ASCII = ord("a")
    z_ASCII = ord("z")

    result = ""
    for c in text:
        c_ASCII = ord(c)
        if A_ASCII <= c_ASCII <= Z_ASCII:
            c_ASCII += shift
            if c_ASCII > Z_ASCII:
                c_ASCII = A_ASCII + (c_ASCII - Z_ASCII) - 1
            result += chr(c_ASCII)
        elif a_ASCII <= c_ASCII <= z_ASCII:
            c_ASCII += shift
            if c_ASCII > z_ASCII:
                c_ASCII = a_ASCII + (c_ASCII - z_ASCII) - 1
            result += chr(c_ASCII)
        else:
            result += c

    return result

def caesar_cipher(text: str, shift: int) -> str:
    """
    Given a string 'text', encrypt it using Caesar Cipher with a given shift value.
    The function should preserve the case of letters and ignore non-alphabetic characters.

    Example:
    caesar_cipher("Hello, World!", 3) -> "Khoor, Zruog!"
    caesar_cipher("Khoor, Zruog!", -3) -> "Hello, World!"
    """

    def convert(c_ascii, shift, s_ascii, e_ascii):
        shift %= 26
        c_ascii += shift

        if c_ascii > e_ascii:
            c_ascii = s_ascii + (c_ascii - e_ascii) - 1
        elif c_ascii < s_ascii:
            c_ascii = e_ascii - (s_ascii - c_ascii) + 1
       
        return chr(c_ascii)
    
    result = ""
    for c in text:
        if "a" <= c <= "z":
            result += convert(ord(c), shift, ord("a"), ord("z"))
        elif "A" <= c <= "Z":
            result += convert(ord(c), shift, ord("A"), ord("Z"))
        else:
            result += c

    return result

print(caesar_cipher("Hello, World!", 3))
print(caesar_cipher("Khoor, Zruog!", -3))