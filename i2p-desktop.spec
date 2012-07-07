Name:		i2p-desktop
Version:	0.6
Release:	1%{?dist}
Summary:	I2P Router Console desktop file

Group:		Applications/Internet

# License from www.i2p2.de/licenses.html
# and http://projects.gnome.org/evince/
License:	GPLv2 and Public Domain
URL:		http://ipredia.org
Source0:	%{name}-%{version}.tar.bz2

## BuildRequires
# desktop-file-utils  - desktop-file-install (Makefile)

BuildRequires:	desktop-file-utils

## Requires
# xdg-utils           - xdg-open
# desktop-file-utils  - update-desktop-database
# i2p                 - for the i2p console

Requires:	  i2p
Requires:         xdg-utils
Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils

BuildArch: 	noarch


%description
This package add a desktop file for the I2P Router Console.


%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT


%post
/usr/bin/update-desktop-database &> /dev/null || :


%postun
/usr/bin/update-desktop-database &> /dev/null || :


%files
%doc
%{_datadir}/applications/i2p-router-console.desktop
%{_datadir}/icons/hicolor/*/apps/i2p-router-console.*

%changelog
* Sat Jul 7 2012 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.6-1
- add more languages

* Mon Jun 21 2012 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.5-1
- new icon

* Mon Jun 18 2012 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.1-2
- include icon

* Mon Jun 18 2012 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.1-1
- initial package
