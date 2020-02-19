import random

msg1 = "hello world!"
print(msg1.capitalize())
print()

msg2 = "welcome to the random password generator!"
print(msg2.capitalize())
print()

msg3 = "here is the randomly generated password:"
print(msg3.capitalize())

Upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
random.shuffle(Upper)
random.choice(Upper)

Lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
random.shuffle(Lower)
random.choice(Lower)

Number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "1", "2", 
"3", "4", "5", "6", "7", "8", "9"]
random.shuffle(Number)
random.choice(Number)

Special = ["!", "@", "#", "$", "%", "&", "!", "@", "#", "$", "%", "&", 
"!", "@", "#", "$", "%", "&", "!", "@", "#", "$", "%", "&"]
random.shuffle(Special)
random.choice(Special)

optionPass = Upper + Lower + Number + Special

print(random.choice(optionPass) + random.choice(optionPass) + 
random.choice(optionPass) + random.choice(optionPass) + 
random.choice(optionPass) + random.choice(optionPass) + 
random.choice(optionPass))