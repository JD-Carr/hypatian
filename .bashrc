# /root/.bashrc: executed by bash(1) for non-login, interactive shells.
# vim: ft=sh

printf "Welcome %s, from %s\n" "$(whoami)" "$PWD"
printf "Sourced by: %s.\n" "$0"

[[ $- == *i* ]] \
	&& printf "This \e[32mis \e[39man \e[35minteractive\e[39m shell\n" \
	|| printf "This \e[31mis not\e[39m an \e[35minteractive\e39m shell\n"

shopt -q login_shell \
	&& printf "This \e[32mis\e[39m a \e[36mlogin\e[39m shell\n" \
	|| printf "This \e[31mis not\e[39m a \e[36mlogin\e[39m shell\n"

# Disable mail features
shopt -u mailwarn

# Disable all bell styles
set bell-style none

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# General Settings {{{
#------------------------------------------------------------------------------#
# Bash won't get SIGWINCH if another process is in the foreground.
# Enable checkwinsize so that bash will check the terminal size when
# it regains control.
# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# Include dotfiles in wildcard expansion.
shopt -s dotglob

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
shopt -s globstar

# Match wildcards case-insensitively.
shopt -s nocaseglob

shopt -s no_empty_cmd_completion

# Prevent file overwrite on stdout redirection
# Use `>|` to force redirection to an existing file
set -o noclobber

# Vim terminal editing
set -o vi

# set teletype
# 'ixon' enables xon/xoff flow control.
# So as not to be disturbed by Ctrl-S / Ctrl-Q in terminals:
stty -ixon

export BROWSER=/usr/bin/lynx
export EDITOR=/usr/bin/vim
export VISUAL="${EDITOR}"
# }}}

# Bash History {{{
# ignorespace: Don't record lines that start with spaces
export HISTCONTROL=ignorespace

# Set path / filename of bash history file
export HISTFILE=~/.bash_history

# History stored on disk
export HISTFILESIZE=65536

# History stored in memory
export HISTSIZE=1024

# ISO 8601 datetime
export HISTTIMEFORMAT='[%FT%T%:z] '

# Save multiline command as one command
shopt -s cmdhist

# Append to history file, don't overwrite it
shopt -s histappend

# History verification, so that commands matched by ! !! and !? are not automatically executed
shopt -s histverify
# }}}

# Less Settings {{{
export LESS='--LINE-NUMBERS --quit-if-one-screen --no-init --RAW-CONTROL-CHARS --quiet'
export LESSCHARSET=utf-8
export LESSHITSIZE=1024
export LESSHISTFILE=~/.lesshst
# }}}

# Terminal Color Settings {{{
# If .dircolors exist, load them.
[[ -f ~/.dir_colors ]] && eval $(dircolors --bourne-shell ~/.dir_colors)
# }}}

# Bash Aliases Configuration {{{
# If ~/.bash_aliases exist, load them.
[[ -f ~/.bash_aliases ]] && . ~/.bash_aliases
# }}}

# Bash Functions Configuration {{{
# if ~/.bash_functions exists, load it.
[[ -f ~/.bash_functions ]] && . ~/.bash_functions
# }}}

# Bash Aliases {{{
#------------------------------------------------------------------------------#
alias ls='ls --color=auto --sort=extension'
alias ll='ls --color=auto -l --human-readable'
alias lal='ls --color=auto -l --human-readable --all'
alias la='ls --color=auto --almost-all'
alias lf="ls -l | egrep -v '^d'" # files only
alias ldir="ls -l | egrep '^d'" # directories only
# Other way to get dirs
#alias dir='ls --color=auto --directory */'
alias dir='dir --color=auto'
alias vdir='ls --color=auto --indicator-style=slash | grep --invert-match /'

alias egrep='egrep --color=auto --binary-files=without-match --exclude-dir=.git'
alias fgrep='fgrep --color=auto --binary-files=without-match --exclude-dir=.git'
alias grep='grep --color=auto --binary-files=without-match --exclude-dir=.git'

alias mkdir='mkdir --parents --verbose'

alias cp='cp --interactive --verbose'
alias mv='mv --interactive --verbose'
alias rm='rm --interactive --verbose --one-file-system --preserve-root'

alias date='date -u +"%Y-%m-%dT%H:%M:%S%:z"'

# Parenting changing perms on / #
alias chown='chown --preserve-root'
alias chmod='chmod --preserve-root'
alias chgrp='chgrp --preserve-root'

# Fix vi to vim.
alias vi='vim'

# make watch always work with colored input
alias watch='watch --color'
# }}}
