
all: install

install:
	helm install -n hello-alpha ../hello

delete:
	helm delete --purge hello-alpha

test:
	curl --noproxy '*' http://80.8.8.99:30010/info

