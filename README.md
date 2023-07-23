# python-web-fastapi-api-sqlserver-ssl-pop

## Description
Simple web app that serves api
for a fastapi project.

Uses sqlalchemy query a table `pop`.

Sql server uses self-signed ssl.

## Tech stack
- python
  - fastapi
  - uvicorn
  - sqlalchemy
- bootstrap
- jquery
- dataTable
- mssql

## Docker stack
- alpine:edge
- python:latest
- mcr.microsoft.com/mssql/server:2017-CU17-ubuntu

## To run
`sudo ./install.sh -u`
- [Availble at](http://localhost/dog)

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`
