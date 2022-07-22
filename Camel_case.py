# Converts dash('-') and underscore('_') delimited words into camel casing.
#  The first word within the output should be capitalized only if the original word is capitalized


def camelCase(punc,text):

    if punc != '':
        text = text.split(punc)
        camelword = text[0]
        
        for letter in text[1:]:
            letter = letter.capitalize()
            camelword+=letter
    
    else:
        camelword = text

    print(camelword)


def auth(text):
    if '-' in text:
        punc = '-'

    elif '_' in text:
        punc = '_'

    else:
        punc = ''


    camelCase(punc,text)
    


auth(
    "how-are-you-today"
)

auth("Lawal is here")
print("lawal".capitalize())
        
