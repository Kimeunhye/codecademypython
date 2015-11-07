# 6.1
print "Welcome to the English to Pig Latin translator!"

# 6.2
original = raw_input("What's your name?")

# 6.3
original = raw_input("What's your name?")
if len(original) > 0:
    print original
else:
    print "empty"

# 6.4
original = raw_input("What's your name?")
if len(original) > 0:
    if original.isalpha():
     print original
else:
    print "empty"

# 6.5
pyg = 'ay'

# 6.6
yg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    print word
    print first

else:
    print 'empty'

# 6.7
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    new_word = word + pyg
    print new_word

else:
    print 'empty'

# 6.8
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    new_word = word[1:] + word[0] + pyg
    print new_word

else:
    print 'empty'
