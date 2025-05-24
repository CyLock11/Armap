# 🗺️ ArMap - Network Discovery Tool

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macOS%20%7C%20windows-lightgrey.svg)](https://github.com/CyLock11/ArMap)

> 🔍 A powerful and elegant network discovery tool that uses ARP protocol to identify active hosts on your network.

## ✨ Features

- 🚀 **Fast Network Scanning**: Efficiently discovers active hosts using ARP protocol
- 🎨 **Colorized Output**: Beautiful colored terminal output for better readability
- 🏷️ **Vendor Detection**: Automatically identifies device manufacturers from MAC addresses
- 📊 **Network Statistics**: Provides detailed network information and scan timing
- 🛡️ **Error Handling**: Robust error handling with informative messages
- 💻 **Cross-Platform**: Works on Linux, macOS, and Windows

## 📋 Requirements

- 🐍 Python 3.6 or higher
- 🔧 Administrator/root privileges (required for network scanning)
- 🌐 Network interface access

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/CyLock11/Armap.git
   cd ArMap
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Make it executable** (Linux/macOS):
   ```bash
   chmod +x armap.py
   ```

## 🎯 Usage

### Basic Usage
```bash
python armap.py -i <interface_name>
```

### Examples

**Linux/macOS**:
```bash
sudo python armap.py -i eth0
sudo python armap.py -i wlan0
```

**Windows**:
```bash
python armap.py -i "Wi-Fi"
python armap.py -i "Ethernet"
```

### 📱 Sample Output
```
Interface: eth0, MAC: 00:11:22:33:44:55, IPv4: 192.168.1.100
Starting armap 1.0 with 254 hosts (https://github.com/CyLock11/ArMap)

192.168.1.1     aa:bb:cc:dd:ee:ff       Cisco Systems
192.168.1.10    11:22:33:44:55:66       Apple Inc.
192.168.1.25    77:88:99:aa:bb:cc       Samsung Electronics
192.168.1.50    dd:ee:ff:00:11:22       Intel Corporate

Ending armap 1.0: 254 hosts scanned in 2.34 seconds
```

## 🔧 Command Line Options

| Option | Description | Required |
|--------|-------------|----------|
| `-i`, `--interface` | Network interface to scan | ✅ Yes |
| `-h`, `--help` | Show help message | ❌ No |

## 🛠️ How It Works

1. **Interface Validation**: Verifies the specified network interface exists
2. **Network Discovery**: Gathers network information (IP, MAC, subnet)
3. **ARP Scanning**: Sends ARP requests to all hosts in the network range
4. **Vendor Lookup**: Identifies device manufacturers using MAC address OUI
5. **Results Display**: Shows discovered hosts with colored, formatted output

## 🐛 Troubleshooting

### Common Issues

**Permission Denied**:
```bash
# Run with elevated privileges
sudo python armap.py -i eth0  # Linux/macOS
```

**Interface Not Found**:
```bash
# List available interfaces first
ip link show  # Linux
ifconfig      # macOS
ipconfig      # Windows
```

**No Hosts Found**:
- Ensure you're connected to the network
- Check if the interface has an IP address
- Verify network connectivity

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. 🍴 Fork the repository
2. 🌟 Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔀 Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**CyLock11**
- 🐙 GitHub: [@CyLock11](https://github.com/CyLock11)
- 🌐 Project Link: [https://github.com/CyLock11/ArMap](https://github.com/CyLock11/ArMap)

## ⚠️ Disclaimer

This tool is intended for educational and authorized network testing purposes only. Always ensure you have proper authorization before scanning networks that don't belong to you.

## 🙏 Acknowledgments

- 📦 [Scapy](https://scapy.net/) - Powerful packet manipulation library
- 🏷️ [mac-vendor-lookup](https://pypi.org/project/mac-vendor-lookup/) - MAC address vendor identification
- 🎨 [termcolor](https://pypi.org/project/termcolor/) - Terminal color formatting

---

<div align="center">
  <strong>⭐ If you found this project helpful, please give it a star! ⭐</strong>
</div>
