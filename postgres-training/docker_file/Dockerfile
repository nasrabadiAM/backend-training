FROM postgres
ENV POSTGRES_PASSWORD docker
ENV POSTGRES_DB world
ENV POSTGRES_USER ali
COPY *.sql /docker-entrypoint-initdb.d/
EXPOSE 5432
