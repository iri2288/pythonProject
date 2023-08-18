import turtle as t
command = input('Put command')
while command != 'q':
        match command: # выбор пунктов меню
         case 'r':
            print('Turn to the right')
            t.left(100)
         case 'l':
            print('Turn to the left')
            t.right(100)
         case 'f':
            print('Go to forward')
            t.forward(100)
           #case 'q':
           # print('Bye!')
           # break
         case _:
            print('Give a correct command')

        print('Bye!')