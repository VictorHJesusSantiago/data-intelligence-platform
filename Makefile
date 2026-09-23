.PHONY: test validate demo serve clean
test:
	PYTHONPATH=src python -m unittest discover -s tests -v
validate:
	PYTHONPATH=src python -m dip validate
demo:
	PYTHONPATH=src python -m dip demo
serve:
	PYTHONPATH=src python -m dip serve
clean:
	python -c "from pathlib import Path; import shutil; [shutil.rmtree(p) for p in Path('.').rglob('__pycache__')]"
