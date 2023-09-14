FROM rust:alpine

ARG name

RUN apk update
RUN apk add --no-cache musl-dev

ADD src /$name/src
ADD Cargo.toml /$name/Cargo.toml

WORKDIR /$name
RUN cargo build --release
