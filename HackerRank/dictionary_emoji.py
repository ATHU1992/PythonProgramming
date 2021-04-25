message = input(">")
words = message.split(" ")
emojis = {
    ":)": "😊",
    ":(": "😓",
    ";)": "😉"
}
output_message = ""
for word in words:
    output_message += emojis.get(word, word) + " "
print(output_message)
