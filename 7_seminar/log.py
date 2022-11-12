def loger(primer, result):
    with open('file7.txt', 'a') as data: # a - создаст файл, если его не будет и запишет в него
        
        rasparse =''.join(map(str,primer))      # соединить список в строку
        rasparse = rasparse + ' = '
        result = str(result) + ' ;\n '            # преобразовываем число в строку
        data.write(str(rasparse))
        data.write(str(result))

       