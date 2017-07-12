# PCLSearch
Philipppine Computing Literature Search Engine

This project utilizes docker and docker-compose. Five containers are used:

1. 1 container for MongoDB (Database)
2. 1 container for ExpressJS (REST API)
3. 1 container for AngularJS (Client)
4. 1 container for GROBID (Paper metadata extractor)
5. 1 container for Scrapy (Web Crawler and PDF file server)


Setup development environment:

`$./rebuild-all.sh`

`$./start-all.sh`

Cleanup:

`$./stop-all.sh`

`$./remove-all.sh`


To get a shell to one of the containers:

`$sudo docker exec -it <container> /bin/bash`

To exit from shell

`Ctrl+p, Ctrl+q`

The application is accessible at http://127.0.0.1:4200

Scraped PDFs are accessible at http://127.0.0.1:7070/pdfs
