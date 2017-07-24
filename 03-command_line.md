# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> >
* `pwd` show current working directory path
* `mkdir` creating a directory
* `rmdir` deleting a directory
* `touch` creating a file
* `rm` deleting a file
* `mv` renaming a file
* `ls -a` listing hidden files
* `cp` copying a file from one directory to another
* `cd` changing directory
* `ls` listing files and directories
* `cat` printing the contents of a file within the Terminal
* `grep` "global regular expression print", finding things inside files (case sensitive)
* `man` reading a manual page
* `env` returning a list of the environment variables for the current user
* `echo` printing arguments
* `export` exporting or setting a new environment variable
* `exit` exiting the Terminal
* `sort` sorting files / directories in alphabetical order
* `sed` "stream editor" - similar to find and replace
* `source` activating the changes made to a file in the current session
* `history` printing a history of Terminal commands from the current session
---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> >
`ls`  lists all files and directories in the working directory
`ls -a`  lists all contents of a directory including hidden files and directories
`ls -l`  lists all contents of a directory in long format
`ls -lh`  lists all contents of a directory in long format with readable file size
`ls -lah`  lists all contents of a directory (including hidden files) in long format with readable file size
`ls -t`  lists all files and directories, ordered by the time they were last modified
`ls -Glp` lists contents of a directory in long format, colorized output enabled, and displays directories with /

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> >
`ls -R` displays subdirectories as well
`ls -S` sort by file size
`ls -1` displays each entry on a line
`ls -m` displays the names as a CSV
`ls *.txt` list only text files with wildcard
---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` reads data from the standard input and executes the command with the data as arguments. Delimiters are space, tab, newline and end-of-file. If no command is supplied as argument to `xargs` the default command is `echo`.
