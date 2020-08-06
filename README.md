# Sublime Text 2 and 3 Gitignore Plug-in

Sublime Text 2 and 3 plug-in for fetching gitignore boilerplates from [the collection of gitignore boilerplates by Github](https://github.com/github/gitignore)

## How it works

Press `Cmd + Shift + P` for Mac and `Ctrl + Shift + P` for Linux/Windows.
Write `Gitignore` and select `Gitignore: new gitignore`.
Then select the desired gitignore boilerplate.
Now select another boilerplate. When you are done, select `Done`.
Save the newly open file as `.gitignore` and your done!

## User-defined Boilerplates

You can add your own `*.gitignore` files to `Packages/User/gitignores` directory to use them via Gitignore Plug-in.
You may need to restart sublime text to load new boilerplates.

User-defined boilerplates override default ones with the same name.

You can find some old gitignore boilerplates at [hadisfr/old-gitignores](https://github.com/hadisfr/old-gitignores).

## Installation

### Install via Package Control

[Install Package Control](https://packagecontrol.io/installation),
then press `Cmd + Shift + P` for Mac and `Ctrl + Shift + P` for Linux/Windows,
select `Package Control: Install Package`,
and select `Gitignore`.

### Manual Install

#### Linux

```bash
git clone https://github.com/kevinxucs/Sublime-Gitignore ~/.config/sublime-text-3/Packages/Gitignore
```

#### Windows

```bash
git clone https://github.com/kevinxucs/Sublime-Gitignore %APPDATA%/Sublime\ Text\ 3/Packages/Gitignore
```


#### Mac

```bash
git clone https://github.com/kevinxucs/Sublime-Gitignore ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Gitignore
```

#### Update Boilerplates

```bash
git subtree pull --prefix boilerplates/ https://github.com/github/gitignore.git master --squash
```
