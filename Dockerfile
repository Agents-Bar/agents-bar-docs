# Need to change this. The base image is 3.24 GB
FROM alpine:latest as build-stage

RUN mkdir -p /etc/sphinx/build
RUN apk add --no-cache python3 py3-pip make git

RUN python3 -m pip install sphinx && \
    python3 -m pip install sphinx-theme
RUN python3 -m pip install --no deps ai-traineree-client tenacity

COPY ./ /etc/sphinx/
WORKDIR /etc/sphinx
RUN make html


# Serving files as static website
FROM nginx:1.15

COPY --from=build-stage /etc/sphinx/_build/html /usr/share/nginx/html
