
Reference to docker file commands
---
https://docs.docker.com/engine/reference/builder/



According to this Docker file in this repo, you can build and run an postgres image with a db_name tnd user_name that defined, in dockerFile.

To Build and run the docker file
---
First you need to build the Dockerfile with this command

```bash
docker build -t postgres-dockerfile .
```

Then run the image that you have built in the last section with this command

```bash
docker image ls //to get list of images you have built
//run the image
docker run -dp 5432:5432 image_id_or_name 
```
Then you can run this command to see running containers 
```bash 
docker ps
```

If you want to stop your container 
---
```bash
docker stop your_container_name
```

If you want to start your container again 
```bash 

docker start your_container_name
```

If you wnat to connect to your running container and do things inside of it. 
```bash 

docker exec -it zen_johnson psql -U ali -d world
```
-it means intractive 
zen_johnson is my container name 
psql is the command i want to run and any thing after that is psql params (my command)

