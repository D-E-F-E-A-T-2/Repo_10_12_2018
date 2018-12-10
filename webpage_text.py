from urllib import request

def downloading(url):
    action = request.urlopen(url) #beautifullsoup can be used to get pure text
    readaction = action.read()

    str_readaction = str(readaction)
    lines = str_readaction.split('\\n')

    store = r'webpage_text.txt'

    writing = open(store,'w')

    for line in lines:
        writing.write(line+'\n')

        writing.close


inp=input()
downloading(inp)
