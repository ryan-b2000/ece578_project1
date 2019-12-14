#!/bin/bash

kill -9 $(pidof ssh)

kill -9 $(pidof sftp)

kill -9 $(pidof python3)
