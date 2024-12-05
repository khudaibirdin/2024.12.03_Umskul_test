run:
	docker run -it -d --env-file .env --restart=unless-stopped --name test_bot_container test_bot
stop:
	docker stop test_bot_container
attach:
	docker attach test_bot_container
dell:
	docker rm test_bot_container