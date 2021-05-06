s1 = "Fgzgrb qftc citkt om cal egdofu ykgd. 28 btakl samtk, ct ktetoxtr a loufas miam cal asdglm mit ladt.".lower()
s2 = "Nobody knew where it was coming from. 28 years later, we received a signal that was almost the same.".lower()

def decipher(s):
    decoded_message = ""
    for c in range(0, len(s)):
        for c1 in range(0, len(s1)):
            if s[c] == s1[c1]:
                decoded_message = decoded_message + s2[c1]
                break
    print(decoded_message)
        # print(string_name[c])

decipher("FADT GY LOUFAS".lower())
input()
