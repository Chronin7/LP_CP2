import utill_functions
def main():
    encoder = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----",".": ".-.-.-",",": "--..--","?": "..--..","!": "-.-.--","/": "-..-.","(": "-.--.",")": "-.--.-","&": ".-...",":": "---...",";": "-.-.-.","=": "-...-","-": "-....-",'"': ".-..-.","@": ".--.-."," ":""}
    decoder = {v: k for k, v in encoder.items()}
    while True:
        choies = utill_functions.get_valid_type(int,"This is a morce code translator\n0 to return\n1 to encode\n2 to decode\nwhat do you want: ")
        if choies==0:
            return
        elif choies==1:
            encode=utill_functions.get_valid_type(str,"What is your message to encode: ").upper()
            for x in list(encode):
                print(encoder.get(x),end=" ")
            print()
        elif choies==2:
            decode=utill_functions.get_valid_type(str,"What is the message to decode: ")
            for x in decode.split(sep=" "):
                print(decoder.get(x),end="")
            print()
if __name__=="__main__":
    main()