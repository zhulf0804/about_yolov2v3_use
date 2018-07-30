f_train = open('train.txt', 'w')
f_val = open('val.txt', 'w')
i = 0
with open('all.txt') as f:
  for line in f:
    if i%10==0:
      f_val.write(line)
    else:
      f_train.write(line)
    print line
    i = i + 1

