a = input()

key_map = {
    "q":"w","w":"e","e":"r","r":"t","t":"y","y":"u","u":"i","i":"o","o":"p","p":"p",
    "a":"s","s":"d","d":"f","f":"g","g":"h","h":"j","j":"k","k":"l","l":"l",
    "z":"x","x":"c","c":"v","v":"b","b":"n","n":"m","m":"m",
}

print("".join([str.lower,str.upper][i.isupper()](key_map[i.lower()]) for i in a))