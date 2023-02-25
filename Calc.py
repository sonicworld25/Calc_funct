### Define a calculator
def calc(a, b, choice=None):


        if choice=='addition':
             return (a+b)
        elif choice=='subtraction':
             return (a-b)
        elif choice == 'multiplication':
               return (a*b)
        elif choice == 'division':
              return (a/b)
        else:

            return result

def main():





    var_1 = int(input ("Please enter first number \n"))
    var_2 = int(input ("Please enter second number \n"))
    print("The options to chose are 1 is for addition, 2 is for subtraction ,"
          " 3 is for multiplication, 4 is for division\n")
    t = int(input("Please enter your choice between 1-4:\n"))





    try:
          if t==1:
            choice = 'addition'
            result_1= calc (var_1, var_2 ,choice)
            print('The addition result is\n', result_1)
          elif t == 2:

                  choice = 'subtraction'
                  result_2 = calc (var_1, var_2 ,choice)
                  print('Thr subtraction result is\n', result_2)

          elif t == 3:

                  choice = 'multiplication'
                  result_3 = calc(var_1, var_2 ,choice)
                  print('Thr multiplication result is\n', result_3)

          elif t == 4:

                  choice = 'division'
                  if (var_2 ==0 ):
                      print("Calculation not possible , Bye:")
                      exit(0)
                      # break
                  result_4 = calc(var_1, var_2 ,choice)
                  print('Thr division result is\n', result_4)

          else:


                  return
    except :
        print("Error")


main ()