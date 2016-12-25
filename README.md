# SublimeLinter module for RedPen #

[![Build Status](https://travis-ci.org/taky/SublimeLinter-redpen.svg?branch=master)](https://travis-ci.org/taky/SublimeLinter-redpen)

Copyright (c) 2015-2016 Takahiro Yoshimura <altakey@gmail.com>  
Copyright (c) 2016 Ken Sakurai <sakurai.kem@gmail.com>  

SublimeLinter module for RedPen ( http://redpen.cc/ ).

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
Before installing this plugin, you must ensure that `redpen` is installed on your system. To install `redpen`, download and run `tar.gz` from the [download page](https://github.com/redpen-cc/redpen/releases/). On Mac OS X, the best option is to install [Homebrew](http://brew.sh) and then enter the following in a terminal:

```sh
brew install redpen
```

**Note:** This plugin requires `redpen` 1.7.0 or later.

### Linter configuration
In order for `redpen` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once `redpen` is installed and configured, you can proceed to install the SublimeLinter-redpen plugin if it is not yet installed.

### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `Add Repository`. Among the commands you should see `Package Control: Add Repository`. If that command is not highlighted, use the keyboard or mouse to select it. Since Form will be displayed, enter the following URL.  
```
https://github.com/taky/SublimeLinter-redpen
```

1. Bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that entry is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `redpen`. Among the entries you should see `SublimeLinter-redpen`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.org/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).

You can configure `conf` options by going to: Tools > SublimeLinter > Open User Settings. You may provide a custom config file by setting the linter’s `"conf"` setting to `"conf" : "/path/to/file"`. On Windows, be sure to double the backslashes in the path, for example `"conf" : "C:\\Users\\Aparajita\\redpen.conf"`.

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pydocstyle linters.
- Vertical whitespace helps readability, don’t be afraid to use it.

Thank you for helping out!
