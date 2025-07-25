# TODO:
# - create more subpackages? (vamp-sdk, vamp-hostsdk)
#
%define		srcname	vamp-plugin-sdk
Summary:	vamp - API for audio analysis and feature extraction plugins
Summary(pl.UTF-8):	vamp - API dla wtyczek analizy i wydobywania cech dźwięku
Name:		vamp
Version:	2.10.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://code.soundsoftware.ac.uk/projects/vamp-plugin-sdk/files
Source0:	https://code.soundsoftware.ac.uk/attachments/download/2691/%{srcname}-%{version}.tar.gz
# Source0-md5:	848f7ac0227b5c783bee0dd7a5cb3642
Patch0:		%{name}-link.patch
# for plugins: http://www.vamp-plugins.org/
URL:		https://code.soundsoftware.ac.uk/projects/vamp-plugin-sdk
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		vampplugindir	%{_libdir}/vamp

%description
Vamp is an audio processing plugin system for plugins that extract
descriptive information from audio data - typically referred to as
audio analysis plugins or audio feature extraction plugins.

%description -l pl.UTF-8
Vamp to system wtyczek przetwarzających dźwięk dla wtyczek
wydobywających informacje opisowe z danych dźwiękowych - przeważnie
nazywane wtyczkami analizy dźwięku lub wtyczkami wydobywającymi cechy
dźwięku.

%package devel
Summary:	Header files for vamp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki vamp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:4.7

%description devel
Header files for vamp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki vamp.

%package static
Summary:	Static vamp library
Summary(pl.UTF-8):	Statyczna biblioteka vamp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static vamp library.

%description static -l pl.UTF-8
Statyczna biblioteka vamp.

%package plugins-example
Summary:	Example vamp plugins
Summary(pl.UTF-8):	Przykładowe wtyczki vampa
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description plugins-example
Example vamp plugins.

%description plugins-example -l pl.UTF-8
Przykładowe wtyczki vampa.

%prep
%setup -q -n %{srcname}-%{version}
%patch -P0 -p1

%build
%configure
%{__make} \
	CXX="%{__cxx}" \
	LDFLAGS="%{rpmcxxflags} %{rpmldflags}" \
	INSTALL_SDK_LIBS="%{_libdir}" \
	INSTALL_PLUGINS="%{vampplugindir}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_SDK_LIBS="%{_libdir}" \
	INSTALL_PLUGINS="%{vampplugindir}" \
	INSTALL_PKGCONFIG="%{_pkgconfigdir}"

# obsoleted by pkg-config; also, not real libtool files
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvamp-*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG COPYING README README.compat
%attr(755,root,root) %{_bindir}/vamp-simple-host
%attr(755,root,root) %{_libdir}/libvamp-hostsdk.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvamp-hostsdk.so.3
%attr(755,root,root) %{_libdir}/libvamp-sdk.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvamp-sdk.so.2
%dir %{vampplugindir}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vamp-rdf-template-generator
%attr(755,root,root) %{_libdir}/libvamp-hostsdk.so
%attr(755,root,root) %{_libdir}/libvamp-sdk.so
%{_includedir}/vamp
%{_includedir}/vamp-hostsdk
%{_includedir}/vamp-sdk
%{_pkgconfigdir}/vamp.pc
%{_pkgconfigdir}/vamp-hostsdk.pc
%{_pkgconfigdir}/vamp-sdk.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvamp-hostsdk.a
%{_libdir}/libvamp-sdk.a

%files plugins-example
%defattr(644,root,root,755)
%attr(755,root,root) %{vampplugindir}/vamp-example-plugins.so
%{vampplugindir}/vamp-example-plugins.cat
%{vampplugindir}/vamp-example-plugins.n3
