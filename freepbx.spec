Summary:	FreePBX - Asterisk Management Portal (AMP)
Summary(pl):	FreePBX - interfejs WWW do Asteriska
Name:		freepbx
Version:	2.0.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/amportal/%{name}-%{version}.tar.gz
# Source0-md5:	aa100b6928a3e1a61603fb969485381a
URL:		http://www.coalescentsystems.ca/
Requires:	php-program
Requires:	php-pear-DB
Requires:	php-pcre
Requires:	libxml2
Requires:	libtiff
Requires:	lame

#Requires:	httpd
#Requires:	Apache2
#Requires:	mysql-client
#Requires:	mysql

Requires:	php-mysql
Requires:	php-gettext
Requires:	php-posix
Requires:	php-gd
Requires:	openssl
Requires:	perl
Requires:	perl-CPAN
Requires:	bison
Requires:	ncurses
Requires:	audiofile
Requires:	curl
Requires:	sox
Requires:	perl-Net-Telnet
Requires:	perl-IPC-Signal
Requires:	perl-Proc-WaitStat
Requires:	asterisk-perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Coalescent Systems Inc. launched the freePBX (formerly Asterisk
Management Portal) project to bring together best-of-breed
applications to produce a standardized implementation of Asterisk
complete with web-based administrative interface.

%description -l pl

%prep
%setup -q
#%patch0 -p1
# undos the source
#find '(' -name '*.php' -o -name '*.inc' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/{cgi-bin,agi-bin,astetc,bin,htdocs,htdocs_panel,mohmp3,sbin,sounds}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/htdocs/{_asterisk,admin,recordings}

cd ./amp_conf
cp -R htdocs/* $RPM_BUILD_ROOT%{_datadir}/%{name}/htdocs
install cgi-bin/* $RPM_BUILD_ROOT%{_datadir}/%{name}/cgi-bin
install agi-bin/* $RPM_BUILD_ROOT%{_datadir}/%{name}/agi-bin
install bin/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/bin
install mohmp3/* $RPM_BUILD_ROOT%{_datadir}/%{name}/mohmp3
install sounds/* $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds

#TODO
#htdocs_panel
#sbin
#astetc

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
#%%dir %{_sysconfdir}
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
#%attr(755,root,root) %{_bindir}/*
#%{_datadir}/%{name}
