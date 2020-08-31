##
## 30/08/2020 Fontainebleau
## Makefile
## File creator:
## Adrien Colombier
##

SRC		=	src/main.py		\
			src/game.py		\
			src/graphic.py	\
			src/data.py
all:
			python ${SRC} map/canon.png

.PHONY: 	all