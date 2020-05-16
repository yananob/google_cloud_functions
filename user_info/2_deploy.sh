#!/usr/bin/env bash
set -e

gcloud functions deploy merch_info --runtime=python37 --trigger-http --region=asia-northeast1
