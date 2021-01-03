

class VigenereChiper:
    def __init__(self):
        self.__chars = [c for c in (chr(i) for i in range(32, 127))]

    def __get_chars(self):
        return self.__chars

    def _generate_key(self, text, keyword):
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

    def __chiper(self, text, keyword, decrypt=False):
        key = self._generate_key(text, keyword)
        result = ''

        CHARS = self.__get_chars()

        for i, c in enumerate(text):
            if c not in CHARS:
                res += c
            else:
                text_index = CHARS.index(c)
                key_index = CHARS.index(key[i % len(key)])

                if decrypt:
                    key_index *= -1
                result += CHARS[(text_index + key_index) % len(CHARS)]

        return result

    def encrypt(self, text, key):

        return self.__chiper(text, key)

    def decrypt(self, text, key):

        return self.__chiper(text, key, True)


# CHARS = [c for c in (chr(i) for i in range(32, 127))]


# def transform(text, key, want_decrypted=False):

#     res = ''
#     for i, c in enumerate(text):
#         if c not in CHARS:
#             res += c
#         else:
#             text_index = CHARS.index(c)
#             key_index = CHARS.index(key[i % len(key)])
#             if want_decrypted:
#                 key_index *= -1
#             res += CHARS[(text_index + key_index) % len(CHARS)]
#     return res


# def encrypt(text, key):

#     return transform(text, key)


# def decrypt(text, key):

#     return transform(text, key, True)
