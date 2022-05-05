# -*- coding: utf-8 -*-

MAX_VAL = 255
MIN_VAL = 0

def append_memory_value(memory, pointer):
    if len(memory) == pointer:
        memory += [0]
    return memory, pointer

def prepend_memory_value(memory, pointer):
    if pointer < 0:
        memory = [0] + memory
        pointer += 1
    return memory, pointer

def is_max_val(val):
    return True if val == MAX_VAL else False
       
def is_min_val(val):
    return True if val == MIN_VAL else False

def right(memory, pointer):
    pointer += 1
    memory, pointer = append_memory_value(memory, pointer)
    return memory, pointer

def left(memory, pointer):
    pointer -= 1
    memory, pointer = prepend_memory_value(memory, pointer)
    return memory, pointer

def up(memory, pointer):
    if is_max_val(memory[pointer]):
        memory[pointer] = 0
    else:
        memory[pointer] += 1
    return memory, pointer

def down(memory, pointer):
    if is_min_val(memory[pointer]):
        memory[pointer] = 255
    else:
        memory[pointer] -= 1
    return memory, pointer

def bump_right(memory, pointer, instructions, index):
    if memory[pointer] == 0:
        needed_bumps = 0
        while True:
            index +=1
            current_instruction = instructions[index]
            if instructions[index] == '🤛':
                if needed_bumps == 0:
                    break
                needed_bumps -= 1
            elif instructions[index] == '🤜':
                needed_bumps += 1
    return index

def bump_left(memory, pointer, instructions, index):
    if memory[pointer] != 0:
        needed_bumps = 0
        while True:
            index -= 1
            current_instruction = instructions[index]
            if current_instruction == '🤜':
                if needed_bumps == 0:
                    break
                needed_bumps -= 1
            elif current_instruction == '🤛':
                needed_bumps += 1
    return index

def bump(memory, pointer):
    print(chr(memory[pointer]), end='')

def decipher_instructions(instructions):
    pointer = 0
    memory = [0]
    index = 0

    while index < len(instructions):
        current_instruction = instructions[index]
        if current_instruction in movements_dict.keys():
            memory, pointer = movements_dict[current_instruction](memory, pointer)
        elif current_instruction in nest_dict.keys():
            index = nest_dict[current_instruction](memory, pointer, instructions, index)
        elif current_instruction in print_dict.keys():
            print_dict[current_instruction](memory, pointer)
        index +=1

    print()

movements_dict = {
    '👉': lambda x,y: right(x,y),
    '👈': lambda x,y: left(x,y),
    '👆': lambda x,y: up(x,y),
    '👇': lambda x,y: down(x,y),

}

nest_dict = {
    '🤜': lambda x, y, z, w: bump_right(x, y, z, w),
    '🤛': lambda x, y, z, w: bump_left(x, y, z, w),
}

print_dict = {
    '👊': lambda x, y: bump(x,y)
}

def main():

    instructions = "👇🤜👇👇👇👇👇👇👇👉👆👈🤛👉👇👊👇🤜👇👉👆👆👆👆👆👈🤛👉👆👆👊👆👆👆👆👆👆👆👊👊👆👆👆👊"
    decipher_instructions(instructions)

    instructions = "👉👆👆👆👆👆👆👆👆🤜👇👈👆👆👆👆👆👆👆👆👆👉🤛👈👊👉👉👆👉👇🤜👆🤛👆👆👉👆👆👉👆👆👆🤜👉🤜👇👉👆👆👆👈👈👆👆👆👉🤛👈👈🤛👉👇👇👇👇👇👊👉👇👉👆👆👆👊👊👆👆👆👊👉👇👊👈👈👆🤜👉🤜👆👉👆🤛👉👉🤛👈👇👇👇👇👇👇👇👇👇👇👇👇👇👇👊👉👉👊👆👆👆👊👇👇👇👇👇👇👊👇👇👇👇👇👇👇👇👊👉👆👊👉👆👊"
    decipher_instructions(instructions)

if __name__ == "__main__":
    main()
