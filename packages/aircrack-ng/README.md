# aircrack-ng

> Wi-Fi security auditing suite for monitoring, capturing and testing wireless networks.

## Overview

Aircrack-ng is a complete suite of tools for assessing Wi-Fi network security.
It includes tools for packet capture, injection, cracking WEP/WPA keys, and
monitoring wireless interfaces.

The Termux package provides the standard Aircrack-ng command-line tools for
supported architectures. Wireless testing requires a compatible adapter and,
on Android, the appropriate permissions and driver support.

## Upstream source

- **Source:** [aircrack-ng/aircrack-ng](https://github.com/aircrack-ng/aircrack-ng)
- **Website:** [aircrack-ng.org](https://www.aircrack-ng.org/)

## Installation

```bash
pkg update
pkg install aircrack-ng
```

The package is built for `aarch64`, `arm`, `i686` and `x86_64`.

## Requirements

- A wireless adapter supported by the Android kernel and Termux
- Monitor mode and packet injection support for the adapter
- Root access on devices where the kernel restricts wireless operations

## Usage

The suite installs several commands. Common tools include:

```bash
aircrack-ng --help
airmon-ng --help
airodump-ng --help
aireplay-ng --help
airbase-ng --help
```

Typical workflow:

```bash
airmon-ng start wlan0
airodump-ng wlan0mon
aireplay-ng --deauth 10 -a <BSSID> wlan0mon
aircrack-ng -w wordlist.txt capture.cap
```

Use only on networks you own or have explicit permission to test.

## Package details

| Field | Value |
|---|---|
| Package | `aircrack-ng` |
| Version | `3:1.7` |
| Architecture | `aarch64`, `arm`, `i686`, `x86_64` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [aircrack-ng/aircrack-ng](https://github.com/aircrack-ng/aircrack-ng) |
| Website | [aircrack-ng.org](https://www.aircrack-ng.org/) |
| Dependencies | Wireless tools and libraries provided by Termux |

## Notes

- Monitor mode and packet injection depend on the device kernel, firmware and
  adapter. Not every Android device supports them.
- Some operations require root or a supported external wireless adapter.
- Use the suite only for authorized security testing and network auditing.

## Troubleshooting

```bash
pkg update
pkg install aircrack-ng
command -v aircrack-ng
aircrack-ng --help
```

If the wireless interface is not detected, verify that the adapter is visible
to Android and that the kernel exposes the required wireless interfaces.

## License

Aircrack-ng is distributed under the GNU General Public License. See the
upstream repository for the complete license and third-party notices.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab)
ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
