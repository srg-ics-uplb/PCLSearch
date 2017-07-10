# PCLSearch
Philipppine Computing Literature Search Engine

This project utilizes docker and docker-compose. Five containers are used:

1. 1 container for MongoDB (Database)
2. 1 container for ExpressJS (REST API)
3. 1 container for AngularJS (Client)
4. 1 container for GROBID (Paper metadata extractor)
5. 1 container for Scrapy (Web Crawler)


Setup development environment:

`$./rebuild-all.sh`

`$./start-all.sh`

Cleanup:

`$./stop-all.sh`

`$./remove-all.sh`


To get a shell

`$sudo docker exec -it <container> /bin/bash`
