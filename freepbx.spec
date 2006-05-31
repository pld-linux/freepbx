# TODO
# - remowe jpgraph, add patch
# - pl translations
Summary:	FreePBX - Asterisk Management Portal (AMP)
Summary(pl):	FreePBX - interfejs WWW do Asteriska
Name:		freepbx
Version:	2.0.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/amportal/%{name}-%{version}.tar.gz
# Source0-md5:	aa100b6928a3e1a61603fb969485381a
#Source1:	%{name}.conf
#Source2:	%{name}-config.php
Patch0:		%{name}-jpgraph.patch
URL:		http://www.coalescentsystems.ca/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}(DB_Driver) = %{version}-%{release}
#Requires:	apache >= 2
#Requires:	asterisk >= 1.2
Requires:	asterisk-perl
Requires:	audiofile
Requires:	bison
Requires:	curl
Requires:	lame
Requires:	libtiff
Requires:	libxml2
#Requires:	mysql
#Requires:	mysql-client
Requires:	ncurses
Requires:	openssl
Requires:	perl
Requires:	perl-CPAN
Requires:	perl-IPC-Signal
Requires:	perl-Net-Telnet
Requires:	perl-Proc-WaitStat
Requires:	php-gd
Requires:	php-gettext
Requires:	php-pcre
Requires:	php-pear-DB
Requires:	php-posix
Requires:	php-program
Requires:	sox
Requires:	jpgraph
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Coalescent Systems Inc. launched the freePBX (formerly Asterisk
Management Portal) project to bring together best-of-breed
applications to produce a standardized implementation of Asterisk
complete with web-based administrative interface.

%description -l pl
Coalescent Systems Inc. uruchomi³o projekt freePBX (poprzednio
Asterisk Management Portal) aby po³±czyæ najlepsze istniej±ce
aplikacje w celu stworzenia ustandaryzowanej implementacji
Asteriska uzupe³nionego o interfejs administracyjny WWW.

%package db-mysql
Summary:	FreePBX DB Driver for MySQL
Summary(pl):	Sterownik bazy danych MySQL dla FreePBX
Group:		Applications/WWW
Requires:	php-mysql
Provides:	%{name}(DB_Driver) = %{version}-%{release}

%description db-mysql
This virtual package provides MySQL database backend for FreePBX.

%description db-mysql -l pl
Ten wirtualny pakiet dostarcza backend bazy danych MySQL dla
FreePBX.

%prep
%setup -q
%patch0 -p1
find '(' -name '*.php' -o -name '*.inc' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'
rm -dfr htdocs/admin/cdr/jpgraph_lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/{cgi-bin,agi-bin,astetc,bin,htdocs,htdocs_panel,mohmp3,sbin,sounds}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d
install -d $RPM_BUILD_ROOT%{_bindir}

cd amp_conf
cp -R htdocs/* $RPM_BUILD_ROOT%{_datadir}/%{name}/htdocs
install cgi-bin/* $RPM_BUILD_ROOT%{_datadir}/%{name}/cgi-bin
install agi-bin/* $RPM_BUILD_ROOT%{_datadir}/%{name}/agi-bin
install bin/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/bin
install mohmp3/* $RPM_BUILD_ROOT%{_datadir}/%{name}/mohmp3
install sounds/* $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds

#install init/op_panel_redhat.sh $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/%{name}
#install op_server.pl	$RPM_BUILD_ROOT%{_bindir}
#TODO
#htdocs_panel
#sbin
#astetc

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add %{name}
%service %{name} restart

%preun
if [ "$1" = "0" ]; then
	%service -q %{name} stop
	/sbin/chkconfig --del %{name}
fi

%files
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
#%attr(754,root,root) /etc/rc.d/init.d/%{name}
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
#%dir %{_sysconfdir}
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
#%attr(755,root,root) %{_bindir}/*
#%{_datadir}/%{name}
%lang(pt_BR) %{_datadir}/%{name}/htdocs/recordings/locale/de_DE/LC_MESSAGES/*
%lang(el_GR) %{_datadir}/%{name}/htdocs/recordings/locale/el_GR/LC_MESSAGES/*
%lang(es) %{_datadir}/%{name}/htdocs/recordings/locale/es_ES/LC_MESSAGES/*
%lang(fr) %{_datadir}/%{name}/htdocs/recordings/locale/fr_FR/LC_MESSAGES/*
%lang(he_IL) %{_datadir}/%{name}/htdocs/recordings/locale/he_IL/LC_MESSAGES/*
%lang(hu) %{_datadir}/%{name}/htdocs/recordings/locale/hu_HU/LC_MESSAGES/*
%lang(it) %{_datadir}/%{name}/htdocs/recordings/locale/it_IT/LC_MESSAGES/*
%lang(pt_BR) %{_datadir}/%{name}/htdocs/recordings/locale/pt_BR/LC_MESSAGES/*
%lang(sv_SE) %{_datadir}/%{name}/htdocs/recordings/locale/sv_SE/LC_MESSAGES/*
#%lang(pl) %{_datadir}/%{name}/htdocs/recordings/locale/pl_PL/LC_MESSAGES/*

%lang(de) %{_datadir}/%{name}/htdocs/admin/i18n/de_DE/LC_MESSAGES/*
%lang(es) %{_datadir}/%{name}/htdocs/admin/i18n/es_ES/LC_MESSAGES/*
%lang(fr) %{_datadir}/%{name}/htdocs/admin/i18n/fr_FR/LC_MESSAGES/*
%lang(it) %{_datadir}/%{name}/htdocs/admin/i18n/it_IT/LC_MESSAGES/*
#%lang(pl) %{_datadir}/%{name}/htdocs/admin/i18n/pl_PL/LC_MESSAGES/*

%files db-mysql
%defattr(644,root,root,755)
