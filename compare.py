def matchList(list1,list2):
  return list1 == list2

if __name__ == "__main__":
  list1 =[]
  list2 =[]
  print('Enter values for first list\n')
  for i in range(10):
    input1 = int(input())
    list1.append(input1)
  print('Enter values for second list\n')
  for j in range(10):
    input2 = int(input())
    list2.append(input2)
  print(matchList(list1,list2))