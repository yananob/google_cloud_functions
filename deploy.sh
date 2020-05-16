#!/usr/bin/env bash
set -e

SCRIPT_NAME=$1

gcloud functions deploy ${SCRIPT_NAME} --runtime=python37 --trigger-http --region=asia-northeast1
