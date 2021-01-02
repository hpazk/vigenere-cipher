import modules.vigenere_cipher as enc


def main():
    text = str(input("enter your text: ")).upper()
    keyword = str(input("enter your keyword: ")).upper()

    # instantiating
    encrypt = enc.VigenereChiper(text, keyword)

    # encryptor
    encrypted_text = encrypt.encryptor()
    print(f"encrypted text: {encrypted_text}")

    # decryptor
    decrypted_text = encrypt.decryptor(encrypted_text)
    print(f"decrypted text: {decrypted_text}")


if __name__ == "__main__":
    main()
