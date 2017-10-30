CONFIG_DIR = $(HOME)/.config/sesamo
BIN_DIR = /usr/local/bin
DATE_BKP = $$(date +%d%m%Y)

config:
	mkdir -p $(CONFIG_DIR)
	mv -v config.ini.example $(CONFIG_DIR)/config.ini

install:
	sudo cp -pv sesamo.py $(BIN_DIR)/sesamo
	sudo chmod +x $(BIN_DIR)/sesamo

update:
	mkdir -p $(CONFIG_DIR)/backup_sesamo
	sudo cp $(BIN_DIR)/sesamo $(CONFIG_DIR)/backup_sesamo/sesamo_bkp_$(DATE_BKP)
	sudo cp -pv sesamo.py $(BIN_DIR)/sesamo
	sudo chmod +x $(BIN_DIR)/sesamo
