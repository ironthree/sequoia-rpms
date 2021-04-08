# Not generated by rust2rpm 16
# https://pagure.io/fedora-rust/rust2rpm/issue/125
%bcond_without check
%global __cargo_skip_build 0

%global crate sequoia-octopus-librnp

%global tb_plugindir %{_libdir}/thunderbird
%global __provides_exclude_from ^%{tb_plugindir}/.*\\.so$

Name:           rust-%{crate}
Version:        1.0.1
Release:        1%{?dist}
Summary:        Reimplementation of RNP's interface using Sequoia

# Upstream license specification: GPL-2.0-or-later
License:        GPLv2+
URL:            https://crates.io/crates/sequoia-octopus-librnp
Source:         %{crates_source}
# Initial patched metadata
# * exclude files only useful for upstream development
# * do not use bundled sqlite in rusqlite
Patch:         sequoia-octopus-librnp-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
# exclude architectures where thunderbird is not available
ExcludeArch:    %{arm} s390x

BuildRequires:  rust-packaging

%global _description %{expand:
Reimplementation of RNP's interface using Sequoia for use with
Thunderbird.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# 0BSD or MIT or ASL 2.0
# ASL 2.0
# ASL 2.0 or Boost
# ASL 2.0 or MIT
# BSD
# CC0
# GPLv2+
# LGPLv3 or GPLv2 or GPLv3
# LGPLv3+
# MIT
# MIT or ASL 2.0
# MIT or ASL 2.0 or zlib
# MIT or LGPLv3+
# MIT or zlib or ASL 2.0
# Unlicense or MIT
# zlib or ASL 2.0 or MIT
License:        GPLv2+ and ASL 2.0 and BSD and CC0 and LGPLv3+ and MIT

Requires:       thunderbird
Provides:       thunderbird-librnp

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE.txt
%doc README.md
%{tb_plugindir}/librnp.so

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
mkdir -p %{buildroot}/%{tb_plugindir}
cp -pav target/release/libsequoia_octopus_librnp.so %{buildroot}/%{tb_plugindir}/librnp.so

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Apr 08 2021 Fabio Valentini <decathorpe@gmail.com> - 1.0.1-1
- Initial package