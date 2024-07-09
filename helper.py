alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
dict_alpha = {}

for i, v in enumerate(alpha_list):
    dict_alpha[v] = i 

dict_alpha[' '] = -1
def encoder(word: str):
    val = []
    for i in word.lower():
        if i == ' ':
            val.append(-1)
        else:
            val.append(dict_alpha[i])
    return val    

def decoder(number):
    val = []
    for i in number:
        for j in dict_alpha:
            if dict_alpha[j] == i:
                val.append(j)
    return ''.join(val)
        
def main():
    z = encoder("Hello World")
    y = decoder([7, 4, 11, 11, 14, -1, 22, 14, 17, 11, 3])
    print(z)
    print(y)

if __name__ == '__main__':
    main()