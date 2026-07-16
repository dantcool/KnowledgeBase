source : https://computingforgeeks.com/install-kvm-arch-linux/
## Prerequisites

- Running Arch Linux System with virtualization enabled 
- CPU with hardware virtualization support (Intel VT-x or AMD-V) 
- sudo or root access
- at least 4GB of ram

## Check Hardware Virtualization Support 

to confirm that CPU supports hardware virtualization run 
`vmx` (Intel) or `svm` (AMD)
full command `grep -c 'vmx|svm' /proc/cpuinfo`

Any number greater than 0 means CPU supports hardware virtualization.
if output is 0 you need to enable VT-x(intel) or AMD-v in your BIOS/UEFI firmware settings.

Next verify that the KVM kernel modules are loaded:
`lsmod | grep kvm`

you should see kvm_intel or kvm_amd along with the base kvm module:
EXAMPLE
`kvm_intel        503808  0
`kvm             1421312  1 kvm_intel
`irqbypass        12288   1 kvm`

if modules aren't loaded, load them manually with command 
`sudo modprobe kvm_intel \\or if amd\\ kvm_amd`


## Install KVM,QEMU, and Virt-manager on Arch Linux
`sudo pacman -S qemu-full virt-manager virt-viewer libvirt dnsmasq edk2-ovmf swtpm iptables-nft`


| PACKAGE      | Purpose                                                                                   |
| ------------ | ----------------------------------------------------------------------------------------- |
| qemu-full    | Complete QEMU installation with all architecture support and features (x86, ARM, etc.)    |
| virt-manager | GTK-based graphical interface for creating and managing virtual machines                  |
| virt-viewer  | Console viewer for connecting to VM displays (SPICE/VNC)\|                                |
| libvirt      | Virtualization management daemon and API – the glue that ties KVM and QEMU together       |
| dnsmasq      | Lightweight DHCP and DNS server for NAT-based VM networking                               |
| edk2-ovmf    | UEFI firmware for virtual machines – required for UEFI-boot VMs and Secure Boot           |
| swtpm        | Software TPM 2.0 emulator – needed for Windows 11 VMs and TPM-dependent operating systems |
| iptables-nft | Firewall backend that libvirt uses to set up NAT networking rules                         |

## Enable and Start the libvirt Daemon
after everything is installed enable and start the `libvirtd` service which is the daemon that manages VM's , Networks, and storage pools

`sudo systemctl enable --now libvirtd`

verify service is running 

`sudo systemctl status libvirtd`

output should show `active (running)`

EXAMPLE 
`● libvirtd.service - Virtualization daemon
  ``   Loaded: loaded (/usr/lib/systemd/system/libvirtd.service; enabled; preset: disabled)
     `Active: active (running) since Mon 2026-03-24 10:15:32 UTC; 5s ago
   `Main PID: 1234 (libvirtd)
      `Tasks: 19 (limit: 32768)
     `Memory: 14.2M
     `CGroup: /system.slice/libvirtd.service
             `└─1234 /usr/bin/libvirtd`

## Add your user to the libvirt Group 

managing VM's thhorut libvirt requires root previleges. To use virt-manager and virsh as a regular user, add your account to the libvirt group 
`sudo usermod -aG libvirt $(whoami)`

After you must log out and log back in for the group change to take effect then verify membership after logging back in with:

`groups`

output should include libvirt in the list
if not you may need to reboot system then try group command again 

## Configure the Default NAT Network 
libvirts comews with a default NAT network that gives VM's internet acces through the host.
this network needs to be started and set to auto-star on boot:

`sudo virsh net-start default`
`sudo virsh net-autostart default`

confirm network is active 

`sudo virsh net-list --all`

should see

 `Name      State    Autostart   Persistent
`--------------------------------------------
 `default   active   yes         yes

default network creates a virtual bridge interface called `virbr0` with the subnet 192.168.122.0/24. VM's connected to this network get IP addresses via DHCP from dnsmasq and can reach the internet through NAT on the host. If the network fails to start it is usually because dnsmasq is not installed or iptables-nft is missing -both are required for libvirt's NAT networking to work. 

## Launch Virt-Manager
open virt-manager from application menu or with command 
`virt-manager`

on first launch virt-manager will attempt to connect to the local QEMU/KVM hypervisor. 
You should see it connecting 
Once connected you will see QEMU/KVM listed as your hypervisor connection, ready to create and manage virtual machines. 
if virt-manager shows "Not Connected" or fails to connect, make sure libvirtd is running and your user is in the libvirt group. 

## Creating your First Virtual Machine 
1. 1. Click **File > New Virtual Machine** (or the “Create a new virtual machine” button in the toolbar)
2. Choose your installation source – **Local install media (ISO)** is the most common option. Browse to your ISO file
3. Set memory and CPU allocation. A good starting point for most Linux VMs is 2048 MB RAM and 2 vCPUs
4. Create a virtual disk. 20-40 GB is typical for Linux, 50+ GB for Windows. The default qcow2 format supports thin provisioning so it won’t use the full size immediately
5. On the final screen, review your settings. Check **“Customize configuration before install”** if you need to change the firmware from BIOS to UEFI, switch network settings, or add hardware like a TPM device

For UEFI-based VMs, select the OVMF firmware in the customization screen under Overview > Firmware. This is required for modern operating systems that expect UEFI boot, including Windows 11. For Windows 11 specifically, you also need to add a TPM device (emulated by swtpm) from the “Add Hardware” dialog.

