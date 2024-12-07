build:
	sudo docker build -t test_bot .
run:
	sudo docker run -it -d --env-file .env --restart=unless-stopped --name test_bot_container test_bot
stop:
	sudo docker stop test_bot_container
attach:
	sudo docker attach test_bot_container
dell:
	sudo docker rm test_bot_container