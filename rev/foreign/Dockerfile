FROM rust:debian-slim

ARG name

RUN rustup target add

ADD src /$name/src
ADD Cargo.toml /$name/Cargo.toml
ADD .cargo /$name/.cargo

WORKDIR /$name
RUN cargo build --release
