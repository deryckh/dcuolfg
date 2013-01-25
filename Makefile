all:
	@echo "See README for building and running info."
	@echo "The Makefile is solely for helper stuff like make clean."

check:
	./bin/django-admin.py test accounts characters missions

clean:
	rm -rf bin build dcuolfg.egg-info dist include lib local

.PHONY: all check clean
