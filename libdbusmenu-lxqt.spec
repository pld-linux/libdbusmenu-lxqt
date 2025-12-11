%define         qtver           6.6.0

Summary:	Library providing a way to implement DBusMenu protocol for LXQt
Name:		libdbusmenu-lxqt
Summary(pl.UTF-8):	Biblioteka umożliwiająca implementację protokołu DBusMenu dla LXQt
Version:	0.3.0
Release:	1
License:	LGPL-2.0-or-later
URL:		https://lxqt-project.org/
Source0:	https://github.com/lxqt/libdbusmenu-lxqt/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	2ccc567ac1481ac1d065639cb7bf8ad7
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.18.0
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library providing a way to implement DBusMenu protocol for LXQt.

%description -l pl.UTF-8
Biblioteka umożliwiająca implementację protokołu DBusMenu dla LXQt.

%package devel
Summary:	Qt - development files for %{name}
Summary(pl.UTF-8):	Pliki rozwojowe dla %{name}
Requires:	%{name} = %{version}-%{release}

%description devel
Files used for developing and building software that uses %{name}.

%description devel -l pl.UTF-8
Pliki używane do tworzenia i budowania oprogramowania, które
wykorzystuje %{name}.

%prep
%setup -q

%build
%cmake -B build
%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
    DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%{_libdir}/libdbusmenu-lxqt.so.0
%{_libdir}/libdbusmenu-lxqt.so.%{version}

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/dbusmenu-lxqt
%{_includedir}/dbusmenu-lxqt
%{_libdir}/libdbusmenu-lxqt.so
%{_pkgconfigdir}/dbusmenu-lxqt.pc

%clean
rm -rf $RPM_BUILD_ROOT
