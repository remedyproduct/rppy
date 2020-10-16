build: clean
	python setup.py sdist bdist_wheel

deploy: build
	python -m twine upload dist/* 

clean:
	rm -rf ./build
	rm -rf ./rppy.egg-info
