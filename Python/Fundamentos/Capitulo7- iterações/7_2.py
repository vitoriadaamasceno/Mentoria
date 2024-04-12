def eval_loop():
    while True:
        string=input()
        if string=='done':
            break
        print(eval(string))

eval_loop()