def enc_x():
    password = input('Enter your massage(should not exceed more than one line) or password to encrypt:')
    key = input("Create key for encrypt(key is required for decription):")
    savefile = input("Enter save file name:")
    encrypt = ''
    enclist = list()
    keyenc = "!"
    def enc(passer, encrypt_1):
        first = True
        char = ''
        for pss in passer:
            tmp = ''
            if pss == "Q":
                val = 12157077
            elif pss == 'W':
                val = 258366381
            elif pss == 'E':
                val = 33303865
            elif pss == 'R':
                val = 1217149
            elif pss == 'T':
                val = 20755163
            elif pss == 'Y':
                val = 7611607
            elif pss == 'U':
                val = 8794529
            elif pss == 'I':
                val = 5007452164
            elif pss == 'O':
                val = 29843237893
            elif pss == 'P':
                val = 13551751
            elif pss == 'A':
                val = '019944211'  # a number cant start with zero
            elif pss == 'S':
                val = 41191550
            elif pss == '1':
                val = 4028474
            elif pss == '2':
                val = '00086647'
            elif pss == '3':
                val = 4616508
            elif pss == '4':
                val = '073866251'
            elif pss == '5':
                val = 243001334
            elif pss == '6':
                val = 32342720
            elif pss == '7':
                val = 23582141152
            elif pss == '8':
                val = 828942016
            elif pss == '9':
                val = 924580517
            elif pss == '0':
                val = 53916088
            elif pss == 'D':
                val = 3443334490
            elif pss == 'F':
                val = 15736602959
            elif pss == 'G':
                val = 38663714664
            elif pss == 'H':
                val = 6976343924
            elif pss == 'J':
                val = 75431913
            elif pss == 'K':
                val = 7828630776
            elif pss == 'L':
                val = 8342140595
            elif pss == 'Z':
                val = 76377015
            elif pss == 'X':
                val = 3322703
            elif pss == 'C':
                val = 428700101
            elif pss == 'V':
                val = 28316285642
            elif pss == 'B':
                val = 66243762384
            elif pss == 'N':
                val = 937886310
            elif pss == 'M':
                val = 6862119
            elif pss == 'q':
                val = 96005337721
            elif pss == 'w':
                val = 2064330295
            elif pss == 'e':
                val = 9931372553
            elif pss == 'r':
                val = 56669410
            elif pss == 't':
                val = 283615068
            elif pss == 'y':
                val = 8102216656
            elif pss == 'u':
                val = 989514016
            elif pss == 'i':
                val = 8810126
            elif pss == 'o':
                val = 24050676449
            elif pss == 'p':
                val = 2864436
            elif pss == 'a':
                val = 19269670400
            elif pss == 's':
                val = 8988415
            elif pss == '~':
                val = 62994875
            elif pss == '`':
                val = 84812788
            elif pss == '!':
                val = 3030050198
            elif pss == '@':
                val = 4823637155
            elif pss == '#':
                val = 50525742181
            elif pss == '$':
                val = '0397417019'
            elif pss == '%':
                val = 7182639
            elif pss == '^':
                val = '08478719'
            elif pss == '&':
                val = 6857511
            elif pss == '*':
                val = '0162607268'
            elif pss == '(':
                val = 276429843
            elif pss == ')':
                val = 1392314
            elif pss == '_':
                val = 3448399288
            elif pss == '+':
                val = '0290185'
            elif pss == '-':
                val = 51947551
            elif pss == '=':
                val = 12463673
            elif pss == '[':
                val = 747773759
            elif pss == ']':
                val = 892513073
            elif pss == '{':
                val = 3697106
            elif pss == '}':
                val = 7904364694
            elif pss == '|':
                val = 40442035
            elif pss == ';':
                val = 4507479
            elif pss == "'":
                val = 7031231557
            elif pss == ':':
                val = 9680751491
            elif pss == '"':
                val = 3938611
            elif pss == '<':
                val = 240247084
            elif pss == '>':
                val = 965280859
            elif pss == '?':
                val = 9708203
            elif pss == ',':
                val = 78689208
            elif pss == '.':
                val = 2871312
            elif pss == 'd':
                val = 6775875969
            elif pss == 'f':
                val = 65627638
            elif pss == 'g':
                val = 1574764575
            elif pss == 'h':
                val = '035124640'
            elif pss == 'j':
                val = 60296807
            elif pss == 'k':
                val = 40996995
            elif pss == 'l':
                val = 2493488
            elif pss == 'z':
                val = '0866876223'
            elif pss == 'x':
                val = 857219694
            elif pss == 'c':
                val = 64397493193
            elif pss == 'v':
                val = 645312532
            elif pss == 'b':
                val = 12147037
            elif pss == 'n':
                val = 669245051
            elif pss == 'm':
                val = 7647164549
            elif pss == ' ':
                val = 69696969
            val = str(val)
            for encrypter in val:
                if encrypter == '1':
                    tmp = tmp + '@'
                elif encrypter == '2':
                    tmp = tmp + '#'
                elif encrypter == '3':
                    tmp = tmp + '$'
                elif encrypter == '4':
                    tmp = tmp + '%'
                elif encrypter == '5':
                    tmp = tmp + '^'
                elif encrypter == '6':
                    tmp = tmp + '&'
                elif encrypter == '7':
                    tmp = tmp + '*'
                elif encrypter == '8':
                    tmp = tmp + '('
                elif encrypter == '9':
                    tmp = tmp + ')'
                elif encrypter == '0':
                    tmp = tmp + '_'

            encrypt_1 = encrypt_1 + char + tmp
            if first == True:
                char = ":"
                first = False
        enclist.append(encrypt_1)
    enc(password, encrypt)
    enc(key, encrypt)
    savefile = savefile + '.txt'
    encfile = open(savefile, "w")
    encrypt = enclist[1] + keyenc + enclist[0][::-1] + keyenc + enclist[1]
    encfile.write(encrypt)
    print(encrypt)

def dec_x():
    decryptfile = input("Enter file name: ")
    if not decryptfile.endswith(".txt"):
        decryptfile = decryptfile + ".txt"
    try :
        decrypt = open(decryptfile,'r')
    except:
        print("file not found !")
        quit()
    deckey = input("Enter key for decryption: ")
    for text in decrypt:
        encrypted = text.strip()
    decrypt.close()
    declist = list()
    encrypt = encrypted.split("!")
    if encrypt[0] != encrypt[2]:
        print("someone edited the file,decryption is not possible")
        quit()
    raw_key = str(encrypt[0])
    raw_password = str(encrypt[1][::-1])
    decryptlist = list()
    def decrypter_0(dec):
        tmplist = list()
        enc = dec.split(":")
        for enc_0 in enc:
            tmp = ''
            for enc_1 in enc_0:
                if enc_1 =='@':
                    tmp = tmp + '1'
                elif enc_1 == '#':
                    tmp = tmp + '2'
                elif enc_1 == '$':
                    tmp = tmp + '3'
                elif enc_1 == '%':
                    tmp = tmp + '4'
                elif enc_1 == '^':
                    tmp = tmp + '5'
                elif enc_1 == '&':
                    tmp = tmp + '6'
                elif enc_1 == '*':
                    tmp = tmp + '7'
                elif enc_1 == '(':
                    tmp = tmp + '8'
                elif enc_1 == ')':
                    tmp = tmp + '9'
                elif enc_1 == '_':
                    tmp = tmp + '0'
            tmplist.append(tmp)
        decryptlist.append(tmplist)
    decrypter_0(raw_password)
    decrypter_0(raw_key)
    key = decryptlist[1]
    password = decryptlist[0]
    def decrypter_1(finaldec):
        tmp = ''
        for dec in finaldec:
            if dec == '12157077':
                tmp = tmp + 'Q'
            elif dec == '258366381':
                tmp = tmp + 'W'
            elif dec == '33303865':
                tmp = tmp + 'E'
            elif dec == '1217149':
                tmp = tmp + 'R'
            elif dec == '20755163':
                tmp = tmp + 'T'
            elif dec == '7611607':
                tmp = tmp + 'Y'
            elif dec == '8794529':
                tmp = tmp + 'U'
            elif dec == '5007452164':
                tmp = tmp + 'I'
            elif dec == '29843237893':
                tmp = tmp + 'O'
            elif dec == '13551751':
                tmp = tmp + 'P'
            elif dec == '019944211':
                tmp = tmp + 'A'
            elif dec == '41191550':
                tmp = tmp + 'S'
            elif dec == '4028474':
                tmp = tmp + '1'
            elif dec == '00086647':
                tmp = tmp + '2'
            elif dec == '4616508':
                tmp = tmp + '3'
            elif dec == '073866251':
                tmp = tmp + '4'
            elif dec == '243001334':
                tmp = tmp + '5'
            elif dec == '32342720':
                tmp = tmp + '6'
            elif dec == '23582141152':
                tmp = tmp + '7'
            elif dec == '828942016':
                tmp = tmp + '8'
            elif dec == '924580517':
                tmp = tmp + '9'
            elif dec == '53916088':
                tmp = tmp + '0'
            elif dec == '3443334490':
                tmp = tmp + 'D'
            elif dec == '15736602959':
                tmp = tmp + 'F'
            elif dec == '38663714664':
                tmp = tmp + 'G'
            elif dec == '6976343924':
                tmp = tmp + 'H'
            elif dec == '75431913':
                tmp = tmp + 'J'
            elif dec == '7828630776':
                tmp = tmp + 'K'
            elif dec == '8342140595':
                tmp = tmp + 'L'
            elif dec == '76377015':
                tmp = tmp + 'Z'
            elif dec == '3322703':
                tmp = tmp + 'X'
            elif dec == '428700101':
                tmp = tmp + 'C'
            elif dec == '28316285642':
                tmp = tmp + 'V'
            elif dec == '66243762384':
                tmp = tmp + 'B'
            elif dec == '937886310':
                tmp = tmp + 'N'
            elif dec == '6862119':
                tmp = tmp + 'M'
            elif dec == '96005337721':
                tmp = tmp + 'q'
            elif dec == '2064330295':
                tmp = tmp + 'w'
            elif dec == '9931372553':
                tmp = tmp + 'e'
            elif dec == '56669410':
                tmp = tmp + 'r'
            elif dec == '283615068':
                tmp = tmp + 't'
            elif dec == '8102216656':
                tmp = tmp + 'y'
            elif dec == '989514016':
                tmp = tmp + 'u'
            elif dec == '8810126':
                tmp = tmp + 'i'
            elif dec == '24050676449':
                tmp = tmp + 'o'
            elif dec == '2864436':
                tmp = tmp + 'p'
            elif dec == '19269670400':
                tmp = tmp + 'a'
            elif dec == '8988415':
                tmp = tmp + 's'
            elif dec == '62994875' : 
                tmp = tmp + '~'
            elif dec == '84812788' :
                tmp = tmp + '`'
            elif dec == '3030050198' :
                tmp = tmp + '!'
            elif dec == '4823637155':
                tmp = tmp + '@'
            elif dec == '50525742181':
                tmp = tmp + '#'
            elif dec == '0397417019' :
                tmp = tmp + '$'
            elif dec == '7182639':
                tmp = tmp + '%'
            elif dec == '08478719':
                tmp = tmp + '^'
            elif dec == '6857511':
                tmp = tmp + '&'
            elif dec == '0162607268':
                tmp = tmp + '*'
            elif dec == '276429843':
                tmp = tmp + '('
            elif dec == '1392314':
                tmp = tmp + ')'
            elif dec == '3448399288':
                tmp = tmp + '_'
            elif dec == '0290185':
                tmp = tmp + '+'
            elif dec == '51947551':
                tmp = tmp + '-'
            elif dec == '12463673':
                tmp = tmp + '='
            elif dec == '747773759':
                tmp = tmp + '['
            elif dec == '892513073 ':
                tmp = tmp + ']'
            elif dec == '3697106':
                tmp = tmp + '{'
            elif dec == '7904364694':
                tmp = tmp + '}'
            elif dec == '40442035':
                tmp = tmp + '|'
            elif dec == '4507479':
                tmp = tmp + ';'
            elif dec == '7031231557':
                tmp = tmp + "'"
            elif dec == '9680751491':
                tmp = tmp + ':'
            elif dec =='3938611':
                tmp = tmp + '"'
            elif dec =='240247084':
                tmp = tmp + '<'
            elif dec =='965280859':
                tmp = tmp + '>' 
            elif dec =='9708203':
                tmp =tmp + '?'
            elif dec =='78689208':
                tmp = tmp + ','
            elif dec =='2871312':
                tmp = tmp + '.'
            elif dec =='6775875969':
                tmp = tmp + 'd'
            elif dec =='65627638':
                tmp = tmp + 'f'
            elif dec =='1574764575':
                tmp = tmp + 'g'
            elif dec =='035124640':
                tmp = tmp + 'h'
            elif dec =='60296807':
                tmp = tmp + 'j'
            elif dec =='40996995':
                tmp = tmp + 'k'
            elif dec =='2493488':
                tmp = tmp + 'l'
            elif dec =='0866876223':
                tmp = tmp + 'z'
            elif dec =='857219694':
                tmp = tmp + 'x'
            elif dec =='64397493193':
                tmp = tmp + 'c'
            elif dec =='645312532':
                tmp = tmp + 'v'
            elif dec =='12147037':
                tmp = tmp + 'b'
            elif dec == '669245051':
                tmp = tmp + 'n'
            elif dec == '7647164549':
                tmp = tmp + 'm'
            elif dec == '69696969':
                tmp = tmp + ' '
        declist.append(tmp)
    decrypter_1(key)
    if deckey != declist[0]:
        print("Wrong key")
        quit()
    elif deckey == declist[0]:
        decrypter_1(password)
        print(declist[1])
print("K-395 encryption")
print("Press 1 for encryption")
print("Press 2 for decryption")
choice = int(input())
if choice == 1:
    enc_x()
elif choice == 2:
    dec_x()
