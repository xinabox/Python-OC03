[![GitHub Issues](https://img.shields.io/github/issues/xinabox/Python-OC03.svg)](https://github.com/xinabox/Python-OC03/issues)
![GitHub Commit](https://img.shields.io/github/last-commit/xinabox/Python-OC03)
![Maintained](https://img.shields.io/maintenance/yes/2020)
![Build status badge](https://github.com/xinabox/Python-OC03/workflows/Python/badge.svg)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)

# Python-OC03

The OC03 xChip is a low-voltage control relay module able to switch AC and DC loads. It is based on the PCA9554A and TLP241A.

The optically isolated relay is controlled by a PCA9554A IO expander, which provides an control interface to the switch. The PCA9554A has several selectable I2C addresses accessible via solder pads.

The TLP241A photorelay consist of a photo MOSFET optically coupled to an infrared light emitting diode which switches a AC or DC load. It provides an isolation voltage of 5000 Vrms, making it suitable for applications that require reinforced circuit insulation.

# Usage

## Mu-editor
Download [Mu-editor](https://github.com/xinabox/mu-editor/releases/tag/v1.1.0a2)

### CW01 and CW02
- Use [XinaBoxUploader](https://github.com/xinabox/XinaBoxUploader/releases/latest) and flash MicroPython to the CW01/CW02.
- Download Python packages from the REPL with the following code:
    ```python
    import network
    import upip
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect("ssid", "password")
    upip.install("xinabox-OC03")
    ```

### CC03, CS11 and CW03
- Download the .UF2 file for CC03/CS11/CW03 [CircuitPython](https://circuitpython.org/board/xinabox_cs11/) and flash it to the board.
- TO DO

### MicroBit
- TO DO

## Raspberry Pi

Requires Python 3
```
pip3 install xinabox-OC03
```

# Example
```python
from xOC03 import xOC03
from xCore import xCore

OC03 = xOC03()

# start OC03
OC03.init()

# sleep time
DELAY = 500

# infinite loop
while True:

    # close relay
    OC03.writePin(True)
    xCore.sleep(DELAY)

    # open relay
    OC03.writePin(False)
    xCore.sleep(DELAY)
```