%define	_srcname	vamp-plugin-sdk
Summary:	vamp provides API for audio analysis and feature extraction plugins
Name:		vamp
Version:	1.0
Release:	0.2
License:	BSD-like
Group:		Applications
Source0:	http://dl.sourceforge.net/sv1/%{_srcname}-%{version}.tar.gz
# Source0-md5:	5c63eaa2fc6d5c871b76da937b8e0b2c
Patch0:		%{name}-install.patch
URL:		http://www.vamp-plugins.org/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vamp is an audio processing plugin system for plugins that extract
descriptive information from audio data — typically referred to as
audio analysis plugins or audio feature extraction plugins.

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

%prep
%setup -q -n %{_srcname}-%{version}
%patch0 -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%ghost %attr(755,root,root) %{_libdir}/lib*.so.?

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
