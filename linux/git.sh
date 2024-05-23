# initialize an empty git repository
git init
git remote add origin $url
git push --remote-? origin main

# copying a repo on your local system
# 1. click on code, copy the url
# 2. on your local machine:
git clone $url

# local -> global: stage, commit, push
## staging
git add $filename 
git add . #all changed files
## check status
git status
## commiting
git commit -m "$message"
git commit # for multi line
## pushing
git push 

# show the current branch
git rev-parse --abbrev-ref HEAD
git branch

# the history is saved in .git folder. 
# don't change anything other than config file. 

# locating the change by commit-id
git diff-tree -r <commit-id>

# difference between current branch and another one
git diff <branch-name> 

# only name of files changes
git diff --name-only

# names of files and number of changes lines in each
git diff --compact-summary

# visualizing branches
git log --oneline --graph

# getting histrory of changes
git log
git log -p #all previous commits
git log --graph
git log --oneline
git log --grep='example'

git checkout $branchname

git revert $commitID

# remove all the changes
git restore 
git restore --staged example.txt # getting back from stage area to untracked

#renaming files
git mv

# viewing the changes in staging area
git diff --cached

# making git ignore files
# create a file called .gitignore in root folder
# add pathes that need to be ignored there.

# merge conflict issues (?)