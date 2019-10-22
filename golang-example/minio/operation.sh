#!/bin/bash

docker run -p 9000:9000 minio:2019-10-22 server /mnt

docker export/save IMAGE_ID > xx.tar
docker import xx.tar
