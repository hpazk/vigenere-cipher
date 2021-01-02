from modules.vigenere_chiper import VigenereChiper


def main():
    text = str(input("enter your text: ")).upper()
    keyword = str(input("enter your keyword: ")).upper()

    # instantiating
    encrypt = VigenereChiper()

    # encryptor
    encrypted_text = encrypt.encryptor(text, keyword)
    print(f"encrypted text: {encrypted_text}")

    # decryptor
    decrypted_text = encrypt.decryptor(encrypted_text, keyword)
    print(f"decrypted text: {decrypted_text}")


if __name__ == "__main__":
    main()
