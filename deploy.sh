#!/usr/bin/env bash
set -e

SCRIPT_NAME=$1

pushd ${SCRIPT_NAME}
cp -rp ../common .
gcloud functions deploy ${SCRIPT_NAME} --runtime=python37 --trigger-http --region=asia-northeast1
rm -rv ./common
popd
