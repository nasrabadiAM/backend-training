FROM postgres
ENV POSTGRES_PASSWORD docker
ENV POSTGRES_DB practice
ENV POSTGRES_USER ali
COPY *.sql /docker-entrypoint-initdb.d/
EXPOSE 5432
