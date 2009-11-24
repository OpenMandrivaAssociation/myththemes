
%define name    myththemes
%define version 0.22
%define fixes 22869
%define rel     1

%define release %mkrel %fixes.%rel

Summary: 	Additional themes for mythtv's frontend
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Video
URL: 		http://www.mythtv.org/
Source0: 	%{name}-%{version}-%{fixes}.tar.bz2
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
