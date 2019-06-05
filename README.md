e-Disi (server)
---------------

Server-side code for e-Disi platform. Handles user registration, verification and
location sharing requests. Will also act as mediator for socket communication.

## Install

First run `pipenv install` to install dependencies

Copy contents of `.env.example` to `.env` and replace placeholder values with real ones.

After that, you can run server with `python -m edisi`

## Http Requests

HTTP requests will be store in `/http` folder
Missing env variables must be defined in `/http/http-client.private.env.json` 