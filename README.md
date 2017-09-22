![Sesamo](img/sesamo.png)

**Sésamo**
===================
Sésamo is a simple python script to access a Ahgora servers.

Why? I'm study Python and I need a challenge to do.

### ToDo's

- Writing tests.
- Improve the code
- Adding more servers
- Adding a PiPy libary

### How to use

Clone the Bitbucket repo:
```bash
git clone git@bitbucket.org:perylemke/sesamo.git
```

Transform a executable (with a Sudo permission):
```bash
cd sesamo
cp -pv sesamo.py /usr/local/bin/sesamo
cd /usr/local/bin/
chmod +x sesamo
```

Configure access.ini.example and change the name:
```bash
sudo mv -v sesamo.ini.example /etc/sesamo.ini
```

To execute is a just simple command:
```bash
sesamo
```

### That's it folks!
