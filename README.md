![Sesamo](img/sesamo.png)

**Sésamo**
===================
Sésamo is a simple python script to concentrate a many servers to access.

Why? I'm study Python and I'm a Lazy SysAdmin.

### ToDo's

* Writing tests.
* Improve the code
* Adding a PyPi libary

### Libs

* os
* sys
* time
* configparser
* getpass
* subprocess

### How to use

Clone the repo and access Sesamo folder:
```bash
git clone https://github.com/perylemke/sesamo.git
cd sesamo
```

Execute make to configure and install:
```bash
make config
make install
```

Configure config.ini:
```bash
vim $HOME/.config/sesamo/config.ini
```

Example to configurate:
```
[SERVER]
ssh=user@host
```

To execute is a just simple command:
```bash
sesamo
```

Feedbacks are welcome and if you have a improvement fork us and pull us! :)

### That's it folks!
