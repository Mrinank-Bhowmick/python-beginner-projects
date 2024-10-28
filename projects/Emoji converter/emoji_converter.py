#code by Deepanshu Sharwan
message = input('Write your message here-> ') #put the text to be processed here
def emoji_converter(message):
    words = message.split(' ')
    emoji = {
        ':)': "😊",
        ':(': '☹️',
        ':o': '😮',
        '=_=': '😑',
        ':thumbs_up': '👍',
        ':okay': '👌',#you can add more emojis as per your wishes to this dictionary
        ':sad': '☹',
        ':smiling': '️😁',
        ':annoyed': '😑',
        ':blushing': '😊',
        ':laughing': '😂',
        ':ROFL': '😂',
    }
    output = ""
    for k in words:
        output += emoji.get(k,k)
        output = output + " "  #gives space after each word
    return output

print(emoji_converter(message))
