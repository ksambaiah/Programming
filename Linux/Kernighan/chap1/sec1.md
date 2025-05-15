# Linux - Introduction

Linux is an operating system, like any operating system like Windows allows creating files, directories, running programs, creating programs.
It is very different from Windows OS.
It is multi user OS, meaning multiple people can work at the same time. It will protect users killing each other process or doing something bad.
Multiple users can be worked at the same time, it consists of groups and whoever is not part of that group it is called others.

## Basic commands
You need to have username and password and entering during the session is called login
Some simple commands you can type.

 1. date 
 2. who
 3. ls
 4. mkdir directory
 
 ## editor
 There are multiple editors are there common one is vi editor. You can start with 
 vi filename
 There are two modes called command mode and insert mode. Command mode helps to delete lines, words, saving file etc. Insert mode allows writing data to the file.
 If you are in command mode pressing **i** helps going into insert mode. However please move your cursor to the right location and press to go into insert mode.
 Going insert mode to command mode you can press **Esc** key.
 In command mode **:wq** saves the file and quits the editor.

## Commands and options
Most of the commands in Linux comes with options. You can learn options using **man commandname**
ls command options
 1. ls  list of files
 2. ls -t list files based on timestamp
 3. ls -l  most useful command tells it is file or directory, permissions owner, group, size date etc.
 4. mv filename newfilename mv as the name suggests moves one file to another filename.
 5. cat filename may be one of the most useful command you ever use. Cat prints filename on the terminal
 6. cp filename newfilename cp means copy file
 7. rm filename rm stands for remove file

## Filenames 
Filename can be anything but it is ideal not to have space in filenames. It is better to extend filenames with **-** or **_** or **.**. Filename doesn't mean it is particular type like in Windows. Windows file xyz.docx stands for Microsoft document, here any file name you can have.

Note: Create a large file and we will work on that file. Let us call this filename xyz.
You wanted to know no. of lines in xyz, words and charecters.

 - wc xyz. gives no. of lines words, and charecters. wc -l means it only gives lines.
 You wanted to search particular word is appearing in the file. You can do using
 grep word xyz
 grep -v word xyz prints all lines not matching the word.
 
 We will cover some more commands dealing with files.
 tail filename prints last 10 files of the file.
 tail -n 2 xyz prints last 2 lines.
 tail +10 xyz prints file excluding first 10 lines.
 diff file1 file2 is another useful command. It gives differences of file1 and file2
 
