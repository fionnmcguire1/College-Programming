'''
Fionn Mcguire
C13316356
Advanced Security Lab 2
20/09/2016
To encrypt and decrypt using caesar and Vigenere
'''
from itertools import cycle
#import enchant
#dictionary = enchant.Dict("en_US")

#Question 1 Encrypting and Decrypting using Caesar Cipher
def caesar (key,text,e_or_d):
    #creating alphabet and a capital letter alphabet as python sees these as two different chars
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    #this is the text made as a result of processing the plaintext or ciphertext
    resulted_text = ''
    #The letter to be appended to the resulted_text
    result_t=''
    i = 0
    #Moving through the text provided
    while i < len(text):
        caps = False
        number = alphabet.find(text[i])
        #if char does not exist it's not a letter it's % or $ or something so
        #i've written it so that these just print with no encryption in order
        #to provide an exact caesar decryption which returns the origional text as it was.
        #The caesar cipher focuses on shifting letters not symbols.
        #if a char doesn't exist in the lower case alphabet, it checks the ALPHABET
        #if it doesn't exist there then it must be a symbol and the symbol is printed.
        if number == -1:
            number = ALPHABET.find(text[i])
            caps = True
            if number == -1:
                resulted_text += text[i]
        #if the char is not a symbol then encryption/decryption must take place
        if number != -1:     
            #If encryption is requested
            if e_or_d == 'e':
                result = (number+key-1)%len(alphabet)
                if caps == True:
                    result_t = ALPHABET[result]
                else:
                    result_t = alphabet[result]
                resulted_text +=result_t
            #If decryption is requested
            if e_or_d == 'd':
                result = (number-key+1)%len(alphabet)
                if caps == True:
                    result_t = ALPHABET[result]
                else:
                    result_t = alphabet[result]
                resulted_text +=result_t
        i=i+1
    #print the result
    #print(resulted_text)
    return(resulted_text)

caesar (3,"And I shall remain satisfied, and proud to have been the first who has ever enjoyed the fruit of his writings as fully as he could desire for my desire has been no other than to deliverover to the detestation of mankind the false and foolish tales of the books of chivalry, which, thanks to that of my true Don Quixote, are even now tottering, and doubtless doomed to fall for ever. Farewell.",'e')
   
'''
Plaintext: And I shall remain satisfied, and proud to have been the
first who has ever enjoyed the fruit of his writings as fully as he
could desire for my desire has been no other than to deliverover
to the detestation of mankind the false and foolish tales of the
books of chivalry, which, thanks to that of my true Don Quixote,
are even now tottering, and doubtless doomed to fall for ever. Farewell.

Ciphertext: Cpf K ujcnn tgockp ucvkuhkgf,cpf rtqwf vq jcxg dggp
vjg hktuv yjq jcu gxgt gplqagf vjg htwkv qh jku ytkvkpiu cu hwnna
cu jg eqwnf fguktg hqt oa fguktg jcu dggp pq qvjgt vjcp vq
fgnkxgtqxgt vq vjg fgvguvcvkqp qh ocpmkpf vjg hcnug cpf
hqqnkuj vcngu qh vjg dqqmu qh ejkxcnta, yjkej, vjcpmu vq vjcv
qh oa vtwg Fqp Swkzqvg, ctg gxgp pqy vqvvgtkpi, cpf fqwdvnguu
fqqogf vq hcnn hqt gxgt. Hctgygnn.
'''

#Question 2: Decrypt Caesar Cipher Brute Force

'''Ciphertext: Vg jbhyq frrz gung, nf ur rknzvarq gur frireny cbffvovyvgvrf, n fhfcvpvba pebffrq uvf zvaq: gur
zrzbel bs ubj ur uvzfrys unq orunirq va rneyvre qnlf znqr uvz nfx jurgure fbzrbar zvtug or
uvqvat ure sebz gur jbeyq'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
i=0
while i < len(alphabet):
    resulted_text = caesar(i,'Vg jbhyq frrz gung, nf ur rknzvarq gur frireny cbffvovyvgvrf, n fhfcvpvba pebffrq uvf zvaq: gurzrzbel bs ubj ur uvzfrys unq orunirq va rneyvre qnlf znqr uvz nfx jurgure fbzrbar zvtug oruvqvat ure sebz gur jbeyq','d')
    #I was unable to import enchant however
    #what i was tring to do was to import enchant, split the resulting string into words
    #check the percentage of words in the plaintext that were english
    #then only print the string with the highest percentage or english words
    #this would most likely be the origional plaintext. As i understand it, importing enchant is an
    #issue with MAC OS/ C libraries fixing it would have needed multiple
    #instalations of different software
    #However when you use my brute force method you get 26 texts returned, skim through them and
    #you'll be able to see the origional ciphertext
    '''words = resulted_text.split()
    j = 0
    while j<len(words):
        dictionary.check(words[j])'''
    
    #print(resulted_text)
    i = i+1


#Question 3 & 4 Encrypting and Decrypting using Vigenere cipher

def Vigenere (key,text,e_or_d):
    i =0
    #these are the same i'm just differenciating between the terms
    ciphertext = ''
    plaintext = ''
    #formatting the text to be properly encrypted or decrypted
    text = text.upper()
    text = text.replace(' ', '')
    text = text.replace('(', '')
    text = text.replace(')', '')
    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace(';', '')
    #key_origional is nessisary as we are altering the key length to repeat the key
    key_origional = key
    if len(key) != len(text):
        #if the key is shorter then the text the key will be repeated until same length as text
        if len(key) < len(text):
            #key = cycle(key)
            while len(key)<len(text):
                j = i %len(key_origional)
                key += key_origional[j]
                i = i+1
        #if key is longer than text then key will be cut
        key = key[0:len(text)]
    #need an alphabet to process
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    i=0
    if e_or_d == 'e':
        #going through each letter
        while i < len(text):
            if text[i] == '0' or text[i] == '1' or text[i] == '2' or text[i] == '3' or text[i] == '4' or text[i] == '5' or text[i] == '6' or text[i] == '7' or text[i] == '8' or text[i] == '9' :
                print(text[i])
                ciphertext = ''.join((ciphertext,text[i]))
            else:
                #finding the position of the text letter in the alphabet          
                number = ALPHABET.find(text[i])
                #finding the position of the key letter in the alphabet
                number_key = ALPHABET.find(key[i])
                #processing the encryption
                resulting_number = (number+number_key)%len(ALPHABET)
                #creating the ciphertext
                ciphertext = ''.join((ciphertext,ALPHABET[resulting_number]))
            i = i+1
        print(ciphertext)
    #The decryption is the same but instead of adding the positions of the key and text in
    #the alphabet you subtract their positions
    if e_or_d == 'd':
        j=0
        while i < len(text):
            if text[i] == '0' or text[i] == '1' or text[i] == '2' or text[i] == '3' or text[i] == '4' or text[i] == '5' or text[i] == '6' or text[i] == '7' or text[i] == '8' or text[i] == '9' :
                plaintext = ''.join((plaintext,text[i]))
            else:
                number=0
                number_key=0
                resulting_number=0
                number = ALPHABET.find(text[i])
                number_key = ALPHABET.find(key[j])
                resulting_number = (number-number_key)%len(ALPHABET)
                #print(resulting_number)
                plaintext = ''.join((plaintext,ALPHABET[resulting_number]))
                j=j+1
                #print("Ciphertext: %s %d -  Key: %s, %d = Plaintext: %s,%d " % (text[i], number, key[i],number_key,ALPHABET[resulting_number],resulting_number))
            i = i+1
        print(plaintext)

    '''
    Plaintext: I shall (from now on) select and take the ingots individually
    in my own yard, and I shall exercise against you my right of rejection
    because you have treated me with contempt.


    Ciphertext: XSZSHZWUDMFGSCEVTLWUPOEGIACWPVVLCG
    GLOWEGXVAVQOCONIFEUCNQNAJVWBULHHSDHSOHGCA
    KAOXDXNKLUCLPNRAYDHFIGEBWYHZRCBWUWIJHNOMZ
    WJVWGESLARDHLILZYCEWTMHL
    '''


def crack_vigenere_key(known_plaintext, text,ciphertext):
    '''Known plaintext was thursday and concidering the numbers 28 2016 were followed
    shortly after i assumed Yudq was a month. There are only two 4 letter months so
    i was able to guess that it was July'''
    #Thursday
    #Yhwvtroi
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key=''
    '''formatting text'''
    ciphertext = ciphertext.replace(' ', '')
    ciphertext = ciphertext.replace('(', '')
    ciphertext = ciphertext.replace(')', '')
    ciphertext = ciphertext.replace('.', '')
    ciphertext = ciphertext.replace(',', '')
    known_plaintext =known_plaintext.upper()
    text = text.upper()
    i = 0
    '''Reverse engineering the key using the formula
    Kn = Cn-Pn then converting it to letters.'''
    while i < len(text):
        known_number=0
        text_number=0
        resulting_number=0
        known_number = ALPHABET.find(known_plaintext[i])
        text_number = ALPHABET.find(text[i])
        resulting_number = (text_number-known_number)%len(ALPHABET)
        key = ''.join((key,ALPHABET[resulting_number]))
        i = i+1
    key = ''.join((key,"PASSWORD"))


    
    print("Key is: ")
    print(key)
    '''
    I was unable to programmably guess the key but from the function decryptor working
    with other Vigenere ciphers and not with this one i knew it had to be longer than 12 letters
    so i printed the key and made a few guesses, eventually guesses FACEBOOKPASSWORD
    and hardcoded it to the function call.'''
    Vigenere("FACEBOOKPASSWORD",ciphertext,'d')

'''Ciphertext: Yhwvtroi, 28 Yudq 2016  Pse bjatw pt foxgf zwjzql bgio qcwelwlar, blsg rmprochek ewrv
nsoyr uvs ndcljebv rk pkium hy bef; sjr wutm vljg aybefl ds ydx mchf asx bojw lwfxx, aph
fjsbntzaju kkwixit hvbduyzkik wme ylpzs gdrdv. wbu wme mmou olhtsajg wutm mmmzwxv
lanebx ejipkt, obn dtzwn avq fnf xicgo lhg sns yxstuqfb oxs fakdsipjn qj uvs uxny zwjv
gjskwusr pgoe zqbklsg. cre wt cdmw oafv lstgqqsfkie, lzam ydae eibgsn urge pvvlw
ipxfadogafua oj zfs kr uvssg pgoaf rqi odiewsxi tg ldszu kavlff oxs mgldsi dsd vs uvs oadwjo,
we rupqwjhwyc tg lds gdxt cptc wx ihw xqhluj, ba wp oqdxny gj smhwy qgdogsdn, lzam nlql
nmws poitwj wbu ptrg lbddsay'''

'''
Plaintext: thursday, 28 july 2016  ten years of reign having been completed,
king piodasses made known the doctrine of piety to men; and from this moment
he has made men more pious, andeverything thrives throughout the whole world.
and the king abstains from killing living beings, and other men and those who
are huntsmen and fishermen of the king havedesisted from hunting. and if some
were intemperate, they have ceased from their intemperance as was in their
power; and obedient to their father and mother and to the elders,in opposition
to the past also in the future, by so acting on every occasion, they will live
better and more happily

Key: FACEBOOKPASSWORD

'''
#Q1 caesar (3,"And I shall remain satisfied, and proud to have been the first who has ever enjoyed the fruit of his writings as fully as he could desire for my desire has been no other than to deliverover to the detestation of mankind the false and foolish tales of the books of chivalry, which, thanks to that of my true Don Quixote, are even now tottering, and doubtless doomed to fall for ever. Farewell.",'e')
#Q2 caesar (14,'Vg jbhyq frrz gung, nf ur rknzvarq gur frireny cbffvovyvgvrf, n fhfcvpvba pebffrq uvf zvaq: gur zrzbel bs ubj ur uvzfrys unq orunirq va rneyvre qnlf znqr uvz nfx jurgure fbzrbar zvtug or uvqvat ure sebz gur jbeyq','d')
#Q3 Vigenere('PASSWORD',"I shall (from now on) select and take the ingots individually in my own yard, and I shall exercise against you my right of rejection because you have treated me with contempt.",'e')
#Q4 crack_vigenere_key("Thursday","Yhwvtroi","Yhwvtroi, 28 Yudq 2016  Pse bjatw pt foxgf zwjzql bgio qcwelwlar, blsg rmprochek ewrv nsoyr uvs ndcljebv rk pkium hy bef; sjr wutm vljg aybefl ds ydx mchf asx bojw lwfxx, aph fjsbntzaju kkwixit hvbduyzkik wme ylpzs gdrdv. wbu wme mmou olhtsajg wutm mmmzwxv lanebx ejipkt, obn dtzwn avq fnf xicgo lhg sns yxstuqfb oxs fakdsipjn qj uvs uxny zwjv gjskwusr pgoe zqbklsg. cre wt cdmw oafv lstgqqsfkie, lzam ydae eibgsn urge pvvlw ipxfadogafua oj zfs kr uvssg pgoaf rqi odiewsxi tg ldszu kavlff oxs mgldsi dsd vs uvs oadwjo, we rupqwjhwyc tg lds gdxt cptc wx ihw xqhluj, ba wp oqdxny gj smhwy qgdogsdn, lzam nlql nmws poitwj wbu ptrg lbddsay")

        
