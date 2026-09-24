%global debug_package %{nil}

Name:           cache-api
Version:        1.0.0
Release:        1%{?dist}
Summary:        Flask caching proxy for Backend API

License:        Proprietary
Source0:        %{name}-%{version}.tar.gz

Requires:       python3

%description
Flask proxy service that caches Backend API responses in Redis.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/local/lib/cache-api
mkdir -p %{buildroot}/etc/cache-api
mkdir -p %{buildroot}/usr/lib/systemd/system

install -m 0644 cache-api.py \
    %{buildroot}/usr/local/lib/cache-api/cache-api.py

cp -a vendor \
    %{buildroot}/usr/local/lib/cache-api/

rm -rf %{buildroot}/usr/local/lib/cache-api/vendor/bin

find %{buildroot}/usr/local/lib/cache-api/vendor \
    -type f -name "*.py" -exec chmod 0644 {} \;

install -m 0644 config.yaml \
    %{buildroot}/etc/cache-api/config.yaml

install -m 0644 cache-api.service \
    %{buildroot}/usr/lib/systemd/system/cache-api.service

%post
/bin/systemctl daemon-reload >/dev/null 2>&1 || true

%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || true

%files
%dir /usr/local/lib/cache-api
/usr/local/lib/cache-api/cache-api.py
/usr/local/lib/cache-api/vendor

%dir /etc/cache-api
%config(noreplace) /etc/cache-api/config.yaml

/usr/lib/systemd/system/cache-api.service

%changelog
* Mon Sep 21 2026 Student <student@localhost> - 1.0.0-1
- Initial package
