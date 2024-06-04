#!bin/bash/ 
# Getting the size of a directory:
du -sh <file-path>
    
# removing extra " .00" from silent files:
# -i writes back changes to the file
sed -i 's/ .00//g' *.silent
sed -i '' -e 's/ .00//g' *.silent  # on OS X

# removing first line of all files
sed -i '1d' SMD_* 

# remove all line beginning with #
sed -i '/^#/d' filepath

# loop + unzip 
for i in {1..10}; do tar -xzf file$i.tar.gz; done

# loop (multiple line)
for i in 1 2 3 4 5
do
echo "Hello $i"
done

# loop range of numbers with steps (from 0 to 10, step size = 2)
for i in `seq 0 2 10`; do echo $i; done

#------- List / ls --------
# list the first 10 files 
ls *.err | head -10

# list hidden files
ls -la | more

# list all python installed packages
pip list

# list, sorted by ...
ls	    #by name, alphabetical order (1 < 11 < 2)
ls -r	# reverse 
ls -U	# no order
ls -v	# by name, natural order (1 < 2 < 11)
ls -S	# by size, largest first
ls -X	# by extension, alphabetically
ls -t	# by last modification date (mtime), newer first
ls -c	# by last change date (ctime), newer first
ls -u	# by last access date (atime), newer first

# list the number of files in a directory
ls -1 | wc -l
ls *.pdb | wc -l

#------- Cast / cat -------
# cast the number of columns in a file
cat file.txt | awk '{print NF; exit}'

# cast the second line of a file
cat file.txt | awk 'FNR == 2 {print}'

# cast the second column of a file
cat file.txt | awk '{print $2}'

# lines with 32 columns
awk ' { if (NF==32) { print } } ' score.fsc

# merging files
cat *.txt > merged_resloops.txt
# merging silent files
head -3 ab_1000.silent > ../concat.silent #header from one file
tail -q -n+4 *.silent >> ../concat.silent #data from all files

# extracting silent from silent
head -3 concat.silent > concat-rms10.silent
awk ' { if ($27<=10) { print $32} } ' score-20k-32row.fsc | while read line; do grep $line concat.silent >> concat-rms10.silent ; done


# cast all shells
cat /etc/shells

#------- Find / find ------

# find a file or directory (it searches subdirectories by default)
find <path> -type d -name dirname                  # directory
find <path> -type f -name filename                 # file 

# check if a file or directory exists
test -d /etc && echo "True".                # directory
test -f /etc/resolv.conf && echo "True"     # file

-f filename
    
#------- Transfer / scp -----

# file transfer
scp remote_username@server:<file-path> file.txt


#------- Creat / touch ----

# Create a file
touch <file-name>

# Create an empty file
fallocate -l 1GB <file-name>

# make the .sh file executable 
chmod +x <file-name.sh>

# print 
echo "hello world"

#-------- other ----------

# wait (seconds)
sleep 10 

Searching in multiple files or a directory

    grep 'keyword' *.pdb

Cat > file.txt : get output
ctrl+D come out of file

append, instead of rewriting
Cat >> file.txt
"Text" >> file


#commenting

: ‘ multi line commenting’

Cat << heredoctext
This is text
New line
Heredoctext

Count = 10 (variable)
If [ $count -eq 10 ] (if count == 10) (( > < ))  [ "$count" -eq -gt -lt] && 
Then
		Echo "true"
Elif ((----- ))
Then

Else
		Echo "false"
Fi


Cancel all running jobs:

scancel -u $USER


list files with specific extension:
ls | grep .txt


Reverse the commit (recover files)
git reset --hard HEAD~1


Define a function
Function name()
{
	Echo "hello"
}


Calling the function
name


Pass an argument to function
Function name()
{
	Echo "hello $1 $2"
}

name noora azadvari


After calling a function, its variables become global.

Make a folder
mkdir foldername
mkdir -p foldername


Get a input from terminal and save it in a variable
read variable


Check if a directory exists
-d $foldername


Read from a file
Whie IFS="" read -r line
do
	Echo "$line"
done < $fileName


remove/delete a file
rm $fileName


remove/delete a folder
rm -r $folderName


Download a file with original file name
url = ""
curl ${url} -O


Download a file
url = ""
curl ${url} -o NewName


url = ""
curl ${url} > NewName


Download the header of a file
url = ""
curl -I ${url}


Selection menu
select variable in option1 option2
do 
echo "select $variable"
done 


Switch
select variable in option1 option2
do 
case $variable in 
option1)
echo "select option1";;
option1)
echo "select option1";;
*)
echo "error";;
esac
done 


ctrl c is used to kill a process. It terminates your program. 
ctrl z is used to pause the process. It will not terminate your program, it will keep your program in the background.




Show all running jobs
jobs


Resume a job a background 
bg %1 #job number 1


bg %abc #refers to a job started by a command beginning with abc


bg %?abc  #refers to a job started by a command containing abc


bg %-- #specifies the previous job


Bring a job to foreground 
fg #like bg


Screen
Sudo yum install screen #installing


Tmux
tmux -V #version of tmux


Open a new tmux window
tmux 


ctrl+b+? → showing binding keys → q → quit
ctrl+b+c → create a new window
ctrl+b+window number → switch between windows
ctrl+b+, → rename window
ctrl+b+n → go to the next window
ctrl+b+n → go to the previous window
ctrl+b+l → go to the last used window
ctrl+b+& → close the window
ctrl+b+” → split window horizontally
ctrl+b+o → switch between panes
ctrl+b+% → split window vertically
ctrl+b+arrow keys → move between panes
ctrl+b+; → move last used panes
ctrl+b → ctrl+o → reorder panes
ctrl+b → ctrl+arrow → resize panes
ctrl+b+! → make pane full window
ctrl+b+t → show clock
ctrl+b+x → close pane
ctrl+b+d → detach

See what is running while detached
tmux ls


Attach to a tmuc session
tmux attach -t $DESIGNATION


ctrl+b+$ → rename the session

Kill a session
tmux kill-session -t $DESIGNATION

# version of linux
cat /etc/os-release

