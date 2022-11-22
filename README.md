# freenove-esp32
![checks][checks] ![release][release]
## Table of contents
* [About](#about)
* [Setup](#setup)
  * [Prerequisites](#prerequisites)
  * [Local environment](#local-environment)
  * [ESP32 board(MicroPython, Wi-Fi connection and WebREPL)](#esp32-boardmicropython-wi-fi-connection-and-webrepl)
* [Usage](#usage)
  * [Serial shell](#serial-shell)
    * [Connect](#connect)
    * [Execute string](#execute-string)
  * [WebREPL client](#webrepl-client)
* [Contribute](#contribute)

## About

ESP32 configuration and scripts.

## Setup

### Prerequisites

Hardware - [Freenove ESP32-WROVER dev board][board]. Check [espressif documentation][esp32] if you
have a different board and modify `MICROPYTHON_BINARY` environment variable(`.env` file will be created as part of the `make init` target) accordingly.

Ubuntu 20.04 as host OS, check [documentation](https://github.com/Freenove/Freenove_Ultimate_Starter_Kit_for_ESP32/blob/master/Python/Python_Tutorial.pdf) for CH340 installation instructions for your system.

CLI tools: [direnv][d], [git][g], [poetry][p] and [pre-commit][pk].

You can use [this][a] playbook for automated tools installation.

### Local environment

```shell
git clone git@github.com:cachuperia/freenove-esp32.git
cd freenove-esp32
make init
direnv allow
```

### ESP32 board(MicroPython, Wi-Fi connection and WebREPL)

1. Connect dev board to the USB port, find port name with the help of `make find-port` command and replace `ESP32_PORT` value in the `.env` file.
2. Open `src/freenove_esp32/chip/cfg.py` file and configure variables.
3. Write `MicroPython` binary and code(`src/freenove_esp32/chip` folder) to the chip with the help of `make esp32-init` command. Logs can be downloaded with the help of `make get-logs` command.

Execute `make help` for list of all available commands.

## Usage

### Serial shell

#### Connect

```shell
poetry shell  # activate venv
mpremote  # connect to the serial terminal
# When you see the blank screen, hit Enter and you should be able to get the REPL prompt.
# Press `Ctrl-D` to initiate a soft reboot or `Ctrl-]` for disconnect
```

#### Execute string

```shell
poetry shell  # activate venv
mpremote exec "import network; wlan = network.WLAN(network.STA_IF); wlan.active(True); print(wlan.scan())"
```

For more options, check `mpremote` [documentation][mpremote]. Shortcut for upload all files from the `src/freenove_esp32/chip` folder to the `MicroPython` root folder - `make write-code`

### WebREPL client

You can start local WebREPL client this way:

```shell
git clone https://github.com/micropython/webrepl.git
cd webrepl
firefox webrepl.html
```

## Contribute

Use [Conventional Commits][cc] message style.

Release can be triggered by commit with `feat` or `fix` prefix. Check GitHub [workflow](.github/workflows/release.yml#L13) for details.


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

[board]: https://github.com/Freenove/Freenove_Ultimate_Starter_Kit_for_ESP32
[esp32]: https://www.espressif.com/en/products/socs/esp32
[mpremote]: https://docs.micropython.org/en/latest/reference/mpremote.html
