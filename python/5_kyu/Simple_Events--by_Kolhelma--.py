#2021-09-23 13:31:45.932000+00:00
"""Your goal is to write an __Event__ constructor function, which can be used to make __event__ objects.

An __event__ object should work like this:

  - it has a    __.subscribe()__ method, which takes a function and stores it as its handler
  - it has an __.unsubscribe()__ method, which takes a function and removes it from its handlers
  - it has an __.emit()__ method, which takes an arbitrary number of arguments and calls all the stored functions  with these arguments

As this is an elementary example of events, there are some simplifications:
   
  - all functions are called with correct arguments (_e.g._ only  functions will be passed to unsubscribe)
  - you should not worry about the order of handlers' execution
  - the handlers will not attempt to modify an event object (_e.g._ add or remove handlers)
  - the context of handlers'  execution is not important
  - each handler will be subscribed at most once at any given moment of time. It can still be unsubscribed and then subscribed again

Also see an example test fixture for suggested usage"""

class Event():
    def __init__(self):
        self.sub = 0
        self.subs=[]
    
    def subscribe(self, func):
        self.sub +=1
        self.subs.append(func)
        
    def unsubscribe (self, func):
        self.sub -=1
        self.subs.remove(func)
        
    def emit(self, *args):
        for i in self.subs:
            i(*args)