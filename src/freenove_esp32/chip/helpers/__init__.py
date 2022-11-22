"""ESP32 helpers."""
from time import sleep_ms

from helpers.logger import get_logger

logger = get_logger(__name__)


class WiFi:
    """Wi-Fi connection wrapper."""

    def __init__(self) -> None:
        import network

        self.wlan = network.WLAN(network.STA_IF)

    def on(self) -> None:
        """Enable Wi-Fi."""
        self.wlan.active(True)
        logger.info("wi-fi enabled")

    def off(self) -> None:
        """Disable Wi-Fi."""
        self.wlan.active(False)
        logger.info("wi-fi disabled")

    def connect(self, ssid: str, key: str, retries: int = 5, sleep: int = 1000) -> None:
        """Connect to Wi-Fi network.

        Args:
            ssid: network name
            key: password
            retries: connection retries
            sleep: sleep interval between retries
        """
        self.on()
        if self.connected:
            logger.info(f"Already connected, board IP - {self.ip}")
            return
        logger.info("Connecting to Wi-Fi network...")
        networks = {str(e[0], "UTF-8") for e in self.wlan.scan()}
        if ssid not in networks:
            logger.error(f"Network {ssid} not found. Available networks - {sorted(networks)}")
            return
        while retries:
            try:
                self.wlan.connect(ssid, key)
            except Exception as e:
                logger.debug(e)
            if self.connected:
                break
            retries -= 1
            logger.debug(f"Connection error, retries left - {retries}")
            sleep_ms(sleep)
        else:
            logger.error("Connection error. No retries left.")
        if self.connected:
            logger.info(f"Connected, board IP - {self.ip}")

    @property
    def connected(self) -> bool:
        """Connection status.

        Returns:
            True if connected

        """
        return self.wlan.isconnected()

    @property
    def ip(self) -> str:
        """Board IP address.

        Returns:
            IP address if connected

        """
        return self.wlan.ifconfig()[0]


def reset() -> None:
    """Hard reset."""
    import machine

    machine.reset()
