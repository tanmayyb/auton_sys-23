# Resetting Jetson Nano

Flashing a new OS onto the EMMC of a Jetson Nano

# NVIDIA SDK Manager

Link: [Download Page](https://developer.nvidia.com/sdk-manager)

> - Requires Ubuntu 18.06
> - After entering forced recovery, connect to the Nano and choose manual flash mode 

# Forced Recovery Mode
![B10 Nano Board](https://docs.nvidia.com/jetson/archives/l4t-archived/l4t-325/Tegra%20Linux%20Driver%20Package%20Development%20Guide/images/hw_setup.1.4.jpg)
> - Connect ground and reset pins on J50 before powering board on
> - Check status with lsusb in terminal: should end in 7f21

Link: [Instructions](https://wiki.seeedstudio.com/reComputer_J1020_A206_Flash_JetPack/#hardware-preparation-force-recovery-mode) -> but with pins listed above
