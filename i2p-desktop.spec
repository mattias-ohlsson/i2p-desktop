Name:		i2p-desktop
Version:	0.1
Release:	1%{?dist}
Summary:	I2P Router Console desktop file

Group:		Applications/Internet

# From www.i2p2.de/licenses.html
License:	Public domain
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
make install DESTDIR=$RPM_BUILD_ROOT


%post
/usr/bin/update-desktop-database &> /dev/null || :


%postun
/usr/bin/update-desktop-database &> /dev/null || :


%files
%doc
%{_datadir}/applications/i2p-router-console.desktop


%changelog

