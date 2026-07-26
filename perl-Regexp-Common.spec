%define upstream_name    Regexp-Common
Name:		perl-%{upstream_name}
Version:	2017060201
Release:	4

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Regexp/Regexp-Common-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
%{upstream_name} module for perl provides commonly requested regular
expressions.

%prep
%autosetup -n %{upstream_name}-%{version} -p1

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc README TODO
%{_mandir}/man*/*
%{perl_vendorlib}/*
