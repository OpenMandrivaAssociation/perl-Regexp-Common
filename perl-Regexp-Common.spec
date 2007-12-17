%define module  Regexp-Common
%define	name	perl-%{module}
%define	version	2.120
%define	release	%mkrel 2
%define	pdir	Regexp

Summary:	%{module} module for perl
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/search?dist=%{module}
BuildArch:	noarch
BuildRequires:	perl-devel 

%description
%{module} module for perl provides commonly requested regular
expressions.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%{_mandir}/man*/*
%{perl_vendorlib}/*

