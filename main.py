from os import system

def clear():
    system('clear')

def get_string(f_name):
    with open(f_name, 'r') as file_obj:
        string = file_obj.read()
    return string # leave string with linebreaks

def decompress_triplet(t): return int(t[:2])*t[2]

def compress_string(s): return ('0' if len(s) < 10 else '') + str(len(s)) + s[0]

def rle_ascii(string):
    """
    RLE -> ASCII
    Expects correct RLE
    Returns decompressed string.
    """
    string = string.strip('\n').split('\n') # format string + split by newline
    new_string=[]
    for line in string:
        new_string.append('')
        for i in range(0, len(line), 3):
            triplet = line[i:i+3] # split string line to triplet
            triplet = decompress_triplet(triplet) # then decompress
            new_string[-1] += triplet # then add to decompressed string
    return '\n'.join(new_string)

def ascii_rle(string):
    """
    ASCII -> RLE
    Returns compressed string.
    """
    string = string.strip('\n').split('\n') # format string + split by newline
    compressed = []
    for line in string:
        compressed.append('')
        
        first_index=0
        for char, index in zip(line, range(len(line))):
            if index == len(line)-1:
                next_char=None # if it reaches the end of line make it impossible to match
            else: next_char = line[index+1] # set the next char

            if char == next_char:
                continue

            compressed[-1] += compress_string(line[first_index:index+1]) # compress the string of repeated chars and add to compressed
            first_index = index+1
    
    return '\n'.join(compressed) # join the list to make string

def enter(msg=''):
    input(msg+'\nPress enter to continue...')
    clear()

def main():
    print('Select option by inputting corresponding number.')
    for o, n in zip(['Enter RLE', 'Display ASCII art', 'Convert to ASCII art', 'Convert to RLE', 'Quit'], range(5)):
        print(f'{n}) {o}')
    choice = input('#~>')
    try:
        choice = int(choice)
    except:
        enter('Enter one of the numbers shown!')
        return True

    if choice == 0: # Enter RLE
        n = None
        while n == None or n < 3:
            if n!=None:
                enter('Enter an integer greater than 2!')
            print('How many lines will you enter? (must be more than 2)')
            try:
                n = int(input('#~>'))
            except:
                n = 0
        rle = ''
        for x in range(n):
            rle+=input(f'Line {x}: ') + '\n'
        enter(rle_ascii(rle))

    elif choice == 1: # Display ASCII art
        print('Enter name of txt:')
        f = input('#~>')
        enter(get_string(f))

    elif choice == 2: # Convert to ASCII art
        print('Enter name of txt:')
        enter(rle_ascii(get_string(input('#~>'))))
    
    elif choice == 3: # Convert to RLE
        print('Enter name of ASCII txt:')
        f_name = input('#~>')
        raw = get_string(f_name)
        compressed = ascii_rle(raw)
        diff = len(raw) - len(compressed) # calculate difference
        with open('RLE_'+f_name, 'w+') as f:
            f.write(compressed)
        enter(f'Compression saves {diff} characters!')
    
    elif choice == 4: # Quit
        return False # break the main loop
    
    else:
        enter('Enter one of the numbers shown!')
    
    return True

if __name__=="__main__":
    while main():
        continue
    print('Goodbye!')
