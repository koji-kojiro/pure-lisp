# Pure Lisp in Pure Python
This repository includes an implementation of **'Pure Lisp'** written in **Pure Python3**. This project is conducted for a learning purpose. When referring this to create your own Lisp, note that there are already so many similar projects.  Most of them may be better than this implementation.

## Usage

```shell
$ make
```

An excutable file named `lisp` will be created.

```shell
$ ./lisp --help
usage: lisp [-h] [-e [ext [ext ...]]] [--list-ext] [file]

positional arguments:
  file                  lisp source code.

optional arguments:
  -h, --help            show this help message and exit
  -e [ext [ext ...]], --ext [ext [ext ...]]
                        enable extensions.
  --list-ext            list avilable extensions.
```

## License
Licensed under [MIT License](LICENSE).

## Author
[TANI Kojiro](https://github.com/koji-kojiro)
