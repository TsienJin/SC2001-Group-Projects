from test.generateTest import GenerateTest


def main():
    obj = GenerateTest(dimension=5, isDirectional=True)
    print(str(obj))
    print(repr(obj))
    print(obj.printBoth())
    
    
if __name__ == '__main__':
    main()