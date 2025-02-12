# Install

## System requiments

### Supported Operating Systems

- Red Hat Linux 8.X
- Oracle Linux 8.X

### Supported Web Browsers

- Mozilla Firefox
- Google Chrome
- Microsoft Edge

### Network Communication

| From | To | Port | Protocol | Description | Bidirectional Communication |
|------|:---|:----:|:--------:|:------------|:---------------------------:|
| Energy Monitor | Nrpe Agent | 5666 | TCP | Agent communication | &#x2B1C; |
| Energy Monitor | Network Host | 161 | UDP | SNMP request comunication | &#x2B1C; |
| Network Host | Energy Monitor | 162 | UDP | SNMP trap comunication | &#x2B1C; |
| User browser | Energy Monitor | 443 | TCP | GUI | &#x2B1C; |
| Other node | Energy Monitor | 15551 | TCP | Cluster communiaction | &#x2705; |
| Other node | Energy Monitor | 22 | TCP | SSH cluster comunication | &#x2705; |

### Repository

Installation need access to below repo.

| Red Hat 8 | Oracle Linux 8 | Added During Installation |
|:---------:|:--------------:|:-------------------------:|
| Red Hat Enterprise Linux 8 for x86_64 - AppStream | Oracle Linux 8 Application Stream (x86_64) | &#x2B1C; |
| Red Hat Enterprise Linux 8 for x86_64 - BaseOS | Oracle Linux 8 BaseOS Latest (x86_64) | &#x2B1C; |
| Red Hat CodeReady Linux Builder for RHEL 8 x86_64 | Oracle Linux 8 CodeReady Builder (x86_64) | &#x2705; |
| Extra Packages for Enterprise Linux 8 | Extra Packages for Enterprise Linux 8  | &#x2705; |
| Docker CE Stable | Docker CE Stable | &#x2705; |

## Installation

The Energy Monitor installer is delivered as tarball `energy-monitor-{product_version}.tar.gz`

### Installation Process

The Energy Monitor comes with simple installation script called `install.sh`. It is designed to facilitate the installation and deployment process of out product. After running(execute) the script, it will detect supported distribution. The script is located in the `energy-monitor` directory.

#### Installation steps

1. Untar the archive containing installer \
    `tar xf energy-monitor-{product_verison}.tar.gz`
1. Copy license files(both of them) to extracted directory \
    `cp monitor_*.* energy-monitor/`
1. Go to the extracted directory \
    `cd energy-monitor`
1. Run installation script with installation flag \
    `./install.sh -i` or `./install.sh install`

During this process you will be asked to confirm that you want to install Energy Monitor on your system.

If everything went correctly, you should be able to login to GUI with default credentials provided at the end of installation process.

GUI will be avaiable at `https://IP_address`

![login_page](/media/00_01_login_page.png)
