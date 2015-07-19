%define	_class	Net
%define	_subclass	IMAP
%define	modname	%{_class}_%{_subclass}

Summary:	An implementation of the IMAP protocol

Name:		php-pear-%{modname}
Version:	1.1.3
Release:	5
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Net_IMAP/
Source0:	http://download.pear.php.net/package/Net_IMAP-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
Provides an implementation of the IMAP4Rev1 protocol using PEAR's
Net_Socket and Auth_SASL class.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{modname}
%{_datadir}/pear/packages/%{modname}.xml


