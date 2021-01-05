class VigenereChiper:
    def __init__(self):
        self.__alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def key_generator(self, text, keyword):
        key = []
        key_count = 0
        for i in range(0, len(text)):
            if text[i] == ' ':
                key.append(' ')
            else:
                x = key_count % len(keyword)
                key.append(keyword[x])
                key_count += 1

        key = ''.join(str(s) for s in key)

        return key

    def get_alphabets(self):
        return self.__alphabets

    def encryptor(self, text, keyword):
        key = self.key_generator(text, keyword)
        alphabets = self.get_alphabets()

        encrypted = ''

        for i in range(0, len(text)):
            if text[i] == ' ':
                encrypted += ' '
            else:
                value = (alphabets.find(
                    text[i]) + alphabets.find(key[i])) % 26
                encrypted += alphabets[value]

        return encrypted

    def decryptor(self, encrypted_text, keyword):
        key = self.key_generator(encrypted_text, keyword)
        alphabets = self.get_alphabets()

        decrypted = ''

        for i in range(0, len(encrypted_text)):
            if encrypted_text[i] == ' ':
                decrypted += ' '
            else:
                value = (alphabets.find(
                    encrypted_text[i]) - alphabets.find(key[i])) % 26
                decrypted += alphabets[value]

        return decrypted


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
