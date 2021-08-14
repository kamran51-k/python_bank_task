a = open('bank.txt','r')
read_file = a.read()
list1 = read_file.split(',')
def bank():
     sum = 0
     deposit_number = 0
     withdraw_number = 0
     for i in list1:
          i = int(i)
          sum +=i
          if i > 0:
               deposit_number += i
          elif i < 0:
               withdraw_number += i
     while True:
          k = """
               1.Total
               2.deposit number
               3.withdraw number
               4.Quit
               """
          print(k)
          index_c = input('Choose: ')
          if index_c == '1':
               print(sum)
          elif index_c == '2':
               print(deposit_number)
          elif index_c == '3':
               print(withdraw_number)
          elif index_c == '4':
               break    
print(bank())          




     
     

          



    


     


     
