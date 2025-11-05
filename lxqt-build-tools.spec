%undefine _debugsource_packages

Summary:	Various packaging tools and scripts for LXQt applications
Name:		lxqt-build-tools
Version:	2.3.0
Release:	1
License:	BSD
Group:		System/Libraries
Url:		https://lxqt.org/
Source0:	https://github.com/lxqt/lxqt-build-tools/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	ninja
BuildRequires:	cmake
BuildRequires:	cmake(Qt6Core)
BuildRequires:	git-core
BuildRequires:	pkgconfig(glib-2.0)

%description
Various packaging tools and scripts for LXQt applications.

%prep
%autosetup -p1

%cmake -DLXQT_ETC_XDG_DIR="%{_sysconfdir}/xdg" -G Ninja

%build
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja -C build

%install
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja_install -C build

%files
%doc README.md
%{_bindir}/lxqt2-transupdate
%{_datadir}/cmake/lxqt2-build-tools
