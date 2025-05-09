def alphabet_position(text):
        string = ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
        print(string)

if __name__ == "__main__":
        alphabet_position("test")
