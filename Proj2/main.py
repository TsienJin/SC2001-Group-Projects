from test.generateTest import GenerateTest


def main():
    obj = GenerateTest(dimension=10, isDirectional=True)
    print(str(obj))
    print(repr(obj))
    obj.printBoth()
    
    
if __name__ == '__main__':
    main()