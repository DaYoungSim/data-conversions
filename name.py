with open('name.txt') as f:
    my_name = f.read()


sentence = "Hello, my name is " + my_name
print my_name
print sentence

with open('hello2.txt', 'w') as f:
    f.write(sentence)
    f.write('\n')
    f.write('This file has names from name.txt')