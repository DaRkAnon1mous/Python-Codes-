Str1 = 'Desserts'
Str2 = "Live" 
Str3 = 'Pals'
Str4 = 'God'
Str5 = 'Raw'

def str_rev(*n):
    output = []
    for word in n:
        reversed_word = word[::-1].capitalize()
        output.append(f"{word} : {reversed_word}")
    return output
# Str1 = 'Desserts'
# Str2 = "Live" 
# Str3 = 'Pals'
# Str4 = 'God'
# Str5 = 'Raw'
result = str_rev(Str1, Str2, Str3, Str4, Str5)
for line in result:
    print(line)
