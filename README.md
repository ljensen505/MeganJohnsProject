# Megan Johns Portfolio Website

## Client

The React client is built using TypeScript and communicated with the Python server using http requests. Static files are generally served from Cloudinary. Though there is not currently any "auth" component to this application, it will be introduced in the future using Google Oauth2.

## Server

The backend of this application is build using Python, FastAPI, and MariaDB. ORM is handled manually (for now), and dependencies are manage with [Poetry](https://python-poetry.org/).

## Deployment

This application, including the database, is hosted on a Linode Ubuntu server with reverse proxying handled with NGINX. SSL is handled with certbot, and the Python server is run with systemd.
