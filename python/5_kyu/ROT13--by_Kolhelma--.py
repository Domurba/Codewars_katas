#2021-12-30 14:14:58.636000+00:00
"""How can you tell an extrovert from an
introvert at NSA? Va gur ryringbef,
gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc.
Test examples:
```
rot13("EBG13 rknzcyr.") == "ROT13 example.";
rot13("This is my first ROT13 excercise!" == "Guvf vf zl svefg EBG13 rkprepvfr!"
```"""

def rot13(message):
    msg = []
    for i in message:
        ltr = ord(i)
        if 96 < ltr < 110 or 64 < ltr < 78:
            msg.append(chr(ltr + 13))
        elif 76 < ltr < 91 or 109 < ltr < 123:
            msg.append(chr(ltr - 13))
        else:
            msg.append(i)
    return "".join(msg)