#!/bin/sh
pip install uvicorn fastapi && uvicorn app.main:app --host 0.0.0.0 --port 8085