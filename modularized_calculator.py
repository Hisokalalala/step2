from collections import deque


def read_number(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        keta = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta /= 10
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def read_plus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def read_minus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1


def read_multiply(line, index):
    token = {'type': 'MULTIPLY'}
    return token, index + 1


def read_divide(line, index):
    token = {'type': 'DIVIDE'}
    return token, index + 1


def read_open_brakets(line, index):
    token = {'type': 'OPBRAKETS'}
    return token, index + 1


def read_close_brakets(line, index):
    token = {'type': 'CLBRAKETS'}
    return token, index + 1


def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = read_number(line, index)
        elif line[index] == '+':
            (token, index) = read_plus(line, index)
        elif line[index] == '-':
            (token, index) = read_minus(line, index)
        elif line[index] == '*':
            (token, index) = read_multiply(line, index)
        elif line[index] == '/':
            (token, index) = read_divide(line, index)
        elif line[index] == '(':
            (token, index) = read_open_brakets(line, index)
        elif line[index] == ')':
            (token, index) = read_close_brakets(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens


def evaluate_plus_and_minus(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'})  # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print('Invalid syntax')
                exit(1)
        index += 1
    return answer


def evaluate_multiply_and_divide(tokens):
    index = 0
    while index < len(tokens):
        if tokens[index]['type'] == 'MULTIPLY':
            calculated_number = tokens[index - 1]['number'] * tokens[index + 1]['number']
            new_token = {'type': 'NUMBER', 'number': calculated_number}
            del tokens[index - 1:index + 2]
            tokens.insert(index - 1, new_token)
            index -= 1
        elif tokens[index]['type'] == 'DIVIDE':
            if tokens[index + 1]['number'] == 0:
                print("Cannot be divided by 0")
                exit(1)
            else:
                calculated_number = tokens[index - 1]['number'] / tokens[index + 1]['number']
                new_token = {'type': 'NUMBER', 'number': calculated_number}
                del tokens[index - 1:index + 2]
                tokens.insert(index - 1, new_token)
                index -= 1
        elif tokens[index]['type'] == 'PLUS' or tokens[index]['type'] == 'MINUS' or tokens[index]['type'] == 'NUMBER':
            pass
        else:
            print('Invalid syntax!')
            exit(1)
        index += 1
    return tokens


def evaluate(tokens):
    stack = deque()
    ministack = deque()
    index = 0
    while index < len(tokens):
        if tokens[index]['type'] == 'OPBRAKETS' or tokens[index]['type'] == 'NUMBER' or tokens[index]['type'] == 'PLUS' or tokens[index]['type'] == 'MINUS' or tokens[index]['type'] == 'MULTIPLY' or tokens[index]['type'] == 'DIVIDE':
            stack.append(tokens[index])
        elif tokens[index]['type'] == 'CLBRAKETS':
            while True:
                token = stack.pop()
                if token['type'] == "OPBRAKETS":
                    break
                else:
                    ministack.appendleft(token)
            calculated_nums_in_brakets = evaluate_plus_and_minus(evaluate_multiply_and_divide(list(ministack)))
            ministack.clear()
            new_token = {'type': 'NUMBER', 'number': calculated_nums_in_brakets}
            stack.append(new_token)
        else:
            print('Invalid syntax!!')
            exit(1)
        index += 1
    tokens_with_plus_and_minus = evaluate_multiply_and_divide(list(stack))
    answer = evaluate_plus_and_minus(tokens_with_plus_and_minus)
    return answer


def test(line):
    tokens = tokenize(line)
    actualAnswer = evaluate(tokens)
    expectedAnswer = eval(line)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expectedAnswer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")
    test("1+2")
    test("1.0+2.1-3")
    test("3.4+5.6")
    test("2.5+3")
    test("6+3.8")
    test("3-5")
    test("3.6-3.4")
    test("3.84-2.3-1.2")
    test("3*6")
    test("0*3")
    test("3.8*2")
    test("3.8*2.9")
    test("3.8*2.9*3.4*3")
    test("1*2*3")
    test("4/2")
    test("4/2/2")
    test("3.8/1.9")
    test("4*5/10")
    test("4*5/2.5")
    test("1+2*4+5-9/3+8")
    test("1.5+3*2.5-4.8/2.4-4")
    test("(1.4-0.3)*6-(9-7)")
    test("(3.0+4*(2-1))")
    test("(9.9/3-5)*4/(8+(9-7))")
    test("3+((4-7)*8-9)/5")
    test("4.5+(3.4+3)/2*(23-4)")

    test("3.8/0")
    print("==== Test finished! ====\n")


run_test()

while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)
