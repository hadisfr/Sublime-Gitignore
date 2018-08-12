import os
import zipfile

import sublime
import sublime_plugin

loader = None


def plugin_loaded():
    global loader
    loader = Loader()


class Loader():
    _bp_list = []
    _bp_folder = 'boilerplates'
    _package_path = None
    _is_zipfile = False
    _address = {}

    def __init__(self):
        self._find_path()
        self._is_zipfile = zipfile.is_zipfile(self._package_path)
        self._build_list()

    def _find_path(self):
        paths = [os.path.join(sublime.installed_packages_path(), 'Gitignore.sublime-package'),
                 os.path.join(sublime.packages_path(), 'Gitignore'),
                 os.path.join(sublime.packages_path(), 'Sublime-Gitignore')]
        for path in paths:
            if os.path.exists(path):
                self._package_path = path
                break

    def _list_dir(self):
        if self._is_zipfile:
            # Dealing with .sublime-package file
            package = zipfile.ZipFile(self._package_path, 'r')
            path = self._bp_folder + '/'
            return [f for f in package.namelist() if f.startswith(path)]
        else:
            return os.listdir(os.path.join(self._package_path, self._bp_folder))

    def _load_file(self, path):
        if self._is_zipfile:
            # Dealing with .sublime-package file
            package = zipfile.ZipFile(self._package_path, 'r')
            with package.open(path, 'r') as f:
                text = f.read()
            return text
        else:
            file_path = os.path.join(self._package_path, path)
            with open(file_path, 'r') as f:
                text = f.read()
            return text

    def _build_list(self):
        for bp_file in self._list_dir():
            self._address[bp_file.replace('.gitignore', '')] = bp_file
        self._bp_list = list(self._address.keys())
        self._bp_list.sort()

    def get_list(self):
        return self._bp_list[:]  # Copy _bp_list

    def load_bp(self, bp):
        return self._load_file(self._bp_folder + '/' + self._address[bp])


class RungiboCommand(sublime_plugin.WindowCommand):
    def show_quick_panel(self, options, done):
        # Fix from http://www.sublimetext.com/forum/viewtopic.php?f=6&t=10999
        sublime.set_timeout(lambda: self.window.show_quick_panel(options, done), 10)

    def run(self):
        self.chosen_array = []
        self.bp_list = loader.get_list()
        self.is_first = True
        self.show_quick_panel(self.bp_list, self.on_select)

    def on_select(self, index):
        if not self.is_first and index == 0:
            self.write_file()
        elif index >= 0:
            self.chosen_array.append(self.bp_list[index])
            self.bp_list.remove(self.bp_list[index])
            if self.is_first:
                self.bp_list.insert(0, 'Done')
                self.is_first = False
            self.show_quick_panel(self.bp_list, self.on_select)

    def write_file(self):
        final = ''

        for bp in self.chosen_array:
            text = loader.load_bp(bp)
            final = final + '### ' + bp + ' ###\n\n' + text + '\n\n'

        final = final.strip()
        final += '\n'
        view = sublime.active_window().new_file()
        view.run_command('writegibo', {'bp': final})


class WritegiboCommand(sublime_plugin.TextCommand):

    def run(self, edit, **kwargs):
        self.view.insert(edit, 0, kwargs['bp'])
        self.view.set_name('.gitignore')
        self.view.set_syntax_file('Packages/Git Formats/Git Ignore.sublime-syntax')
