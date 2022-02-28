setup_redis:
	docker run -p 127.0.0.1:6379:6379/tcp --name test-redis -d --rm  redis

cleanup:
	docker kill test-redis