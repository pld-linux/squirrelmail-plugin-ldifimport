%define		_plugin	ldifimport
%define		mversion	1.2.x
Summary:	A squirrelmail LDIF Address Book Import plug-in
Summary(pl.UTF-8):	Wtyczka squirrelmaila do importu książki adresowej LDIF
Name:		squirrelmail-plugin-%{_plugin}
Version:	1.4
Release:	2
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}-%{version}-%{mversion}.tar.gz
# Source0-md5:	0d280a925c6e2e16310621eeace7b843
URL:		http://www.squirrelmail.org/plugin_view.php?id=18
Requires:	squirrelmail >= 1.4.0
Provides:       squirrelmail-compatibility >= 2.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_datadir}/squirrelmail/plugins/%{_plugin}
%define		_sysconfdir	/etc/webapps/squirrelmail

%description
Imports nearly all address book data. If the address book you wish to
import is not in LDIF format, this plugin will direct you to the
InterGuru web site where you can convert many popular address book
formats into LDIF format in order to import it with this plugin. 

%description -l pl.UTF-8
Ta wtyczka importuje prawie wszystkie dane z książki adresowej. Jeśli
książka adresowa, którą chcemy zaimportować, nie jest w formacie LDIF,
ta wtyczka przekieruje na stronę WWW InterGuru, gdzie można
przekonwertować wiele popularnych formatów książek adresowych do
formatu LDIF w celu zaimportowania przy użyciu tej wtyczki.

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir} $RPM_BUILD_ROOT%{_sysconfdir}

mv config.php $RPM_BUILD_ROOT%{_sysconfdir}/%{_plugin}_config.php
install *.php $RPM_BUILD_ROOT%{_plugindir}
ln -s %{_sysconfdir}/%{_plugin}_config.php $RPM_BUILD_ROOT%{_plugindir}/config.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{_plugin}_config.php
%dir %{_plugindir}
%{_plugindir}/*.php
