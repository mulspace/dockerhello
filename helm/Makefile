
all: install

install: alpha belta

alpha belta:
	helm install -n hello-$@ -f $@_values.yaml ../helm

delete:
	helm delete --purge hello-alpha
	helm delete --purge hello-belta

test:
	@echo "==> Test alpha service"
	curl --noproxy '*' http://127.0.0.1:30010/info
	@echo "==> Test belta service"
	curl --noproxy '*' http://127.0.0.1:30011/info

