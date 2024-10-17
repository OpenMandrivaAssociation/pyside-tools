Name:		pyside-tools
Version:	0.2.14
Release:	3
License:	LGPLv2+
Summary:	PySide development tools
Group:		Development/KDE and Qt
URL:		https://www.pyside.org
Source0:	http://www.pyside.org/files/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	phonon-devel
BuildRequires:	shiboken-devel
Buildrequires:	python-devel
Buildrequires:	pyside-devel
Requires:	pyside-phonon
Requires:	pyside-core
Requires:	pyside-declarative
Requires:	pyside-gui
Requires:	pyside-help
Requires:	pyside-multimedia
Requires:	pyside-network
Requires:	pyside-opengl
Requires:	pyside-script
Requires:	pyside-scripttools
Requires:	pyside-sql
Requires:	pyside-test
Requires:	pyside-xmlpatterns
Requires:	pyside-xml
Requires:	pyside-uitools
Requires:	pyside-svg
Requires:	pyside-webkit

%description
PySide tools includes pyside-uic which generate Python code from ui files 
created with Qt Designer, pyside-rcc generate python source code containing
data specified in a Qt resource file and pyside-lupdate finds Qt Linguist
translatable strings, and updates the translation files.

%files
%{py_platsitedir}/*
%{_bindir}/pyside-lupdate
%{_bindir}/pyside-rcc
%{_bindir}/pyside-uic
%{_mandir}/man1/*

%prep
%setup -q

%build
%define Werror_cflags %nil
%cmake \
	-DQT_SRC_DIR=%{buildroot}%{qt4dir} \
	-DQT_PHONON_INCLUDE_DIR=%{_includedir}/phonon
%make

%install
%makeinstall_std -C build

