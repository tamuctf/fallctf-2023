FROM rust:slim-buster

ARG name

RUN apt update; apt install crossbuild-essential-s390x -y
RUN rustup target add s390x-unknown-linux-gnu

ADD src /$name/src
ADD Cargo.toml /$name/Cargo.toml
ADD .cargo /$name/.cargo

WORKDIR /$name
RUN cargo build --release --target s390x-unknown-linux-gnu
