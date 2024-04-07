from line_hw4 import draw_line_string as line

def welcome_message(msg1, msg2):
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    line(nstr)
    print(f' {msg1}')
    print(f' {msg2} ')
    line(nstr)
    
travler_name = input('Input his/her name:')
travler_name_1 = 'Hello ' + travler_name +','
welcome_to_Seoul = 'Welcome to Seoul.'
welcome_message(travler_name_1, welcome_to_Seoul)

