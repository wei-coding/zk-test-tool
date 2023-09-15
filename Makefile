all:
	git pull

install:
	sudo docker build . -t zktest:latest