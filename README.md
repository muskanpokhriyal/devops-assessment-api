docker build -t tech-sonar-api -f Dockerfile .


docker run -d -p 5050:5050 tech-sonar-api

docker container list

docker stop [container_id]

