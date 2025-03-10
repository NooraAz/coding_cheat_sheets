# add new session with a name
tmux new -s the_name

# getting all commands in tmux 
tmux list-commands

# entering into a previosly made session (attaching)
tmux attach -t <session_name_or_number>

# killing all sessions
tmux kill-server

# killing one session
tmux kill-session -t <target-session>

# split panes
# horizontal -> ctrl+b "
# vertical   -> ctrl+b %



# all commands
attach-session (attach) [-dEr] [-c working-directory] [-t target-session]
bind-key (bind) [-cnr] [-T key-table] key command [arguments]
break-pane (breakp) [-dP] [-F format] [-n window-name] [-s src-pane] [-t dst-window]
capture-pane (capturep) [-aCeJpPq] [-b buffer-name] [-E end-line] [-S start-line][-t target-pane]
choose-buffer [-N] [-F format] [-f filter] [-O sort-order] [-t target-pane]
choose-client [-N] [-F format] [-f filter] [-O sort-order] [-t target-pane]
choose-tree [-GNsw] [-F format] [-f filter] [-O sort-order] [-t target-pane]
clear-history (clearhist) [-t target-pane]
clock-mode [-t target-pane]
command-prompt [-1Ni] [-I inputs] [-p prompts] [-t target-client] [template]
confirm-before (confirm) [-p prompt] [-t target-client] command
copy-mode [-Mu] [-t target-pane]
delete-buffer (deleteb) [-b buffer-name]
detach-client (detach) [-aP] [-E shell-command] [-s target-session] [-t target-client]
display-message (display) [-p] [-c target-client] [-F format] [-t target-pane] [message]
display-panes (displayp) [-d duration] [-t target-client]
find-window (findw) [-CNT] [-t target-pane] match-string
has-session (has) [-t target-session]
if-shell (if) [-bF] [-t target-pane] shell-command command [command]
join-pane (joinp) [-bdhv] [-p percentage|-l size] [-s src-pane] [-t dst-pane]
kill-pane (killp) [-a] [-t target-pane]
kill-window (killw) [-a] [-t target-window]
last-pane (lastp) [-de] [-t target-window]
last-window (last) [-t target-session]
link-window (linkw) [-dk] [-s src-window] [-t dst-window]
list-buffers (lsb) [-F format]
list-clients (lsc) [-F format] [-t target-session]
list-commands (lscm) [-F format]
list-keys (lsk) [-T key-table]
list-panes (lsp) [-as] [-F format] [-t target-window]
list-sessions (ls) [-F format]
list-windows (lsw) [-a] [-F format] [-t target-session]
load-buffer (loadb) [-b buffer-name] path
lock-client (lockc) [-t target-client]
lock-server (lock)
lock-session (locks) [-t target-session]
move-pane (movep) [-bdhv] [-p percentage|-l size] [-s src-pane] [-t dst-pane]
move-window (movew) [-dkr] [-s src-window] [-t dst-window]
new-session (new) [-AdDEP] [-c start-directory] [-F format] [-n window-name] [-s session-name] [-t target-session] [-x width] [-y height] [command]
new-window (neww) [-adkP] [-c start-directory] [-F format] [-n window-name] [-t target-window] [command]
next-layout (nextl) [-t target-window]
next-window (next) [-a] [-t target-session]
paste-buffer (pasteb) [-dpr] [-s separator] [-b buffer-name] [-t target-pane]
pipe-pane (pipep) [-IOo] [-t target-pane] [command]
previous-layout (prevl) [-t target-window]
previous-window (prev) [-a] [-t target-session]
refresh-client (refresh) [-S] [-C size] [-t target-client]
rename-session (rename) [-t target-session] new-name
rename-window (renamew) [-t target-window] new-name
resize-pane (resizep) [-DLMRUZ] [-x width] [-y height] [-t target-pane] [adjustment]
respawn-pane (respawnp) [-c start-directory] [-k] [-t target-pane] [command]
respawn-window (respawnw) [-c start-directory] [-k] [-t target-window] [command]
rotate-window (rotatew) [-DU] [-t target-window]
run-shell (run) [-b] [-t target-pane] shell-command
save-buffer (saveb) [-a] [-b buffer-name] path
select-layout (selectl) [-Enop] [-t target-pane] [layout-name]
select-pane (selectp) [-DdegLlMmRU] [-P style] [-T title] [-t target-pane]
select-window (selectw) [-lnpT] [-t target-window]
send-keys (send) [-lXRM] [-N repeat-count] [-t target-pane] key ...
send-prefix [-2] [-t target-pane]
set-buffer (setb) [-a] [-b buffer-name] [-n new-buffer-name] data
set-environment (setenv) [-gru] [-t target-session] name [value]
set-hook [-gu] [-t target-session] hook-name [command]
set-option (set) [-aFgosquw] [-t target-window] option [value]
set-window-option (setw) [-aFgoqu] [-t target-window] option [value]
show-buffer (showb) [-b buffer-name]
show-environment (showenv) [-gs] [-t target-session] [name]
show-hooks [-g] [-t target-session]
show-messages (showmsgs) [-JT] [-t target-client]
show-options (show) [-gqsvw] [-t target-session|target-window] [option]
show-window-options (showw) [-gv] [-t target-window] [option]
source-file (source) [-q] path
split-window (splitw) [-bdfhvP] [-c start-directory] [-F format] [-p percentage|-l size] [-t target-pane] [command]
start-server (start)
suspend-client (suspendc) [-t target-client]
swap-pane (swapp) [-dDU] [-s src-pane] [-t dst-pane]
swap-window (swapw) [-d] [-s src-window] [-t dst-window]
switch-client (switchc) [-Elnpr] [-c target-client] [-t target-session] [-T key-table]
unbind-key (unbind) [-an] [-T key-table] key
unlink-window (unlinkw) [-k] [-t target-window]
wait-for (wait) [-L|-S|-U] channel