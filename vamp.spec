# TODO:
# - create more subpackages? (vamp-sdk, vamp-hostsdk)
#
%define	vampplugindir	%{_libdir}/vamp

Summary:	vamp - API for audio analysis and feature extraction plugins
Summary(pl.UTF-8):	vamp - API dla wtyczek analizy i wydobywania cech dźwięku
Name:		vamp
Version:	2.1
Release:	0.1
License:	BSD-like
Group:		Libraries
%define		_srcname	vamp-plugin-sdk
Source0:	http://dl.sourceforge.net/vamp/%{_srcname}-%{version}.tar.gz
# Source0-md5:	13252077a73987dae72a9174e529b6b9
Patch0:		%{name}-install.patch
Patch1:		%{name}-optflags.patch
Patch2:		%{name}-link.patch
URL:		http://www.vamp-plugins.org/
BuildRequires:	libstdc++-devel
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
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	OPTFLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	LIB=%{_lib} \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{vampplugindir}
install examples/*.so $RPM_BUILD_ROOT%{vampplugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%ghost %attr(755,root,root) %{_libdir}/lib*.so.?
%dir %{vampplugindir}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/vamp
%{_includedir}/vamp-sdk
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files plugins-example
%defattr(644,root,root,755)
%attr(755,root,root) %{vampplugindir}/*so
