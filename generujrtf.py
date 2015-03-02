#!/usr/local/bin/python
# coding: utf-8

pl_dict = {'ą' :r"\'b9", 
'ć' :r"\'e6", 
'ę' :r"\'ea", 
"ł" :r"\'b3", 
"ń" :r"\'f1", 
"ó" :r"\'f3", 
"ś" :r"\'9c", 
"ź" :r"\'9f", 
"ż" :r"\'bf",
"Ł" :r"\'a3"}

def pl_encode(text):  #Switch polish letters to ansi code
    a = ""
    for i in range(len(text)):
        if (text[i]=="\xc4")  or (text[i]=="\xc5")or (text[i]=="\xc3"):
            a += pl_dict[text[i:i+2]]
        elif text[i-1]=="\xc4" or (text[i-1]=="\xc5") or (text[i-1]=="\xc3"):
            print("420 NOSCOPEBLAZEIT")
        else:
            a+=text[i]
    return a

wejscie = open('listaludzi', 'r')
plik = open("listaludzi.rtf",'w')
plik.write(r'{\rtf1\ansi\deff0\fcharset238' + '\n' + r'{\fonttbl {\f0 Arial;}{\f1 Courier;}}{\colortbl;\red0\green0\blue0;\red0\green255\blue0;\red255\green0\blue255;\red255\green100\blue255;}' + '\n')
for i in range(25):
    plik.write(r"\trowd\trgaph180\clbrdrt\brdrw15\brdrdot\clbrdrl\brdrw15\brdrdot\clbrdrb\brdrw15\brdrdot0\clbrdrr\brdrw15\brdrdot\clcbpat3\cellx4500\clbrdrt\brdrw15\brdrdot\clbrdrl\brdrw15\brdrdot\clbrdrb\brdrw15\brdrdot\clbrdrr\brdrw15\brdrdot\clcbpat4\cellx9000"+'\n'+r"\pard\intbl")
    plik.write(r"\f0\fs30\cf1\ql\b0 Imi\'ea:"+ pl_encode(wejscie.readline())+ ' \\line \n')
    plik.write(r"\f0\fs30\cf1\ql Nazwisko:"+ pl_encode(wejscie.readline())+ ' \\line \n \\par')
    plik.write(r"\pard\intbl\f1\fs24\qr\cf2\b P\'b3e\'e6:"+ pl_encode(wejscie.readline())+ ' \\line \n')
    plik.write(r"\f1\fs24\qr\cf2\b Ur.:"+ pl_encode(wejscie.readline())+ ' \\line \n')
    plik.write(r"\f1\fs24\qr\cf2\b Nr tel.:"+ pl_encode(wejscie.readline())+ '\n \\par')
    wejscie.readline()
    plik.write('\\cell\n')
    plik.write(r"\pard\intbl\cb3\f0\fs30\cf1\ql\b0 Imi\'ea:"+ pl_encode(wejscie.readline())+ ' \\line \n')
    plik.write(r"\f0\fs30\cf1\ql Nazwisko:"+ pl_encode(wejscie.readline())+ ' \\line \n \\par')
    plik.write(r"\pard\intbl\f1\fs24\qr\cf2\b P\'b3e\'e6:"+ pl_encode(wejscie.readline())+ ' \\line \n')
    plik.write(r"\f1\fs24\qr\cf2\b Ur.:"+ pl_encode(wejscie.readline())+ ' \\line \n')
    plik.write(r"\f1\fs24\qr\cf2\b Nr tel.:"+ pl_encode(wejscie.readline())+ '\n \\par')
    wejscie.readline()
    plik.write('\\cell\\row\n')
    
plik.write('}')
plik.close()
