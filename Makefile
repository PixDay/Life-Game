##
## 30/08/2020 Fontainebleau
## Makefile
## File creator:
## Adrien Colombier
##

SRC		=	src/main.py	\
			src/game.py
all:
			python ${SRC} map/canon.png

.PHONY: 	all