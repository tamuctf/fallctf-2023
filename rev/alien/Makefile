# deployment vars
NAME := alien

all: $(NAME)

clean: .PHONY
	rm -f $(NAME) $(NAME).zip
	docker container rm -f $(NAME)$(SUFFIX)

build: Dockerfile Cargo.toml alien/ .cargo lm3s6965-uart flag.txt
	docker $(DOCKER_GLOBAL) build -t $(NAME) \
		--build-arg name=$(NAME) \
		--build-arg port=$(PWN_CPORT) \
		.

extract: build
	$(eval id := $(shell docker create $(NAME)))
	docker cp $(id):/$(NAME)/$(NAME).elf - | tar xv $(NAME)
	docker rm -v $(id)

$(NAME).elf: extract

dist: extract

.PHONY: