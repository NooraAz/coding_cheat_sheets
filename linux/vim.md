Quitting without saving change     -> :q!
Quitting with saving changes       -> :wq

Going to the end of the file       -> G
Going to line n                    -> nG
Going to the beggining of the file -> gg

move n chars forward               -> nl / n[forward-key]
move n chars backward              -> nh / n[backward-key]
move n lines up                    -> nj / n[up-key]
move n lines down                  -> nk / n[down-key]

move n chars forward (go to next line if this line finished)
                                   -> n[space]
move n chars backward (go to previous line if this line finished)
                                   -> n[backspace]

move cursor Forward full page      -> CTRL+f
move cursor Backwards full page    -> CTRL+b
move cursor Up half page           -> CTRL+u
move cursor Down half page.        -> CTRL+d
move screen so cursor is at Top.   -> zt
move screen so cursor is at Bottom -> zb

center screen on cursor            -> zz 
save document and quit             -> ZZ 

copying the current line           -> yy

deletes the current line.          -> dd
deletes n starting at the cursor   -> ndd 
deletes all lines after the cursor -> dG 

split window horizontal            -> :sp    / ctrl+w+s
split window vertical              -> :vsp   /  ctrl+w+v
moving between split windows       -> crtl+W
split with another file            -> :split file.txt
split with another file vertical   -> :vsplit file.txt

paste without indentation          -> :set paste

showing line numbers.              -> :set nu / :set number
unshowing line numbers.            -> :set nonu / :set nonumber

get vim version
`vim --version`