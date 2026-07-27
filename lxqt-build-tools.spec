%undefine _debugsource_packages

Summary:	Various packaging tools and scripts for LXQt applications
Name:		lxqt-build-tools
Version:	2.4.0
Release:	2
License:	BSD
Group:		System/Libraries
Url:		https://lxqt.org/
Source0:	https://github.com/lxqt/lxqt-build-tools/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildSystem:	cmake
BuildOption:	-DLXQT_ETC_XDG_DIR="%{_sysconfdir}/xdg"
BuildRequires:	cmake(Qt6Core)
BuildRequires:	git-core
BuildRequires:	pkgconfig(glib-2.0)

%description
Various packaging tools and scripts for LXQt applications.

%build -p
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8

%install -p
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8

%files
%doc README.md
%{_bindir}/lxqt2-transupdate
%{_datadir}/cmake/lxqt2-build-tools
