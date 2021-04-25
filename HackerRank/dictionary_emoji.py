def convert_emoji(message):
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😓",
        ";)": "😉"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
output_message = convert_emoji(message)
print(output_message)
