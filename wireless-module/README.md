# UltraEdge Wireless module shells

Printable shells for the UltraEdge Wireless module: an ESP32-C3 board that sits in your radio's external module bay
and links the [UltraEdge app](https://github.com/50UR4V/UltraEdge-app) to the radio over Bluetooth LE.

- **2-in-1:** one shell for both a standard JR bay (TX16S, QX7 and similar) and a nano bay (Pocket and similar).
- **Pocket:** a smaller shell made for the RadioMaster Pocket.

**Status:** prototype. UltraEdge Wireless isn't released yet; the module's firmware and how to get it will be
announced on [ultraedge.app](https://ultraedge.app).

## Files

| Shell | Part | 3MF | STL | Size (mm) |
|---|---|---|---|---|
| 2-in-1 | Body | `3mf/UltraEdge-Wireless-2in1-Body.3mf` | `stl/UltraEdge-Wireless-2in1-Body.stl` | 55.2 × 23.9 × 59.5 |
| 2-in-1 | Cover | `3mf/UltraEdge-Wireless-2in1-Cover.3mf` | `stl/UltraEdge-Wireless-2in1-Cover.stl` | 47.7 × 4.0 × 63.0 |
| Pocket | Body | `3mf/UltraEdge-Wireless-Pocket-Body.3mf` | `stl/UltraEdge-Wireless-Pocket-Body.stl` | 30.2 × 19.4 × 59.5 |
| Pocket | Cover | `3mf/UltraEdge-Wireless-Pocket-Cover.3mf` | `stl/UltraEdge-Wireless-Pocket-Cover.stl` | 30.2 × 15.4 × 59.8 |

STL files are made from the 3MF files with `../tools/3mf2stl.py`. Print settings as for the mounts (PLA+, 0.2 mm
layers, 4 walls).

## What goes inside (prototype)

- An ESP32-C3 board
- A 5 V regulator (7805, TO-220) on a small piece of perfboard, fed from the bay
- Header pins to the bay's contacts

Don't plug the C3's USB into a computer while the module is in a powered bay.

## Licence

This folder (the shells' design files) is under [CC BY-SA 4.0](LICENSE): you may print, change, share and sell the
shells or prints of them, with credit to UltraEdge, and changed versions must use the same licence. The module's
firmware is not part of this repository and is not covered by this licence.

UltraEdge is not affiliated with or endorsed by EdgeTX, FrSky or RadioMaster.
