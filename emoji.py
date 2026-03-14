def imoji_replacer(message):
    imojis_dict = {"happy": "😄", "sad": "😔", "cry": "😭", "angry": "😡","love":"❤️","laugh":"😂","ok":"👌","fire":"🔥","cool":"😎"}
    words = message.split()
    result = []
    for word in words:
            result.append(imojis_dict.get(word.lower(),word))
    return " ".join(result)
user_message = input("Enter your message: ")
print("Converted message:", imoji_replacer(user_message))
