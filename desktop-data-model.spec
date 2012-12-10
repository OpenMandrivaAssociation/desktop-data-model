%define debug_package %{nil}
%define api   1
%define major 0
%define libname %mklibname ddm %{api}_%major
%define develname %mklibname -d ddm %api

Name:           desktop-data-model
Version:        1.2.5
Release:        6
Summary:        Engine providing live updates of online data to the desktop

Group:          Graphical desktop/GNOME
License:        LGPLv2+
URL:            http://live.gnome.org/OnlineDesktop
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%name/%name-%{version}.tar.bz2
Patch:		desktop-data-model-1.2.5-fix-format-strings.patch

BuildRequires:  pkgconfig(gdk-2.0) >= 2.6
BuildRequires:  pkgconfig(loudmouth-1.0) >= 1.0.3-3
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.61 
BuildRequires:  pkgconfig(gnome-desktop-2.0) >= 2.10.0
BuildRequires:  pkgconfig(gnome-vfs-2.0)
BuildRequires:  pkgconfig(sqlite3) >= 3.0.0
BuildRequires:  pkgconfig(xscrnsaver)
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
%configure2_5x --without-empathy LIBS="-lX11 -lm"
%make

%install
%makeinstall_std

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




%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.5-6mdv2011.0
+ Revision: 610231
- rebuild

* Wed Jan 13 2010 Götz Waschk <waschk@mandriva.org> 1.2.5-5mdv2010.1
+ Revision: 490512
- rebuild for new libgnome-desktop

* Sun Jan 03 2010 Götz Waschk <waschk@mandriva.org> 1.2.5-4mdv2010.1
+ Revision: 485927
- update build deps
- disable empathy support

* Fri Jan 02 2009 Götz Waschk <waschk@mandriva.org> 1.2.5-3mdv2009.1
+ Revision: 323281
- fix format strings

* Thu Nov 06 2008 Götz Waschk <waschk@mandriva.org> 1.2.5-2mdv2009.1
+ Revision: 300171
- rebuild for new  gnome-desktop

* Wed Oct 29 2008 Götz Waschk <waschk@mandriva.org> 1.2.5-1mdv2009.1
+ Revision: 298177
- new version
- update build deps
- fix source URL

* Sat Sep 06 2008 Frederic Crozat <fcrozat@mandriva.com> 1.2.4-2mdv2009.0
+ Revision: 282007
- Add conflicts to ease upgrade from Mdv 2008.1

* Wed Jul 23 2008 Götz Waschk <waschk@mandriva.org> 1.2.4-1mdv2009.0
+ Revision: 242272
- import desktop-data-model


* Wed Jul 23 2008 Götz Waschk <waschk@mandriva.org> 1.2.4-1mdv2009.0
- adapt for mandriva

* Thu Jun 05 2008 Caolán McNamara <caolanm@redhat.com> - 1.2.4-2
- rebuild for dependancies

* Thu Apr 24 2008 Colin Walters <walters@redhat.com> - 1.2.4-1
- new upstream

* Fri Apr 04 2008 Colin Walters <walters@redhat.com> - 1.2.3-1
- new upstream

* Thu Mar 20 2008 Colin Walters <walters@redhat.com> - 1.2.2-1
- new upstream

* Wed Feb 27 2008 Colin Walters <walters@redhat.com> - 1.2.0-2
- Require desktop-data-model from -devel
- Add conflicts: on earlier Mugshot versions since we both ship libddm-1.so

* Tue Jan 29 2008 Colin Walters <walters@redhat.com> - 1.2.0-1
- initial splat into spec
