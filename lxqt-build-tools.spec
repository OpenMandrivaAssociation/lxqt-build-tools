%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Various packaging tools and scripts for LXQt applications
Name:		lxqt-build-tools
Version:	0.4.0
Release:	1
License:	BSD
Group:		System/Libraries
Url:		http://lxqt.org/
Source0:	https://github.com/lxde/lxqt-build-tools/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	cmake(Qt5Core)
BuildRequires:	git-core

%description
Various packaging tools and scripts for LXQt applications.

%prep
%setup -q

%cmake_qt5 -DLXQT_ETC_XDG_DIR="%{_sysconfdir}/xdg/qt5"

%build
%make -C build

%install
%makeinstall_std -C build

%files
%doc README.md
%{_datadir}/cmake/lxqt-build-tools
