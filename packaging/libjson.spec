Name:       libjson
Summary:    json-c library
Version:    0.9.3
License:    TO BE FILLED IN
Release:    0
Group:      Development/Libraries
URL:	    http://oss.metaparadigm.com/json-c
Source: %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
libjson needed by pulseaudio

%package devel
Summary:    libjson devel header
Group:      TO BE FILLED IN
Requires: %{name} = %{version}

%description devel
libjson library.

%prep
%setup -q

%build
%configure 
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%manifest libjson.manifest
%defattr(-,root,root,-)
/usr/lib/*.so.*

%files devel
/usr/lib/pkgconfig/*.pc
/usr/include/json/*.h
/usr/lib/*.so
