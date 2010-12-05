%define api   1
%define major 0
%define libname %mklibname ddm %{api}_%major
%define develname %mklibname -d ddm %api

Name:           desktop-data-model
Version:        1.2.5
Release:        %mkrel 6
Summary:        Engine providing live updates of online data to the desktop

Group:          Graphical desktop/GNOME
License:        LGPLv2+
URL:            http://live.gnome.org/OnlineDesktop
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%name/%name-%{version}.tar.bz2
Patch:		desktop-data-model-1.2.5-fix-format-strings.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  gtk2-devel >= 2.6
BuildRequires:  loudmouth-devel >= 1.0.3-3
BuildRequires:  dbus-glib-devel >= 0.61 
BuildRequires:  gnome-desktop-devel >= 2.10.0
BuildRequires:  gnome-vfs2-devel
BuildRequires:  sqlite3-devel >= 3.0.0
BuildRequires:  libxscrnsaver-devel
Conflicts: mugshot < 1.2.1-1mdv

%description
desktop-data-model provides an engine and client library that allow
desktop applications to retrieve data from the online.gnome.org server
and elsewhere and get updates when the data changes. This allows
creating applications that provide a live display of information
from the Internet.

%package -n %{libname}
Group: System/Libraries
Summary: Engine providing live updates of online data to the desktop
Requires: %name >= %version

%description -n %libname
desktop-data-model provides an engine and client library that allow
desktop applications to retrieve data from the online.gnome.org server
and elsewhere and get updates when the data changes. This allows
creating applications that provide a live display of information
from the Internet.

%package -n %develname
Summary: Development headers for Online Desktop Data Model
Group: Development/C
Requires: %libname = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}
Provides: libddn-devel = %version-%release

%description -n %develname
This package contains libraries for Online Desktop Data Model.

%prep
%setup -q
%patch -p1

%build
%configure2_5x --without-empathy
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo %{version} > %{_datadir}/desktop-data-model/version

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig
%endif


%files
%defattr(-,root,root,-)
%doc COPYING
%ghost %{_datadir}/desktop-data-model/version
%{_libexecdir}/desktop-data-engine
%{_datadir}/dbus-1/services/*.service

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/libddm-%{api}.so.%{major}*


%files -n %develname
%dir %{_includedir}/ddm-1
%{_includedir}/ddm-1/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_libdir}/*.la

