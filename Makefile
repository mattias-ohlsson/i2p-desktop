NAME=$(shell awk '/Name/ { print $$2 }' *.spec)
VERSION=$(shell awk '/Version/ { print $$2 }' *.spec)

all:

install:
	# We need to specify dir to use the prefix 
	@desktop-file-install --dir=${PREFIX}/usr/share/applications/ \
	 i2p-router-console.desktop
	# Install the i2p icon
	@install -D icons/scalable/i2p-router-console.svg \
	 ${PREFIX}/usr/share/icons/hicolor/scalable/apps/i2p-router-console.svg
	@echo "Do not forget to run update-desktop-database"

archive:
	@git archive --prefix=$(NAME)-$(VERSION)/ HEAD -o $(NAME)-$(VERSION).tar
	@bzip2 -f $(NAME)-$(VERSION).tar
	@echo "$(NAME)-$(VERSION).tar.bz2 created"
clean:
	rm -f *~ *bz2
