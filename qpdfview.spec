Name:		qpdfview
Summary:	Light-weight tabbed PDF, DJVU and PostScript viewer
Version:	0.4.18
Release:	2
License:	GPLv2+
Group:		Office
URL:		https://launchpad.net/qpdfview
Source0:	https://launchpad.net/qpdfview/trunk/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires:	imagemagick
BuildRequires:	cups-devel
BuildRequires:	magic-devel
BuildRequires:	qt5-devel
BuildRequires:	qt5-linguist-tools
BuildRequires:	pkgconfig(ddjvuapi)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	pkgconfig(libspectre)
BuildRequires:	pkgconfig(poppler-qt5)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(krb5)

%description
qpdfview is a light-weight tabbed PDF, DJVU and PostScript viewer.

%prep
%setup -q
# % patch0 -p1

%build
%{_libdir}/qt5/bin/lrelease %{name}.pro
%qmake_qt5 \
        QMAKE_STRIP="" \
	PLUGIN_INSTALL_PATH="%{_libdir}/%{name}" \
	DATA_INSTALLPATH="%{_datadir}/%{name}" \
	%{name}.pro
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}
install -Dm 0644 icons/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -Dm 0644 icons/%{name}.svg %{buildroot}%{_datadir}/%{name}/%{name}.svg

# install menu icons
for N in 16 32 48 64 128;
do
convert icons/%{name}.svg -resize ${N}x${N} $N.png;
install -D -m 0644 $N.png %{buildroot}%{_iconsdir}/hicolor/${N}x${N}/apps/%{name}.png
done
install -D -m 0644 icons/%{name}.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg


%files  
%{_bindir}/%{name}
%{_libdir}/%{name}/libqpdfview_djvu.so
%{_libdir}/%{name}/libqpdfview_pdf.so
%{_libdir}/%{name}/libqpdfview_ps.so
%{_libdir}/%{name}/libqpdfview_image.so
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/%{name}.svg
%{_datadir}/%{name}/help*.html
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/appdata/*
%{_datadir}/qpdfview/qpdfview_*.qm
