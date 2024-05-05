
#--------------------------------------------------
# some infrastructure
#--------------------------------------------------
# Python-specific code to get a character from the eventStream
def GetChar():
    for character in eventStream: yield character
    yield None # ... when there are no more characters

getchar = GetChar()

START = "start..:" # constants for state names
SPACES = "spaces.:"
LETTERS = "letters:"
END = "end....:"

def quote(argString): return '"' + argString + '"'

#-----------------------------------------------------
# the event-handlers
#-----------------------------------------------------
def handleSpace(c):
    global state, outstring
    if state == START:
        # activities for exiting the current state
        # -- nothing to do when leaving START state
        # change the status to the new state
        state = SPACES
        # activities for entering the new state
        outstring = c
    elif state == SPACES:
        # activities for exiting the current state
        # -- do nothing: new state is same as old state
        # change the status to the new state
        # -- do nothing: new state is same as old state
        # activities for entering the new state
        outstring = outstring + c
    elif state == LETTERS:
        # activities for exiting the current state
        print(state, quote(outstring))
        # change the status to the new state
        state = SPACES
        # activities for entering the new state
        outstring = c

def handleLetter(c):
    global state, outstring
    if state == START:
        # activities for exiting the current state
        # -- nothing to do when leaving START state
        # change the status to the new state
        state = LETTERS
        # activities for entering the new state
        outstring = c
    elif state == LETTERS:
        # activities for exiting the current state
        # -- do nothing: new state is same as old state
        # change the status to the new state
        # -- do nothing: new state is same as old state
        # activities for entering the new state
        outstring = outstring + c
    elif state == SPACES:
        # activities for exiting the current state
        print(state, quote(outstring))
        # change the status to the new state
        state = LETTERS
        # activities for entering the new state
        outstring = c

def handleEndOfInput():
    global state, outstring
    if state == START:
        raise Exception("ERROR: Input stream was empty!")
    else:
        # activities for exiting the current state
        print(state, quote(outstring))
        # change the status to the new state
        state = END
        # activities for entering the new state
        # -- nothing to do to startup END state

#------------------------------------------------
# the driver routine, the event loop
#------------------------------------------------
# Create an eventStream so we can demo the application

eventStream = "Suzy Smith loves John Jones"
state = START # initialize the state-machine in the START state

while True: # do forever: this is the event loop
    c = next(getchar) # en python3 # c = getchar.next() # get the character (event)
    if c == None: # indicates end of the event stream
        print(c)
        handleEndOfInput()
        break # break out of the event loop
    elif c == " ":
        handleSpace(c)
    else: # a "letter" is any non-space character
        handleLetter(c)
