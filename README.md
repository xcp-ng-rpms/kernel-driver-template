# hello-world

## To build the driver yourself, go on your docker host and use follwing shell commands to build it.

mkdir driver-hello-world

cd driver-hello-world

git clone https://github.com/xcp-ng/xcp-ng-build-env

git clone https://github.com/xcp-ng-rpms/kernel-driver-template

chown 1000 ./kernel-driver-template/ -R

./xcp-ng-build-env/run.py -b 7.6 --build-local kernel-driver-template/ --rm
