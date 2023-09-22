# deployment vars
NAME := foreign

all: $(NAME)

clean: .PHONY
	rm -f $(NAME) $(NAME).zip
	docker container rm -f $(NAME)$(SUFFIX)

build: Dockerfile src Cargo.toml
	docker $(DOCKER_GLOBAL) build -t $(NAME) \
		--build-arg name=$(NAME) \
		--build-arg port=$(PWN_CPORT) \
		.

extract:
	$(eval id := $(shell docker create $(NAME)))
	docker cp $(id):/$(NAME)/target/s390x-unknown-linux-gnu/release/$(NAME) - | tar xv $(NAME)
	docker rm -v $(id)

$(NAME): build extract

dist: extract

.PHONY:
