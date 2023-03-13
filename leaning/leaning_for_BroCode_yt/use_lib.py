# Module = a file containing python code. May contain function, classes, etc. ..
# Used with modular programming, which is to separate a program into parts

import messages

messages.hello()
messages.bye()

import messages as msg
msg.hello()
msg.by()

from messages import hello,by
hello()
bye()

from messages import *

hello()
bye()

