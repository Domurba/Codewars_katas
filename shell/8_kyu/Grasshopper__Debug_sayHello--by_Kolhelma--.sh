#2021-10-10 12:16:47.468000+00:00
"""## Debugging sayHello function

The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard. It is your job to fix the code and get the program working again!

Example output: 
```
Hello, Mr. Spock
```"""

#!/bin/bash 
say_hello(){
   echo 'Hello, '$1;
}
say_hello "$1"