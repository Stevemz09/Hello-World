from program23 import translate
from storytext import text

mynewdict={'wolf':'Fish','Tap':'BOOM!'}
new_text=translate(text,mynewdict).split('.')
for sentence in new_text:
    print(sentence,end='.\n')

