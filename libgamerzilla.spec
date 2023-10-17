%define libname %mklibname gamerzilla
%define devname %mklibname -d gamerzilla

Summary: Gamerzilla Integration Library
Name: libgamerzilla
Version: 0.1.3
Release: 1
Group:  System/libraries/games
License: zlib
URL: https://github.com/dulsi/libgamerzilla
Source0: http://www.identicalsoftware.com/gamerzilla/%{name}-%{version}.tgz

BuildRequires: cmake
BuildRequires: pkgconfig(jansson)
BuildRequires: pkgconfig(libcurl)
 
%description
Gamerzilla is trophy/achievement system for games. It integrates with a
hubzilla plugin to display your results online. Games can either connect
directly to hubzilla or connect to a game launcher with using this
library.
 
%package -n %{libname}
Summary:        Shared library for %{name}

%description -n %{libname}
Gamerzilla is trophy/achievement system for games. 

%package -n %{devname}
Summary:        Development files for %{name}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains development files for %{name}.

%package server
Summary: Simple Gamerzilla server to relay information to Hubzilla
 
%description server
The gamerzillaserver listens for trophies awarded by games. It logs into
the user's Hubzilla server and passes on the awards.
 
%prep
%autosetup -p1
 
%build
%cmake
%make_build

%install
%make_install -C build

%files -n %{libname}
%doc README
%license LICENSE
%{_libdir}/libgamerzilla.so.0
%{_libdir}/libgamerzilla.so.0.1.0
 
%files -n %{devname}
%{_includedir}/gamerzilla/
%{_libdir}/libgamerzilla.so
%{_libdir}/pkgconfig/gamerzilla.pc
%{_datadir}/vala/vapi/gamerzilla.vapi
%{_datadir}/vala/vapi/gamerzilla.deps
 
%files server
%{_bindir}/gamerzillaserver
