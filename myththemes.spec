
%define name    myththemes
%define version 0.24
%define gitversion v0.24-6-g9310
%define fixesdate 20110303
%define rel     1

%if %{fixesdate}
%define release %mkrel %fixesdate.%rel
%else
%define release %mkrel %rel
%endif

Summary: 	Additional themes for mythtv's frontend
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Video
URL: 		https://www.mythtv.org/
Source0: 	%{name}-%{version}.tar.bz2
%if %{fixesdate}
Patch1: fixes-%{gitversion}.patch
%endif
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: 	noarch
BuildRequires:	qt4-devel
BuildRequires:	libmyth-devel >= %{version}

%description
This package contains additional themes for mythtv-frontend and
mythtv-setup.

%package -n mythtv-themes-myththemes
Summary: 	Additional themes for mythtv's frontend
Group: 		Video
Provides: 	mythtv-theme-Titivillus
Obsoletes: 	mythtv-theme-Titivillus
Provides:	myththemes = %{version}
Obsoletes:	myththemes < 0.20-2

%description -n mythtv-themes-myththemes
This package contains additional themes for mythtv-frontend and
mythtv-setup.

Base themes are contained in the mythtv-themes-base package.

%prep
%setup -q
%autopatch -p1

%build
./configure --prefix=%{_prefix}
%make

%install
rm -rf %{buildroot}
%makeinstall INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}

%files -n mythtv-themes-myththemes
%defattr(-,root,root,-)
%doc COPYING
%{_datadir}/mythtv


%changelog
* Thu Mar 03 2011 Colin Guthrie <cguthrie@mandriva.org> 0.24-20110303.1mdv2011.0
+ Revision: 641477
- Update to latest fixes
- New version 0.24

* Thu Jun 17 2010 Colin Guthrie <cguthrie@mandriva.org> 0.23-25111.1mdv2010.1
+ Revision: 548213
- Update to latest fixes

* Tue May 25 2010 Colin Guthrie <cguthrie@mandriva.org> 0.23-24661.1mdv2010.1
+ Revision: 545876
- Updated to latest (post-release) -fixes

* Sun May 02 2010 Colin Guthrie <cguthrie@mandriva.org> 0.23-24269.1mdv2010.1
+ Revision: 541627
- New version: 0.23
- Update to latest -fixes

* Tue Nov 24 2009 Colin Guthrie <cguthrie@mandriva.org> 0.22-22869.1mdv2010.1
+ Revision: 469804
- Update to latest fixes

* Thu Nov 12 2009 Colin Guthrie <cguthrie@mandriva.org> 0.22-22793.1mdv2010.1
+ Revision: 465511
- Update to post release -fixes.
- Latest upstream fixes-branch

* Tue Oct 13 2009 Colin Guthrie <cguthrie@mandriva.org> 0.22-22400.0.1mdv2010.0
+ Revision: 457195
- Latest fixes

* Sun Oct 11 2009 Colin Guthrie <cguthrie@mandriva.org> 0.22-22345.0.1mdv2010.0
+ Revision: 456646
- Latest version
- Update to latest 0.22 code (currently trunk - release due shortly)

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.21-17137.2mdv2010.0
+ Revision: 430143
- rebuild

* Sat Sep 27 2008 Colin Guthrie <cguthrie@mandriva.org> 0.21-17137.1mdv2009.0
+ Revision: 288920
- Update to -fixes revision r17137

* Sat Mar 15 2008 Colin Guthrie <cguthrie@mandriva.org> 0.21-16505.1mdv2008.1
+ Revision: 188084
- Update to new fixes

* Sat Mar 01 2008 Colin Guthrie <cguthrie@mandriva.org> 0.21-0.16317.1mdv2008.1
+ Revision: 177222
- Update fixes branch
- Start tracking the 0.21-fixes branch ahead of official release.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Colin Guthrie <cguthrie@mandriva.org> 0.20.2-14301.2mdv2008.0
+ Revision: 86035
- Rebuild

* Thu Aug 30 2007 Colin Guthrie <cguthrie@mandriva.org> 0.20.2-14301.1mdv2008.0
+ Revision: 76261
- Update to 0.20.2 + fixes

* Tue Aug 14 2007 Colin Guthrie <cguthrie@mandriva.org> 0.20-3.13646.1mdv2008.0
+ Revision: 63247
- Update to 'fixes' r13646

* Tue Apr 17 2007 Anssi Hannula <anssi@mandriva.org> 0.20-3mdv2008.0
+ Revision: 13782
- raise release
- Import myththemes




* Sat Mar 24 2007 Anssi Hannula <anssi@mandriva.org> 0.20-2mdv2007.0
+ Revision: 148726
- own %%_datadir/mythtv
- rename to mythtv-themes-myththemes
- fix description, this is no longer in plf
- Import myththemes



* Tue Sep 12 2006 Anssi Hannula <anssi@zarb.org> 0.20-1plf2007.0
- 0.20

* Sun Jul 16 2006 Anssi Hannula <anssi@zarb.org> 0.19-3plf2007.0
- fix buildrequires

* Sun Apr 23 2006 Anssi Hannula <anssi@zarb.org> 0.19-2plf
- fix PLF reason

* Tue Feb 21 2006 Anssi Hannula <anssi@zarb.org> 0.19-1plf
- 0.19
- fix summary and description
- drop provides mythtv-themes

* Thu Oct 13 2005 Anssi Hannula <anssi@zarb.org> 0.18.2-0.7468.1plf
- upgrade to release-0-18-fixes svn branch revision 7468
- mkrel

* Tue Jun 21 2005 Austin Acton <austin@zarb.org> 0.18-1plf
- into PLF
- cleanup spec

* Fri May 20 2005 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.18-1.mdk10.2.thac
- Rebuilt for le2005

* Fri Apr 15 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.18.

* Thu Apr 14 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Split off themes onto their own (source) package.
