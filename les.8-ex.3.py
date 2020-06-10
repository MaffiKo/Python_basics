class CheckNumbers(Exception):

    @staticmethod
    def lets_check(self):
        numbers = []
        while True:
            try:
                n = int(input('Enter number to list: '))
            except:
                print('not number!')
            else:
                numbers.append(n)
                print(f'The list is {numbers}')
            finally:
                if input('Enter "#" for exit\n') == '#':
                    print(f'Program the end, the list is {numbers}')
                    break


CheckNumbers.lets_check(0)