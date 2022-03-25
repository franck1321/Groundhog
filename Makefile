##
## EPITECH PROJECT, 2021
## B-CNA-410-MAR-4-1-groundhog-iliam.amara
## File description:
## Makefile
##

all:
	cp Groundhog.py Groundhog
	chmod +x Groundhog

clean:
	rm Groundhog

fclean: clean

re: fclean all