#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kcodecs
Version  : 6.5.0
Release  : 91
URL      : https://download.kde.org/stable/frameworks/6.5/kcodecs-6.5.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.5/kcodecs-6.5.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.5/kcodecs-6.5.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 LGPL-2.0 LGPL-2.1 MIT MPL-1.1
Requires: kcodecs-data = %{version}-%{release}
Requires: kcodecs-lib = %{version}-%{release}
Requires: kcodecs-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules gperf
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KCodecs
String encoding library
## Introduction
KCodecs provide a collection of methods to manipulate strings using various
encodings.

%package data
Summary: data components for the kcodecs package.
Group: Data

%description data
data components for the kcodecs package.


%package dev
Summary: dev components for the kcodecs package.
Group: Development
Requires: kcodecs-lib = %{version}-%{release}
Requires: kcodecs-data = %{version}-%{release}
Provides: kcodecs-devel = %{version}-%{release}
Requires: kcodecs = %{version}-%{release}

%description dev
dev components for the kcodecs package.


%package lib
Summary: lib components for the kcodecs package.
Group: Libraries
Requires: kcodecs-data = %{version}-%{release}
Requires: kcodecs-license = %{version}-%{release}

%description lib
lib components for the kcodecs package.


%package license
Summary: license components for the kcodecs package.
Group: Default

%description license
license components for the kcodecs package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kcodecs-6.5.0
cd %{_builddir}/kcodecs-6.5.0
pushd ..
cp -a kcodecs-6.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1723213802
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1723213802
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcodecs
cp %{_builddir}/kcodecs-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kcodecs/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kcodecs-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kcodecs/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kcodecs-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcodecs/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kcodecs-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kcodecs/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kcodecs-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcodecs/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kcodecs-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kcodecs/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kcodecs-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kcodecs/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3 || :
cp %{_builddir}/kcodecs-%{version}/LICENSES/MPL-1.1.txt %{buildroot}/usr/share/package-licenses/kcodecs/b40d491259fdd8faefb41c11fda11d9be6c0bdb1 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/locale/af/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/as/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/ast/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/az/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/be/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/bn/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/br/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/crh/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/csb/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/cy/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/da/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/de/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/el/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/es/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/et/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/fa/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/fy/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/gu/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/ha/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/he/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/hne/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/hy/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/id/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/is/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/it/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/km/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/kn/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/ku/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/lb/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/mai/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/mk/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/ms/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/ne/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/oc/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/or/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/ps/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/se/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/si/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/sq/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/ta/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/te/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/th/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/tt/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/uz/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/wa/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/xh/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/zh_HK/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kcodecs6_qt.qm
/usr/share/qlogging-categories6/kcodecs.categories
/usr/share/qlogging-categories6/kcodecs.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KCodecs/KCharsets
/usr/include/KF6/KCodecs/KCodecs
/usr/include/KF6/KCodecs/KEmailAddress
/usr/include/KF6/KCodecs/KEncodingProber
/usr/include/KF6/KCodecs/kcharsets.h
/usr/include/KF6/KCodecs/kcodecs.h
/usr/include/KF6/KCodecs/kcodecs_export.h
/usr/include/KF6/KCodecs/kcodecs_version.h
/usr/include/KF6/KCodecs/kemailaddress.h
/usr/include/KF6/KCodecs/kencodingprober.h
/usr/lib64/cmake/KF6Codecs/KF6CodecsConfig.cmake
/usr/lib64/cmake/KF6Codecs/KF6CodecsConfigVersion.cmake
/usr/lib64/cmake/KF6Codecs/KF6CodecsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6Codecs/KF6CodecsTargets.cmake
/usr/lib64/libKF6Codecs.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6Codecs.so.6.5.0
/usr/lib64/libKF6Codecs.so.6
/usr/lib64/libKF6Codecs.so.6.5.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcodecs/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kcodecs/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kcodecs/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kcodecs/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kcodecs/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/kcodecs/b40d491259fdd8faefb41c11fda11d9be6c0bdb1
/usr/share/package-licenses/kcodecs/e712eadfab0d2357c0f50f599ef35ee0d87534cb
