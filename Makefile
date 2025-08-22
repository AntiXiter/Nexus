.PHONY: run fmt lint migrate upgrade

run:
\tflask run --host=0.0.0.0 --port=8000

fmt:
\tblack .
\tisort .

lint:
\truff check .

migrate:
\tflask db migrate -m "initial"

upgrade:
\tflask db upgrade
