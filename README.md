# Termux-Packages
##### _for i-Haklab_

This project is with the purpose of offering easy and fast access to the installation of tools and/or frameworks provided by the cyber security and pentesting laboratory [i-Haklab](https://github.com/ivam3/i-Haklab), for the Android operating system under the [Termux](https://github.com/termux/termux-app) application.

## Available tools and/or frameworks

| Tool | Description |
| ------ | ------ |
| [i-Haklab](https://github.com/ivam3/i-Haklab) | Ciber-security and pentesting laboratory for Termux |
| [acccheck](https://github.com/qashqao/acccheck) | Windows SMB Password Dictionary Attack Tool |
| [adbfastboot](https://developer.android.com/studio/command-line/adb) | Versatile command-line tool that facilitates a variety of device actions |
| [adminpanel](https://github.com/Techzindia/admin_penal) | Find website's admin panel |
| [amass](https://github.com/OWASP/Amass) | In-depth Attack Surface Mapping and Asset Discovery |
| [androbugs](https://github.com/AndroBugs/AndroBugs_Framework) | Android vulnerability scanner |
| [aquatone](https://github.com/michenriksen/aquatone) | A Tool for Domain Flyovers |
| [beef](https://www.beefproject.com) | powerful and intuitive security tool focuses on leveraging browser vulnerabilities to assess the security posture of a target |
| [binwalk](https://github.com/ReFirmLabs/binwalk) | Tool for analyzing, reverse engineering, and extracting firmware images | 
| [blackbox](https://github.com/jothatron/blackbox) | A penetration testing framework|
| [botgram](https://github.com/ivam3/botgram) | Fetch all information about Telegram group members |
| [burpsuite](https://portswigger.net/burp) | Graphical tool for performing security testing of web applications |
| [cewl](https://github.com/digininja/CeWL) | Custom word lists spidering a targets website |
| [cloudbunny](https://github.com/Warflop/CloudBunny) | Capture the real IP of the server that uses a WAF as a proxy or protection |
| [code-server](https://github.com/Leask/code-server-nodejs) | VS Code with Nodejs development environment running on a remote server |
| [converter](https://github.com/miluxmil/milux/blob/master/converter) | Easy multimedia file converter |
| [credmap](https://github.com/lightos/credmap) | Test the user credentials provided on several popular websites to see if the password has been reused on any of them |
| [d-tect](https://github.com/shawarkhanethicalhacker/D-TECT-1) | Pentest the Modern Web |
| [dos-a-tool](https://github.com/ivam3/DoS-A-Tool) | Performs denial of service attacks under the SYN Flood method |
| [dex2jar](https://github.com/pxb1988/dex2jar) | Toolkit to work with android .dex and java .class files |
| [dnsenum](https://github.com/fwaeytens/dnsenum) | Enumerate DNS information |
| [embed](https://github.com/ivam3/embed) | Embed metasploit payload into a legtim APK |
| [evilurl](https://github.com/UndeadSec/EvilURL) | Generate unicode domains for IDN Homograph Attack and detect them. |
| [exif](https://github.com/ivam3/ExiF) | Extract information (meta data) from files. |
| [exploitdb](https://github.com/offensive-security/exploitdb) | The official [Exploit Database](https://www.exploit-db.com) repository |
| [fbi](https://github.com/xHak9x/fbi) | Facebook account information gathering |
| [fuzzdb](https://github.com/fuzzdb-project/fuzzdb) | Dictionary of attack patterns and primitives for black-box application fault injection and resource discovery |
| [getnpusers](https://github.com/SecureAuthCorp/impacket/blob/master/examples/GetNPUsers.py) | List and get TGT for those users who have ownership |
| [ghost]() | |
| [gobuster]() | |
| [gophish]() | |
| [hakku]() | |
| [hasher]() | |
| [hatcloud]() | |
| [hunner]() | |
| [hydra]() | |
| [infoga]() | |
| [ipgeolocations]() | |
| [johntheripper]() | |
| [kerbrute]() | |
| [kalilinux]() | |
| [lockphish]() | |
| [metasploit-framework]() | |
| [nexphisher]() | |
| [ngrok](https://ngrok.com) | |
| [osintgram]() | |
| [phomber]() | |
| [phonesploit]() | |
| [pybelt]() | |
| [quack]() | |
| [recon-ng]() | |
| [recondog]() | |
| [rhawk]() | |
| [routersploit]() | |
| [saycheese]() | |
| [sayhello]() | |
| [seeker]() | |
| [shc]() | |
| [shellsploit]() | |
| [sherlock]() | |
| [slowhttptest]() | |
| [sqliv]() | |
| [stegsnow]() | |
| [sublist3r]() | |
| [tangalanga]() | |
| [termux-desktop-xfce]() | |
| [torvpn]() | |
| [trape]() | |
| [userrecon]() | |
| [virustotal]() | |
| [vulnx]() | |
| [wbruter]() | |
| [webhackshl]() | |
| [websploit]() | |
| [wfuzz]() | |
| [whatweb]() | |
| [wpscan]() | |
| [xerosploit]() | |
##### Suggest a tool and/or framework to be add in our [Telegram Support Group](https://t.me/iHaklab)

## How to get ...

To add the list of available tools and/or frameworks to the package manager `apt` in [Termux](https://github.com/termux/termux-app) follow those 5 simple steps:

- Install `wget` package:
```bash
apt install wget
```

- Create a directory:
```bash
mkdir -p $PREFIX/etc/apt/sources.list.d
```

- Download sources file:
```bash
wget https://raw.githubusercontent.com/ivam3/termux-packages/gh-pages/ivam3-termux-packages.list -O $PREFIX/etc/apt/sources.list.d/ivam3-termux-packages.list
```

- Update Termux:
```bash
apt update && apt upgrade
```

### License

GNU

##### Follow me on [Socials Network](https://wlo.link/@Ivam3)

