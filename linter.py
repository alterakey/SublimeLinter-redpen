# linter.py: Entrypoint.
# Copyright (c) 2015-2016 Takahiro Yoshimura <altakey@gmail.com>
# Copyright (c) 2016 Ken Sakurai <sakurai.kem@gmail.com>

"""This module exports the RedPen plugin class."""

from SublimeLinter.lint import Linter, persist, util
import os.path
import json


class Redpen(Linter):
    """Provides an interface to RedPen."""

    syntax = ('plain text', 'markdown', 'wiki', 'javaproperties', 'latex', 'asciidoc')
    executable = 'redpen'
    error_stream = util.STREAM_STDOUT
    defaults = {
        'conf': '',
    }
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.7.0'

    def cmd(self):
        """Return the command line to execute."""
        command = [self.executable, '--result-format', 'json', '--format']
        try:
            file_format = {'plain text': 'plain',
                           'markdown': 'markdown',
                           'wiki': 'wiki',
                           'javaproperties': 'properties',
                           'latex': 'latex',
                           'asciidoc': 'asciidoc',
                           }[persist.get_syntax(self.view)]
            command.append(file_format)
        except KeyError:
            raise KeyError('Illegal syntax. \'{}\''.format(self.view))

        settings = self.get_view_settings()
        conf_file_path = settings.get('conf', '')
        if conf_file_path != '':
            if os.path.exists(conf_file_path):
                command.append('--conf')
                command.append(conf_file_path)
            else:
                persist.printf('ERROR: Config file is not exist. \'{}\''.format(conf_file_path))
        command.append('@')
        return command

    def find_errors(self, output):
        """
        Convert json output into a set of matches SublimeLinter can process.

        Redpen 's warning output format is a plain text format, it will be one line or multiple lines.
        Since this behavior is difficult to handle in processing with regular expressions,
        we will treat the warning output format as JSON.
        """
        data = json.loads(output)
        data = data[0]
        for error_json in data.get("errors", []):
            yield self.split_match(error_json)

    def split_match(self, error_json):
        """Mapping the dictionary in the warning list to the screen display Taple."""
        if "startPosition" in error_json:
            start_position = error_json.get("startPosition", {})
            col = start_position.get("offset", None)
            line_num = start_position.get("lineNum", None)
        else:
            col = None
            line_num = error_json.get("lineNum", None)

        return error_json.get("sentence",
                              None), None if line_num is None else line_num - 1, col, True, None, error_json.get(
            "message", ""), None
