FROM rust:debian-slim

ARG name

RUN apt update; apt install crossbuild-essential-s390x-linux-gnu -y
RUN rustup target add s390x-unknown-linux-gnu

ADD src /$name/src
ADD Cargo.toml /$name/Cargo.toml
ADD .cargo /$name/.cargo

WORKDIR /$name
RUN cargo build --release
