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

# -------- Branch ------------
git branch # show the current branch
git branch --column

# print branches with their heads
git branch -v 

# the history is saved in .git folder. 
# don't change anything other than config file. 

git column

git config gpg.format ssh
git config --global reverse.enabled true # reuse recorded resolution
git config --global column.ui auto
git config --global branch.sort -committerdate

git diff-tree -r <commit-id> # locating the change by commit-id
git diff <branch-name> # difference between current branch and another one
git diff --name-only # only name of files changes
git diff --compact-summary # names of files and number of changes lines in each
git diff --word-diff #word based 
git diff --cached # viewing the changes in staging area


git log --oneline --graph # visualizing branches
git log # getting histrory of changes
git log -p #all previous commits
git log --graph
git log --oneline
git log --grep='example'
git log -S

git checkout $branchname

git revert $commitID

# remove all the changes
git restore 
git restore --staged example.txt # getting back from stage area to untracked

#renaming files
git mv

# making git ignore files
# create a file called .gitignore in root folder
# add pathes that need to be ignored there.

# merge conflict issues (?)

# others
git push --force-with-lease
git push --signed
git maintainance
git maintainance start
git ls-remote
git blame -w
git blame -C
git blame -c-c
git blame -c-c-c
git reflog #log of reerences
git rebase -i
git rev-parse --abbrev-ref HEAD