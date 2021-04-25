def convert_emoji(message):
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😓",
        ";)": "😉"
    }
    output_message = ""
    for word in words:
        output_message += emojis.get(word, word) + " "
    return output_message


message = input(">")
output_message = convert_emoji(message)
print(output_message)
