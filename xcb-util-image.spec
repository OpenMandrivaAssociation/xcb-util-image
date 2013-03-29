%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define develnamest %mklibname %{name} -d -s

Summary:	xcb-util's xcb-image
Name:		xcb-util-image
Version:	0.3.9
Release:	2
Url:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
License:	MIT
Group:		System/X11
BuildRequires:	xcb-util-devel >= 0.3.9
BuildRequires:	x11-util-macros

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n %{libname}
Summary:	xcb-util-image library package
Group:		System/X11

%description -n %{libname}
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

This is the xcb-util-image library package.

%package -n %{develname}
Summary:	xcb-util-image development files
Group:		Development/C
Provides:	libxcb-util-image-devel = %{version}-%{release}
Provides:	xcb-util-image-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Conflicts:	%{mklibname xcb-util -d} < 0.3.9
Conflicts:	%{mklibname xcb-util -d -s} < 0.3.9

%description -n %{develname}
This pakcage includes the development files required to build software against
%{name}.


%package -n %{develnamest}
Summary:	xcb-util-image development files
Group:		Development/C
Provides:	libxcb-util-image-devel-static = %{version}-%{release}
Provides:	xcb-util-image-devel-static = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	xcb-util-image-devel = %{version}-%{release}
Conflicts:	%{mklibname xcb-util -d} < 0.3.9
Conflicts:	%{mklibname xcb-util -d -s} < 0.3.9

%description -n %{develnamest}
This pakcage includes the development files required to build software against
%{name}.


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%{_libdir}/libxcb-image.so.%{major}*

%files -n %{develname}
%doc ChangeLog NEWS README
%{_includedir}/xcb/xcb_image.h
%{_includedir}/xcb/xcb_pixel.h
%{_includedir}/xcb/xcb_bitops.h
%{_libdir}/libxcb-image.so
%{_libdir}/pkgconfig/xcb-image.pc

%files -n %{develnamest}
%{_libdir}/libxcb-image.a


%changelog
* Mon Jun 04 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.3.9-1
+ Revision: 802326
- description fix
- version update 0.3.9

* Wed Oct 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.8-1
+ Revision: 707429
- import xcb-util-image

