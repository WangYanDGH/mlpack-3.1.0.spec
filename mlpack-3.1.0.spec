Name:           mlpack
Version:        3.1.0
Release:        2
Summary:        mlpack is an intuitive, fast, and flexible header-only C++ machine learning library with bindings to other languages
License:        3-clause BSD
URL:            https://www.mlpack.org
Source:         %{name}-%{version}.tar.gz

%description
mlpack is an intuitive, fast, and flexible header-only C++ machine learning library with bindings to other languages. It is meant to be a machine learning analog to LAPACK, and aims to implement a wide array of machine learning methods and functions as a "swiss army knife" for machine learning researchers

%prep
%autosetup


%build
make

%install
%make_install PREFIX=%{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_unitdir}
make install -pDm640 DESTDIR=%{buildroot} 

%files
%{_bindir}/%{name}-*


%changelog
* Mon Jan 15 2024  -3.1.0
- Add service

* Mon Jan 15 2024  -3.1.0
- Package init
