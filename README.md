# Sublime Text 2 and 3 Gitignore Plug-in

Sublime Text 2 and 3 plug-in for fetching gitignore boilerplates from [the collection of gitignore boilerplates by Github](https://github.com/github/gitignore)

## How it works

Press `Cmd + Shift + P` for Mac and `Ctrl + Shift + P` for Linux/Windows.
Write `Gitignore` and select `Gitignore: new gitignore`.
Then select the desired gitignore boilerplate.
Now select another boilerplate. When you are done, select `Done`.
Save the newly open file as `.gitignore` and your done!

## Installation

### Install via Package Control

[Install Package Control](https://packagecontrol.io/installation),
then press `Cmd + Shift + P` for Mac and `Ctrl + Shift + P` for Linux/Windows,
select `Package Control: Install Package`,
and select `Sublime-Gitignore`.

### Manual Install

#### Linux

```bash
git clone https://github.com/kevinxucs/Sublime-Gitignore ~/.config/sublime-text-2/Packages/Gitignore
git submodule update --init --recursive
```

#### Windows

```bash
git clone https://github.com/kevinxucs/Sublime-Gitignore %APPDATA%/Sublime\ Text\ 2/Packages/Gitignore
git submodule update --init --recursive
```


#### Mac

```bash
git clone https://github.com/kevinxucs/Sublime-Gitignore ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/Gitignore
git submodule update --init --recursive
```
