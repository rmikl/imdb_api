## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

#### General info
This is simple dockerized tool for checking move rating from IMDB.

## Technologies
Project is created with:
Python 3.10.0 (container: python:latest, f48ea80eae5a) 
Docker 20.10.10, build b485636

##Setup:
1. First You need to export your API key as environment variable:

    `export TOKEN="<YOUR API KEY>"`

    example:     `export TOKEN="123456"`

2. Then build docker image:

    `docker build -t rmikl/omdb_api --build-arg TOKEN .` 

3. Check your movie rating!

    `docker run rmikl/omdb_api <NAME OF THE MOVIE>`
    example: `docker run rmikl/omdb_api the office`

