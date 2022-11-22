"""This file is executed on every boot (including wake-boot from deepsleep)."""
import helpers.cfg as cfg

if cfg.CONNECT_WIFI:
    from helpers import WiFi

    wifi = WiFi()
    wifi.connect(cfg.WIFI_NETWORK, cfg.WIFI_NETWORK_PASSWORD)

if cfg.CONNECT_WIFI and wifi.connected and cfg.WEB_REPL:
    import webrepl

    webrepl.start(password=cfg.WEB_REPL_PASSWORD)
