'''
fout=open('./vocab_4kmer.txt','w')
s='atcgn'
for aa1 in s:
    for aa2 in s:
        for aa3 in s:
            for aa4 in s:
                    a = aa1
                    b = aa2
                    c = aa3
                    d = aa4
                    fout.write(a + b + c + d + '\n')                    
fout.close()
'''        
fout=open('../vocab_3kmer.txt','a')
f=open('./vocab_5kmer.txt','r')
data=f.readlines()
f.close()
for line in data:
    fout.write(line)
fout.close()
