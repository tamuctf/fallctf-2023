FROM debian:buster-slim as build

ARG name

RUN apt-get update -y; apt-get install build-essential libssl-dev curl -y
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

ADD src /$name/src
ADD Cargo.toml /$name/Cargo.toml

WORKDIR /$name
RUN /root/.cargo/bin/cargo build --release
