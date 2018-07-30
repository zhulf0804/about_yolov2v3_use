import json

total_num = {'0':0, '1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0,'13':0,'14':0, '15':0, '16':0, '17':0, '18':0, '19':0, '20':0, '21':0, '22':0, '23':0, '23':0, '24':0, '25':0, '26':0, '27':0, '28':0, '29':0}

for i in range(0, 29):
  with open('via_region_data_%d.json' %i) as f:
    print i
    file = json.loads(f.read())
    #print type(file)
    for key in file:
      pic = file[key]
      #print pic
      for k in pic['regions']:
        if pic['regions'][k]['region_attributes'].has_key('object'):
	  label = pic['regions'][k]['region_attributes']['object']
          if total_num.has_key(label):
            total_num[label] = total_num[label] + 1

for i in range(0,30):
  z = str(i)
  print "calss " + str(i) + ": " + str(total_num[z]) 
