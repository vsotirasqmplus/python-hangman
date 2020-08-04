def what_to_do(instructions):
    size = len(instructions)
    say = 'Simon says'
    say_length = len(say)
    index = instructions.find(say)
    
    if index == 0:
        answer = 'I ' + instructions[say_length + 1:size]
    elif index == size - say_length:
        answer = 'I ' + instructions[0:index]
    else:
        answer = "I won't do it!"
    return answer
