# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate virtio-bindings

Name:           rust-virtio-bindings
Version:        0.2.1
Release:        %autorelease
Summary:        Rust FFI bindings to virtio generated using bindgen

License:        BSD-3-Clause OR Apache-2.0
URL:            https://crates.io/crates/virtio-bindings
Source0:        %{crates_source}
Source1:        https://raw.githubusercontent.com/rust-vmm/vm-virtio/main/LICENSE-APACHE
Source2:        https://raw.githubusercontent.com/rust-vmm/vm-virtio/main/LICENSE-BSD
# Initial patched metadata
# * Exclude unneeded files
Patch0:         virtio-bindings-fix-metadata.diff

ExclusiveArch:  x86_64 aarch64 ppc64le
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Rust FFI bindings to virtio generated using bindgen.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-BSD
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/CONTRIBUTING.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+virtio-v4_14_0-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+virtio-v4_14_0-devel %{_description}

This package contains library source intended for building other packages which
use the "virtio-v4_14_0" feature of the "%{crate}" crate.

%files       -n %{name}+virtio-v4_14_0-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+virtio-v5_0_0-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+virtio-v5_0_0-devel %{_description}

This package contains library source intended for building other packages which
use the "virtio-v5_0_0" feature of the "%{crate}" crate.

%files       -n %{name}+virtio-v5_0_0-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep
cp %{SOURCE1} .
cp %{SOURCE2} .

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
%autochangelog
