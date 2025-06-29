import calculator

def test():
    print(calculator.add(10,10))
    print(calculator.substract(12, 2))
    
    try:
        print(calculator.divide(10,0))
    except Exception as e:
        print(f"woops, error, {e}")
    

test()