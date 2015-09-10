from Crypto.Hash import MD4

targetHash = raw_input("Enter hash you wanna decrypt: ")
cset = raw_input("Enter charset(put 0 for default): ")
if cset == "0":
    cset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

length        = 1                 # length of created_data
possibilities = len(cset)**length # possibilities of different hashes
created_data  = ""                # created data whose hash will be checked with targetHash 
created_hash  = ""                # hash of created_data
data_lines    = []

for _ in xrange(length):
    data_lines.append(0)

flag = True # Flag to end while loop when data be found
print "[+] Bruteforce for specified hash is starting...\n"

while flag:
    print "[+] Current length is", length, "with", possibilities, "possibilities."
    for i in xrange(possibilities):
        created_data = ""
        for i in xrange(length):
            created_data += cset[ data_lines[i] ]
        
        created_hash = MD4.new(created_data).hexdigest()
        if created_hash == targetHash:
            print ""
            print "[!] FOUND! Data is:", created_data
            print ""
            print "[x] Thanks for using FTdecoder..."
            flag = False
            break
        
        data_lines[ length-1 ] += 1
        
        for i in xrange(length-1, -1, -1):
            if data_lines[i] < len(cset):
                break
            else:
                data_lines[i]   = 0
                data_lines[i-1] += 1
    length += 1
    possibilities *= len(cset)
    data_lines.append(0)

'''
NOTES: According to cset and length, speed will increase or decrease so if you have
       extra information about characterset or length of the data whose hash will be decrypt,
       change that variables.
'''
