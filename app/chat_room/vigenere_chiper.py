

CHARS = [c for c in (chr(i) for i in range(32, 127))]


def transform(text, key, want_decrypted=False):

    res = ""
    for i, c in enumerate(text):
        if c not in CHARS:
            res += c
        else:
            text_index = CHARS.index(c)
            key_index = CHARS.index(key[i % len(key)])
            if want_decrypted:
                key_index *= -1
            res += CHARS[(text_index + key_index) % len(CHARS)]
    return res


def encrypt(text, key):

    return transform(text, key)


def decrypt(text, key):

    return transform(text, key, True)
