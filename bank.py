a = open('bank.txt','r')
read_file = a.read()
list1 = read_file.split(',')
sum = 0
while True:
     k = """
          1.Total
          2.deposit number
          3.withdraw number
          4.Quit
          """
     print(k)
     c = input('Choose: ')
     deposit_number = 0
     withdraw_number = 0
     for i in list1:
          i = int(i)
          sum +=i
          if i > 0:
               deposit_number += i
          elif i < 0:
               withdraw_number += i
     if c == '1':
          print(sum)
     elif c == '2':
          print(deposit_number)
     elif c == '3':
          print(withdraw_number)   
     elif c == '4':
          break    

     



     
     

          



    


     


     
