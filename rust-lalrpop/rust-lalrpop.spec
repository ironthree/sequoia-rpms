# Generated by rust2rpm 16
%bcond_without check

%global crate lalrpop

Name:           rust-%{crate}
Version:        0.19.5
Release:        1%{?dist}
Summary:        Convenient LR(1) parser generator

# Upstream license specification: Apache-2.0/MIT
# https://github.com/lalrpop/lalrpop/issues/600
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/lalrpop
Source:         %{crates_source}
# Initial patched metadata
# * bump term from 0.5 to 0.6 to match ascii-canvas in Fedora,
#   not upstreamable until ascii-canvas 2.1.0 is published
Patch0:         lalrpop-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Convenient LR(1) parser generator.}

%description %{_description}

%if ! %{__cargo_skip_build}
%package     -n %{crate}
Summary:        %{summary}
# ASL 2.0 or MIT
# CC0
# MIT
# MIT or ASL 2.0
# Unlicense or MIT
License:        MIT and CC0

%description -n %{crate} %{_description}

%files       -n %{crate}
%{_bindir}/lalrpop
%endif

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+lexer-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+lexer-devel %{_description}

This package contains library source intended for building other packages
which use "lexer" feature of "%{crate}" crate.

%files       -n %{name}+lexer-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+pico-args-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pico-args-devel %{_description}

This package contains library source intended for building other packages
which use "pico-args" feature of "%{crate}" crate.

%files       -n %{name}+pico-args-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+test-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+test-devel %{_description}

This package contains library source intended for building other packages
which use "test" feature of "%{crate}" crate.

%files       -n %{name}+test-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Apr 08 2021 Fabio Valentini <decathorpe@gmail.com> - 0.19.5-1
- Initial package
