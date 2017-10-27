CONFIG_DIR = $(HOME)/.config/sesamo
BIN_DIR = /usr/local/bin

config:
	mkdir -p $(CONFIG_DIR)
	mv -v config.ini.example $(CONFIG_DIR)/config.ini

install:
	sudo cp -pv sesamo.py $(BIN_DIR)/sesamo
	sudo chmod +x $(BIN_DIR)/sesamo
