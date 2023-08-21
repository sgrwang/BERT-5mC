import json
import sys

input_file = sys.argv[1] 
output_file = sys.argv[2]
label_file = sys.argv[3] 
label = []	

fea = open(output_file,'w')
tmp = []
for line in open(input_file,'r'):
    tmp.append(json.loads(line))
for line in open(label_file,'r'):
    label.append(line.split('\t')[0])
print(label)
for i in range(len(tmp)):
    fea.write(label[i])
    #for f in range(len(tmp[i]['features'])):
    s = len(tmp[i]['features'][0]['layers'])
    for j in range(s):
        # print(tmp[i]['features'][0]['layers'][j]['values'])
        ss = len(tmp[i]['features'][0]['layers'][j]['values'])
        for k in range(ss):
            # print(type(tmp[i]['features'][0]['layers'][k]['values']))
            fea.write(',' + str(tmp[i]['features'][0]['layers'][j]['values'][k]))
    fea.write('\n')

fea.close()


