to_decode = ".--.--.--.-...-.--....-...-..-.-.------.--...-..-.-.---...--." \
    "--..-.---..-----..-..-...--.-........"

# to_decode = ".--"
# to_decode = ".-.-"

mmap = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '.-.-.-': '.',
    '--..--': ',',
    '---...': ':',
    '..--..': '?',
    '.----.': "'",
    '-....-': '-',
    '-..-.': '/',
    '-.--.-': '(',
    '.-..-.': '"',
    '.--.-.': '@',
    '-...-': '='}

items = tuple((m, char.lower(), len(m)) for m, char in mmap.items())

words = list(
    w.strip().lower() for w in open('/usr/share/dict/words')
    if len(w.strip()) > 2 or w.strip().lower() in ('i', 'a'))
words.append('www')

tree = {'char': '', 'pos': 0, 'children': [], 'parent': None}


def add_nodes(parent):
    pos = parent['pos']
    '''
    chars = []
    par = parent
    while par is not None:
        chars.insert(0, par['char'])
        par = par['parent']
    print(''.join(chars))
    '''
    if pos == len(to_decode):
        chars = []
        par = parent
        while par is not None:
            chars.insert(0, par['char'])
            par = par['parent']
        print(''.join(chars))
    elif pos < len(to_decode):
        children = parent['children']
        chars = []
        par = parent
        while par is not None and par['char'] != ' ':
            chars.insert(0, par['char'])
            par = par['parent']
        w = ''.join(chars)
        if not any(word.startswith(w) for word in words):
            return
        if w in words:
            child = {
                'char': ' ', 'pos': pos, 'children': [], 'parent': parent}
            children.append(child)
            add_nodes(child)
        remainder = to_decode[pos:]
        # print("remainder: ", remainder)
        for morse, alpha, lenalpha in items:
            if remainder.startswith(morse):
                child = {
                    'char': alpha, 'pos': pos + lenalpha, 'children': [],
                    'parent': parent}
                children.append(child)
                add_nodes(child)

add_nodes(tree)
