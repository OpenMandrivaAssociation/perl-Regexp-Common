%define upstream_name    Regexp-Common
%define upstream_version 2013031301

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 2013031301
Release:	1

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Regexp/Regexp-Common-2013031301.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
%{upstream_name} module for perl provides commonly requested regular
expressions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%defattr(644,root,root,755)
%doc README TODO
%{_mandir}/man*/*
%{perl_vendorlib}/*

%changelog
* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2011041701.0.0-1mdv2011.0
+ Revision: 660015
- update to new version 2011041701

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 2011041602.0.0-2
+ Revision: 655211
- rebuild for updated spec-helper

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 2011041602

* Sun Jan 03 2010 Jérôme Quelin <jquelin@mandriva.org> 2010010201.0.0-1mdv2011.0
+ Revision: 485809
- update to 2010010201

* Thu Dec 31 2009 Jérôme Quelin <jquelin@mandriva.org> 2009123002.0.0-2mdv2010.1
+ Revision: 484376
- update to 2.122

* Wed Dec 30 2009 Jérôme Quelin <jquelin@mandriva.org> 2009123001.0.0-2mdv2010.1
+ Revision: 483888
- update to 2009123001

* Fri Aug 21 2009 Jérôme Quelin <jquelin@mandriva.org> 2.122.0-2mdv2010.0
+ Revision: 418941
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 2.122-2mdv2009.0
+ Revision: 268715
- rebuild early 2009.0 package (before pixel changes)

* Wed May 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.122-1mdv2009.0
+ Revision: 212227
- update to new version 2.122

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 2.120-2mdv2008.0
+ Revision: 25103
- rebuild


* Wed Mar 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.120-1mdk
- 2.120

* Fri Jan 07 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.119-1mdk
- 2.119

* Thu Jul 01 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.117-1mdk
- new version 2.117

* Sat Jun 19 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.115-1mdk
- 2.115
- disable test for now
- use %%makeinstall_std macro
- cosmetics

* Wed Apr 07 2004 Michael Scherer <misc@mandrake.org> 2.113-2mdk 
- REbuild to remove wrond Requires

* Wed Jun 04 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.113-1mdk
- from Peter Chen <petechen@netilla.com> :
	- Initial packaging.


