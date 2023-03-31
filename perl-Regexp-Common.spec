%define upstream_name    Regexp-Common
%define upstream_version 2017060201

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Regexp/Regexp-Common-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
%{upstream_name} module for perl provides commonly requested regular
expressions.

%prep
%autosetup -n %{upstream_name}-%{upstream_version} -p1

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
