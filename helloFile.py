def writeToFile():
  '''f = open('test.txt','w')
  f.write('Hello World')
  f.close()'''
  f1 = open('test.txt', 'w')
  #print(f1.read())
  f1.write('Hi Python Programming')
  f1.close()
  f2 = open('test.txt','r')
  print(f2.read())

if __name__ == '__main__':
  writeToFile()