userMessage = "привет"

userMessageEnc=userMessage.encode('utf-8')
print(userMessageEnc)

userMessageDec=userMessageEnc.decode('utf-8')
print(userMessageDec)

print(id(userMessage))
print(type(userMessage))
print(userMessage)

myStr4='''This is a multi-line string (text).
 This is the first line of text.
 This is the second line of text.
 This is the third line of text with 'quotes'
 '''
print(myStr4)

myStj="foobar"
print(myStj[0])
print(myStj[1])
print(len(myStj)-1)
print(myStj[-1])
print(myStj[-2])

myStr="Hello"
print(myStr*5)
myBigStr=myStr*5
print(myBigStr)

