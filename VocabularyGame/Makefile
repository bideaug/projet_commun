.PHONY: proto run test
PROTOPATH = ./protobuf

.DEFAULT_GOAL = help

COM_COLOR = \033[0;34m
OBJ_COLOR = \033[0;36m
OK_COLOR = \033[0;32m
ERROR_COLOR = \033[0;31m
WARM_COLOR = \033[0;33m
NO_COLOR = \033[m

CC = python
CCProto = protoc


proto: $(PROTOPATH)/word.proto ## Compile the .proto file
	$(CCProto) -I=$(PROTOPATH) --python_out=$(PROTOPATH) $(PROTOPATH)/word.proto

graphical:
	$(CC) main.py -g

run: main.py ## Run the program
	$(CC) main.py

test: test.py ## Run the test
	$(CC) test.py

all: main.py test.py ## Compile the protobuf file and then run the test and the program
	$(MAKE) proto
	$(MAKE) test
	$(MAKE) run

help: ## Display a list of available command
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-10s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'

clean: ## Clean all unnecessary files
	rm -v $(PROTOPATH)/*_pb2.py
	
	
