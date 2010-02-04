# TODO:
# - create more subpackages? (vamp-sdk, vamp-hostsdk)
# - unpackaged programs
#
%define	vampplugindir	%{_libdir}/vamp

%define		_srcname	vamp-plugin-sdk
Summary:	vamp - API for audio analysis and feature extraction plugins
Summary(pl.UTF-8):	vamp - API dla wtyczek analizy i wydobywania cech dźwięku
Name:		vamp
Version:	2.1
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://dl.sourceforge.net/vamp/%{_srcname}-%{version}.tar.gz
# Source0-md5:	13252077a73987dae72a9174e529b6b9
Patch0:		gcc4.patch
URL:		http://www.vamp-plugins.org/
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%setup -q -n %{_srcname}-%{version}
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_libdir}/libvamp-hostsdk.*.*.*
%attr(755,root,root) %{_libdir}/libvamp-sdk.*.*.*
%attr(755,root,root) %ghost %attr(755,root,root) %{_libdir}/libvamp-hostsdk.so.3
%attr(755,root,root) %ghost %attr(755,root,root) %{_libdir}/libvamp-sdk.so.2
%dir %{vampplugindir}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvamp-hostsdk.so
%attr(755,root,root) %{_libdir}/libvamp-sdk.so
%{_libdir}/libvamp-hostsdk.la
%{_libdir}/libvamp-sdk.la
%{_includedir}/vamp
%{_includedir}/vamp-hostsdk
%{_includedir}/vamp-sdk
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvamp-hostsdk.a
%{_libdir}/libvamp-sdk.a

%files plugins-example
%defattr(644,root,root,755)
%attr(755,root,root) %{vampplugindir}/vamp-example-plugins.cat
%attr(755,root,root) %{vampplugindir}/vamp-example-plugins.so
