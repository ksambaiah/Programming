# Shell

You are typing the commands at the prompt **$**, the process taking your commands and running and providing output is called shell. If Operating system makes you to interact with hardware, shell is responsible for interacting with OS.
You can make the following things in shell, we will cover.

 - Filename shorthand. It is not required to provide all filenames on the shell, we will see you can use what is called regular expressions
 - Input output redirection. You can arrange output of a program to input file and input of a program coming from a file.
 - Environment personalise
 
 ## Regular expressions or patterns
 Suppose you wanted to list files ending with txt but file name can be anything you can run command
 $ls *.txt
 You wanted to list a file start with abc and having only four charecters 
 $ls abc? 
 ? marks only one charecter, * matches any charecter
 [a-c] matches a or b or c
 You wanted to word count all files with extension txt, you know the command
 $wc onefile.txt will do one file and
 $wc *.txt gives output of all files ending with .txt
 
 ### echo
 echo is so useful program it just echo's what you type.
 $echo abcd
 abcd
 $echo *
 lists all files in current directory.
Practice the following commands
 - ls /
 - ls
 - ls *
 - ls '*'
 - echo junk
 - echo /
 - echo
 - echo *
 - echo '*'
 -
 ### Input output redirection
 
 Any program which you run gives output and it directs to terminal. **ls** or **cat** etc. You can run the command
 ```
 $ls > filelist
 ```
 The output of ls is redirected to file filelist rather than standard output and nothing produced on the terminal.
 A symbol **>>** is similar to *>* but here file will be appended. **>** is dangerous too as file already exist it will be created.
