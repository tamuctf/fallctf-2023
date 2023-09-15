FROM rust:slim-buster

ARG name
ARG port

RUN apt update; apt install -y gcc-arm-none-eabi
RUN rustup target add thumbv7m-none-eabi

ADD .cargo /$name/.cargo
ADD alien /$name/alien
ADD lm3s6965-uart /$name/lm3s6965-uart
ADD Cargo.toml /$name/Cargo.toml
ADD flag.txt /$name/flag.txt

WORKDIR /$name
RUN cargo build --release
