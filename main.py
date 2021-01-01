import modules.vigenere_cipher as enc


def main():
    text = str(input("enter your text: ")).upper()
    keyword = str(input("enter your keyword: ")).upper()

    encrypt = enc.VigenereChiper(text, keyword)

    key_word = encrypt.key_generator()

    print(key_word)


if __name__ == "__main__":
    main()
