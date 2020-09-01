# clean up lost souls
docker rm $(docker ps -a -f status=exited -q)
docker rmi $(docker images -f "dangling=true" -q) --force
docker system prune -a

# create and run the docker
docker build --no-cache --tag lds . # build the docker image

docker run -t -d --name lds lds # run a container on detached mode

docker exec -it lds /bin/bash # open the docker to run the command