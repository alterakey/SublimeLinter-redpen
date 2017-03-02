# SublimeLinter module for RedPen 

[![Build Status](https://travis-ci.org/taky/SublimeLinter-redpen.svg?branch=master)](https://travis-ci.org/taky/SublimeLinter-redpen)

Copyright (c) 2015-2016 Takahiro Yoshimura <altakey@gmail.com>  
Copyright (c) 2016 Ken Sakurai <sakurai.kem@gmail.com>  

RedPen ( http://redpen.cc/ ) の SublimeLinter module プラグインです。  

## SublimeLinter 3 のインストール
このプラグインを使うには SublimeLinter 3 のインストールが必要になります。SublimeLinter 3 がインストールされていない場合、[こちら](http://sublimelinter.readthedocs.org/en/latest/installation.html)に従ってインストールを行ってください。  

### Redpen のインストール
このプラグインを使う前に、使用しているシステム上に `redpen` がインストールされていることを確認してください。 `redpen` をインストールするには、[ダウンロードページ](https://github.com/redpen-cc/redpen/releases/) から、`tar.gz` をダウンロードし、解凍してください。Mac OS X の場合、[Homebrew](http://brew.sh) を使いターミナル上で、以下のコマンドを入力することで、インストールできます。

```sh
brew install redpen
```

**注意点:** このプラグインは、`redpen` 1.7.0 以降のバージョンで動作確認をしています。

### Redpen の設定
 SublimeLinter で `redpen` を実行するには、SublimeLinter からパスが参照できる必要があります。  
プラグインの実行前に、["Finding a linter executable"](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) "Validating your PATH" の手順を参照し、パスの設定を確認してください。
 
 `redpen` をインストールし、設定が完了後、プラグインが使えるようになります。  

### プラグインのインストール
linter プラグインをインストールするには、[Package Control](https://sublime.wbond.net/installation) を使用してください。
Package Control を使用することで、新しいバージョンが利用可能になったときにプラグインが更新されるようになります。  
ソースからインストールする方法については、ここでは扱いません。  

Package Control を使用してインストールするには、次の手順を実行します。

1. Sublime Text 内で、[Command Palette](http://docs.sublimetext.info/ja/sublime-text-3/extensibility/command_palette.html) を開き、`Add Repository` と入力します。コマンドの中に `Package Control:Add Repository` があります。 そのコマンドが強調表示されていない場合は、キーボードまたはマウスを使用して選択します。  フォームが表示されるので、次の URL を入力します。

```
https://github.com/taky/SublimeLinter-redpen
```

1. [Command Palette](http://docs.sublimetext.info/ja/sublime-text-3/extensibility/command_palette.html) を開き、 `install` と入力します。 コマンドの中には `Package Control:Install Package` があります。 その項目が強調表示されていない場合は、キーボードまたはマウスを使用して選択します。 パッケージコントロールが利用可能なプラグインのリストを取得する間、数秒間の時間がかかります。  

1. プラグインリストが表示されたら、 `redpen` と入力します。 エントリの中に `SublimeLinter-redpen` があります。 その項目が強調表示されていない場合は、キーボードまたはマウスを使用して選択します。  

## プラグインの設定
SublimeLinter の設定に関する一般的な情報は、[Settings](http://sublimelinter.readthedocs.org/ja/latest/settings.html) を参照してください。 一般的な  `linter` 設定の詳細については、[Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html) を参照してください。

Tool > SublimeLinter> Open User Settings に移動して `conf` オプションを設定することができます。 lint の `"conf"` の設定を `"conf" : "/path/to/file"` と設定することで、独自の設定ファイルを読み込むことができます。 Windows では、 `"conf" : "C:\\Users\\Aparajita\\redpen.conf"`  のように、パスのバックスラッシュを二重にしてください。  

## 参加方法
改善や修正に貢献したい場合は、以下に従ってください。  

1. リポジトリを folk します。
1. 最新の `master` から作成された別のトピックブランチをハックします。
1. トピックブランチをコミットしてプッシュします。
1. プルリクエストを行います。
1. 経過を待ってください。 ;-)  

変更は次のコーディングガイドラインに従ってください。  

- インデントは4つのスペースです。
- コードは、flake8 と pydocstyle の linters を渡す必要があります。
- 縦の空白は可読性を向上させるため、積極的に使用してください。  

ありがとう!
