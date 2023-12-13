# braille_converter.py
def text_to_braille(text):
    braille_mapping = {
        'a': '⠁', 'ă': '⠜', 'â': '⠡', 'b': '⠃', 'c': '⠉',
        'd': '⠙', 'đ': '⠮', 'e': '⠑', 'ê': '⠣', 'f': '⠛',
        'h': '⠓', 'i': '⠊', 'k': '⠅', 'l': '⠇', 'm': '⠍',
        'n': '⠝', 'o': '⠕', 'ô': '⠹', 'ơ': '⠪', 'p': '⠏',
        'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞', 'u': '⠥',
        'ư': '⠳', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
        'z': '⠵', 
        
        'A': '⠨ ⠁', 'Ă': '⠨ ⠜', 'Â': '⠨ ⠡', 'B': '⠨ ⠃', 'C': '⠨ ⠉',
        'D': '⠨ ⠙', 'Đ': '⠨ ⠮', 'E': '⠨ ⠑', 'Ê': '⠨ ⠣', 'F': '⠨ ⠛',
        'H': '⠨ ⠓', 'I': '⠨ ⠊', 'K': '⠨ ⠅', 'L': '⠨ ⠇', 'M': '⠨ ⠍',
        'N': '⠨ ⠝', 'O': '⠨ ⠕', 'Ô': '⠨ ⠹', 'Ơ': '⠨ ⠪', 'P': '⠨ ⠏',
        'Q': '⠨ ⠟', 'R': '⠨ ⠗', 'S': '⠨ ⠎', 'T': '⠨ ⠞', 'U': '⠨ ⠥',
        'Ư': '⠨ ⠳', 'V': '⠨ ⠧', 'W': '⠨ ⠺', 'X': '⠨ ⠭', 'Y': '⠨ ⠽',
        'Z': '⠨ ⠵', 

        '': '⠾', '́': '⠈', '̀': '⠘', '̉': '⠐',
        '̃': '⠰', '̣': '⠂', 
        ':': '⠒', ',': '⠂', ';': '⠆','.': '⠲','!': '⠖', '?': '⠢',
        
        '(': '⠣', ')': '⠜', 
        '+': '⠋', '-': '⠤','x': '⠦', '/': '⠲', '=': '⠶', '<': '⠪', '>': '⠕',


        '0': '⠼ ⠚', '1': '⠼ ⠁', '2': '⠼ ⠃', '3': '⠼ ⠉', '4': '⠼ ⠙',
        '5': '⠼ ⠑', '6': '⠼ ⠋', '7': '⠼ ⠛', '8': '⠼ ⠓', '9': '⠼ ⠊'
    }

    braille_result = ''
    for char in text:
        braille_result += braille_mapping.get(char, char)
    return braille_result

