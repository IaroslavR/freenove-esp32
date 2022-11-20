# freenove-esp32
![checks][checks] ![release][release]
## Table of contents
* [About](#about)
* [Development](#development)
  * [Prerequisites](#prerequisites)
  * [Setup local environment](#setup-local-environment)
  * [Contribute](#contribute)

## About

ESP32 scripts.

Usage:
```shell
pip install git+https://github.com/cachuperia/freenove-esp32.git
freenove-esp32 --help
```

## Development

Release can be triggered by commit with `feat` or `fix` prefix. Check GitHub [workflow](.github/workflows/release.yml#L13) for details.

### Prerequisites

Tools to install: [direnv][d], [git][g], [poetry][p] and [pre-commit][pk].

You can use [this][a] playbook for automated tools installation(Ubuntu only).

### Setup local environment

```shell
git clone git@github.com:cachuperia/freenove-esp32.git
cd freenove-esp32
make init
direnv allow
```
Run `make` for list all available targets.

### Contribute

Use [Conventional Commits][cc] message style.

[a]: https://github.com/IaroslavR/ansible-role-server-bootstrap
[cc]: https://www.conventionalcommits.org/en/v1.0.0/
[d]: https://direnv.net/
[g]: https://www.atlassian.com/git/tutorials/install-git
[p]: https://python-poetry.org/docs/#installation
[pk]: https://pre-commit.com/#install

[checks]: https://github.com/cachuperia/freenove-esp32/actions/workflows/checks.yml/badge.svg
[release]: https://github.com/cachuperia/freenove-esp32/actions/workflows/release.yml/badge.svg

[wch]: .github/workflows/checks.yml
[wr]: .github/workflows/release.yml
