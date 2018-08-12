Change Log
===

* [ef94583](https://github.com/theadamlt/Sublime-Gitignore/commit/ef945833daa22f088b276061341cfb1c5d9101c3): First commit
* [a5e6cbc](https://github.com/theadamlt/Sublime-Gitignore/commit/a5e6cbcf0d5ab2bb32a6ce4f2b36c62bedd2d050): Completely rewrite of the plug-in
* [bc6e0dc](https://github.com/theadamlt/Sublime-Gitignore/commit/bc6e0dca423fb644ff27413b43e8c9d46cd05116): Add windows support and independence of [gibo](https://github.com/simonwhitaker/gibo)
* [8dc4578](https://github.com/kevinxucs/Sublime-Gitignore/commit/8dc457884b766b0cefc7a270b71cbf6760747817): Fix most of code issue & 
Start to work on `begin_edit` restriction on ST3
* [aa250e9](https://github.com/hadisfr/Sublime-Gitignore/commit/aa250e91bf3f748e2bdf367c7f5575da29d3175f): Use submodule for boilerplates

    The following boilerplates from [9b87ee1](https://github.com/kevinxucs/Sublime-Gitignore/commit/9b87ee16d470c68eda2f2fea4eadb1aa6a1a32f5) seems to be missing from [github/gitignore@ea28c14](https://github.com/github/gitignore/commit/ea28c14da0faf75047165c10223635ba95566ad7):
    * [Bancha.gitignore](boilerplates/Bancha.gitignore) has been removed by [github/gitignore#1192](https://github.com/github/gitignore/pull/1192)
    * [CSharp.gitignore](boilerplates/CSharp.gitignore) has been consolidate into [VisualStudio.gitignore](boilerplates/VisualStudio.gitignore) by [github/gitignore#492](https://github.com/github/gitignore/pull/492)
    * [Compass.gitignore](boilerplates/Compass.gitignore) has been merged to [Sass.gitignore](boilerplates/Sass.gitignore) by [github/gitignore@503bde5](https://github.com/github/gitignore/commit/503bde5d249374a35ea9296ba707af66b03451db) in [github/gitignore#945](https://github.com/github/gitignore/pull/945)
    * [Django.gitignore](boilerplates/Django.gitignore) has been merged into [Python.gitignore](boilerplates/Python.gitignore) by [github/gitignore#473](https://github.com/github/gitignore/pull/473)
    * [IPythonNotebook.gitignore](boilerplates/IPythonNotebook.gitignore) has been deleted due to existence of Jupyter Notebook of [Python.gitignore](boilerplates/Python.gitignore) by [github/gitignore#2172](https://github.com/github/gitignore/pull/2172)
    * [IntelliJ.gitignore](boilerplates/IntelliJ.gitignore) appears in [JetBrains.gitignore](boilerplates/Global/JetBrains.gitignore)
    * [Jython.gitignore](boilerplates/Jython.gitignore) has been merged into [Python.gitignore](boilerplates/Python.gitignore) by [github/gitignore#1493](https://github.com/github/gitignore/pull/1493)
    * [LaTeX.gitignore](boilerplates/LaTeX.gitignore) has been renamed to [TeX.gitignore](boilerplates/TeX.gitignore) in [github/gitignore@81f8222](https://github.com/github/gitignore/commit/81f8222e7fb5b1174b6c83016f0d6c5f28d6abea) by [github/gitignore#832](https://github.com/github/gitignore/pull/832)
    * [Meteor.gitignore](boilerplates/Meteor.gitignore) has been removed by [github/gitignore#1521](https://github.com/github/gitignore/pull/1521)
    * [OSX.gitignore](boilerplates/OSX.gitignore) has been renamed to [macOS.gitignore](boilerplates/Global/macOS.gitignore) by [github/gitignore#2085](https://github.com/github/gitignore/pull/2085)
    * [PhPStorm.gitignore](boilerplates/PhPStorm.gitignore) appears in [JetBrains.gitignore](boilerplates/Global/JetBrains.gitignore)
    * [PyCharm.gitignore](boilerplates/PyCharm.gitignore) appears in [JetBrains.gitignore](boilerplates/Global/JetBrains.gitignore)
    * [Quartus2.gitignore](boilerplates/Quartus2.gitignore) has been removed by [github/gitignore#1193](https://github.com/github/gitignore/pull/1193)
    * [RubyMine.gitignore](boilerplates/RubyMine.gitignore) appears in [JetBrains.gitignore](boilerplates/Global/JetBrains.gitignore)
    * [SASS.gitignore](boilerplates/SASS.gitignore) has been renamed to [Sass.gitignore](boilerplates/Sass.gitignore) by [github/gitignore@503bde5](https://github.com/github/gitignore/commit/503bde5d249374a35ea9296ba707af66b03451db) in [github/gitignore#945](https://github.com/github/gitignore/pull/945)
    * [Symfony2.gitignore](boilerplates/Symfony2.gitignore) has been renamed to [Symfony.gitignore](boilerplates/Symfony.gitignore) in [github/gitignore@5e34ab0](https://github.com/github/gitignore/commit/5e34ab0bc2c0aebc0af0ee1419671043734fc346) by [github/gitignore#1117](https://github.com/github/gitignore/pull/1117)
    * [Target3001.gitignore](boilerplates/Target3001.gitignore) has been removed by [github/gitignore#1190](https://github.com/github/gitignore/pull/1190)
    * [Tasm.gitignore](boilerplates/Tasm.gitignore) has been removed by [github/gitignore#1189](https://github.com/github/gitignore/pull/1189)
    * [VB.Net.gitignore](VB.Net.gitignore) has been consolidate into [VisualStudio.gitignore](boilerplates/VisualStudio.gitignore) by [github/gitignore#492](https://github.com/github/gitignore/pull/492)
    * [vim.gitignore](boilerplates/vim.gitignore) has been renamed to [Vim.gitignore](boilerplates/Global/Vim.gitignore)
    * [webMethods.gitignore](boilerplates/webMethods.gitignore) has been removed. I couldn't find any thing related to it's deletion.

    Some of those deleted files are available at [hadisfr/old-gitignores](https://github.com/hadisfr/old-gitignores).
