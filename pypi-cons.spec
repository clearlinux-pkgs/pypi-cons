#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cons
Version  : 0.4.4
Release  : 1
URL      : https://files.pythonhosted.org/packages/30/b5/5e680fdeb401fab91d779ea02e781bbe54119a8bd9d9540aaf77959deaaf/cons-0.4.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/30/b5/5e680fdeb401fab91d779ea02e781bbe54119a8bd9d9540aaf77959deaaf/cons-0.4.4.tar.gz
Summary  : An implementation of Lisp/Scheme-like cons in Python.
Group    : Development/Tools
License  : LGPL-3.0
Requires: pypi-cons-license = %{version}-%{release}
Requires: pypi-cons-python = %{version}-%{release}
Requires: pypi-cons-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(logical_unification)

%description
# Python `cons`
        
        An implementation of [`cons`][cons] in Python.
        
        ## Usage and Design

%package license
Summary: license components for the pypi-cons package.
Group: Default

%description license
license components for the pypi-cons package.


%package python
Summary: python components for the pypi-cons package.
Group: Default
Requires: pypi-cons-python3 = %{version}-%{release}

%description python
python components for the pypi-cons package.


%package python3
Summary: python3 components for the pypi-cons package.
Group: Default
Requires: python3-core
Provides: pypi(cons)
Requires: pypi(logical_unification)

%description python3
python3 components for the pypi-cons package.


%prep
%setup -q -n cons-0.4.4
cd %{_builddir}/cons-0.4.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640114117
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cons
cp %{_builddir}/cons-0.4.4/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-cons/f45ee1c765646813b442ca58de72e20a64a7ddba
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cons/f45ee1c765646813b442ca58de72e20a64a7ddba

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*