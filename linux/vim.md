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

There are several window commands that allow you to change split window size:

Ctrl+W +/-: increase/decrease height (ex. 20<C-w>+)
Ctrl+W >/<: increase/decrease width (ex. 30<C-w><)
Ctrl+W _: set height (ex. 50<C-w>_)
Ctrl+W |: set width (ex. 50<C-w>|)
Ctrl+W =: equalize width and height of all windows
See also: :help CTRL-W

paste without indentation          -> :set paste

showing line numbers.              -> :set nu / :set number
unshowing line numbers.            -> :set nonu / :set nonumber

stop all terminal output           -> ctrl+s
back to normal.                    -> ctrl+q

get vim version
`vim --version`

