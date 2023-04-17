Getting size of a directory:

    du -sh <file-path>
    
removing extra " .00" from silent files:

    sed -i 's/ .00//g' *.silent
