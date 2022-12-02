# CASPaperTunneling

Help you enjoy downloading papers with CAS(Chinese Academy of Sciences) webVPN.

## Feature

- Forget about the annoying webVPN, just download papers(if not exist locally)

- Save downloaded papers to your local disk automatically

- Try to open the downloaded with default pdf reader

## Requirements

```bash
    pip install requests re json # Python 3
```

And a corresponding python interpreter at `#!/usr/local/bin/python3`. You can also modify the interpreter as you wish by just modifying the first line of the script in this repo: `caspt`.

## Install

You can include `~/bin` in your `$PATH`. Then just clone this repo to anywhere and run make install.

```bash
    make install
    # to unistall: make uninstall
```

## Config

- Login to [CAS webVPN](https://webvpn.las.ac.cn) with Chrome. This program will automatically load the cookies from Chrome.

- (Optional) See json config file at `$HOME/.CASPTrc`. Initialized automatically when first run.

## Example

```shell
$ caspt https://journals.aps.org/prb/pdf/10.1103/PhysRevB.101.245139
Does not find the PDF in cache, downloading...
Downloading Finished. opening...

$ caspt https://journals.aps.org/prb/pdf/10.1103/PhysRevB.101.245139
Find the PDF in cache, opening...
```

## Development

There are a lot of features need to be polished, including a more intelligent url process and tests on Windows. Pull requests are very welcome!
