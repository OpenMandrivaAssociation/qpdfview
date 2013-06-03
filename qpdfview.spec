Name:		qpdfview
Summary:	Light-weight tabbed PDF, DJVU and PostScript viewer
Version:	0.4.3
Release:	1
License:	GPLv2+
Group:		Office
URL:		https://launchpad.net/qpdfview
Source0:	https://launchpad.net/qpdfview/trunk/%{version}/+download/%{name}-%{version}.tar.gz
Patch0:		qpdfview-0.4-desktop.patch
BuildRequires:	imagemagick
BuildRequires:	cups-devel
BuildRequires:	magic-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(ddjvuapi)
BuildRequires:	pkgconfig(libspectre)
BuildRequires:	pkgconfig(poppler-qt4)
BuildRequires:	pkgconfig(zlib)

%description
qpdfview is a light-weight tabbed PDF, DJVU and PostScript viewer.

%prep
%setup -q
%patch0 -p0

%build
lrelease %{name}.pro
%qmake_qt4 \
	QMAKE_CXXFLAGS_RELEASE=  \
	PLUGIN_INSTALL_PATH="%{_libdir}/%{name}" \
	%{name}.pro
%make

%install
make install INSTALL_ROOT=%{buildroot}

# install menu icons
for N in 16 32 48 64 128;
do
convert icons/%{name}.svg -resize ${N}x${N} $N.png;
install -D -m 0644 $N.png %{buildroot}%{_iconsdir}/hicolor/${N}x${N}/apps/%{name}.png
done
install -D -m 0644 icons/%{name}.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg

%find_lang %{name} --with-qt

%files -f %{name}.lang
%{_bindir}/%{name}
%{_libdir}/%{name}/libqpdfview_djvu.so
%{_libdir}/%{name}/libqpdfview_pdf.so
%{_libdir}/%{name}/libqpdfview_ps.so
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/%{name}.svg
%{_datadir}/%{name}/help.html
%{_datadir}/%{name}/qpdfview_ast.qm
%{_iconsdir}/hicolor/*/apps/%{name}.*
