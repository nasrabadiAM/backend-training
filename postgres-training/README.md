
Run a postgress instance with docker
---


First
-----
create a named volume in your docker 

```bash 
docker volume ls

docker volume create postgres-data

```

Second
-----
pull your docker image 

```bash 
docker pull postgres
```

Third
-----
Run your postgres with this command

```bash
 docker run -itd -e POSTGRES_USER=ali -e POSTGRES_PASSWORD=password -e POSTGRES_DB=hello -p 5432:5432 -v postgres-data:/var/lib/postgresql/data --name postgresql-practice postgres                
```

Forth 
-----
Connect to docker container and query to database with  psql 

docker exec -it container_name psql -U user_name -d database_name


```bash 
docker exec -it postgresql-practice psql -U ali -d hello
```


After run 
-----
after running your instance, you can stop or re-run the image
```bash 
docker run instance-id

docker stop instance-id
```

you can get the instance-id with run this command

```bash 

docker ps (--all)
```






