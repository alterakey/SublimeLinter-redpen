# linter.py: Entrypoint.
# Copyright (c) 2015 Takahiro Yoshimura <altakey@gmail.com>

"""This module exports the RedPen plugin class."""

from SublimeLinter.lint import Linter, persist


class Redpen(Linter):

    """Provides an interface to RedPen."""

    syntax = ('plain text', 'markdown', 'wiki')
    executable = 'redpen-sublimelinter'

    # We are missing out on some errors by ignoring multiline messages.
    regex = (
        r'^<stdin>:(?P<line>\d+):(?P<col>\d+): '
        r'(?:(?P<error>(error|fatal error))|(?P<warning>warning)): '
        r'(?P<message>.+)'
    )

    defaults = {
        'extra_flags': ""
    }

    base_cmd = (
        'redpen-sublimelinter '
    )

    def cmd(self):
        """
        Return the command line to execute.
        """

        result = self.base_cmd

        try:
            result += ' -%s ' % {
                'plain text':'p',
                'markdown':'m',
                'wiki':'w'
            }[persist.get_syntax(self.view)]
        except KeyError:
            pass

        settings = self.get_view_settings()
        result += settings.get('extra_flags', '')

        return result
