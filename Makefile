NAME=$(shell awk '/Name/ { print $$2 }' *.spec)
VERSION=$(shell awk '/Version/ { print $$2 }' *.spec)

all:

install: 

archive:
	@git archive --prefix=$(NAME)-$(VERSION)/ HEAD -o $(NAME)-$(VERSION).tar
	@bzip2 -f $(NAME)-$(VERSION).tar
	@echo "$(NAME)-$(VERSION).tar.bz2 created"
clean:
	rm -f *~ *bz2
