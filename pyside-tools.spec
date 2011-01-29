Name: pyside-tools
Version: 0.2.6
Release: %mkrel 1
License: LGPLv2+
Summary: PySide development tools
Group: Development/KDE and Qt
URL: http://www.pyside.org
Source0: http://www.pyside.org/files/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: cmake
BuildRequires: qt4-devel
BuildRequires: phonon-devel
BuildRequires: generatorrunner-devel >= 0.6.4
BuildRequires: shiboken-devel >= 1.0.0
Buildrequires: python-devel
Buildrequires: pyside-devel
Requires: pyside-phonon
Requires: pyside-core
Requires: pyside-declarative
Requires: pyside-gui
Requires: pyside-help
Requires: pyside-multimedia
Requires: pyside-network
Requires: pyside-opengl
Requires: pyside-script
Requires: pyside-scripttools
Requires: pyside-sql
Requires: pyside-test
Requires: pyside-xmlpatterns
Requires: pyside-xml
Requires: pyside-uitools
Requires: pyside-svg
Requires: pyside-webkit

%description
PySide tools includes pyside-uic which generate Python code from ui files 
created with Qt Designer, pyside-rcc generate python source code containing
data specified in a Qt resource file and pyside-lupdate finds Qt Linguist
translatable strings, and updates the translation files. 

%files
%defattr(-,root,root,-)
%{py_platsitedir}/*
%{_bindir}/pyside-lupdate
%{_bindir}/pyside-rcc
%{_bindir}/pyside-uic

%prep
%setup -q -n %{name}-%{version}

%build
%define Werror_cflags %nil
%cmake \
	-DQT_SRC_DIR=%buildroot/%qt4dir \
	-DQT_PHONON_INCLUDE_DIR=%_includedir/phonon
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %buildroot
