import sublime
import sublime_plugin


class DuplicateLineBelowCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command('duplicate_line')
        self.view.run_command('swap_line_up')