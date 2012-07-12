Name:		qpdfview
Summary:	Tabbed PDF viewer
Version:	0.3.1
Release:	1
License:	GPLv2
Group:		Office
URL:		https://launchpad.net/qpdfview
Source0:	https://launchpad.net/qpdfview/trunk/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(poppler-qt4)
BuildRequires:	cups-devel
BuildRequires:	qt4-devel

%description
qpdfview is a tabbed PDF viewer using the poppler library.

%prep
%setup -q

%build
%qmake_qt4
%make

%install
make install INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/qpdfview
%{_datadir}/applications/qpdfview.desktop
%{_mandir}/man1/qpdfview.1*
%{_datadir}/qpdfview/
