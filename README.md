# rheinermark-viur

Created by Max.

https://rheinermark-viur.appspot.com

## Description

This is rheinermark-viur.

## Build the Vi

To build the Vi, run

```bash
$ cd vi
$ make deploy
```

## Change Git origin URL

Please set another Git repository origin. The default viur-base origin has been automatically deleted by ``clean-base.py``, for security reasons.

```bash
$ git remote add git@github.com:Max/rheinermark-viur.git
```

## Install prerequisites

To install prerequisites, once do

```bash
$ pip2 install -t deploy/lib -r requirements.txt --upgrade
```

or on any prerequisite change/update.

## Run local development version

To locally run, do

```bash
$ ./local_run.sh
```

or manually, do

```bash
$ cd deploy
$ dev_appserver.py -A rheinermark-viur --log_level=debug .
```

## Deploy to GAE

Deployment is performed using the gcloud SDK:

```bash
$ cd deploy

# Deploy to dev
$ gcloud app deploy --no-promote -q --project=rheinermark-viur --version=$USER-dev

# Deploy to live (beware!)
$ gcloud app deploy -q --project=rheinermark-viur --version=`date +"%Y-%m-%d"-$USER`
```

## Contact

Contact @Max for help and support.
