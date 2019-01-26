%define uname  %{kernel_version}
%define module_dir updates

Summary: Driver for hello-world
Name: hello-world
Version: 1.0
Release: %{?release}%{!?release:1}
License: GPL
Source: %{name}-%{version}.tar.gz

BuildRequires: kernel-devel
Provides: vendor-driver
Requires: kernel-uname-r = %{kernel_version}
Requires(post): /usr/sbin/depmod
Requires(postun): /usr/sbin/depmod

%description
hello-world Linux Device Driver source.

%prep
%setup -q -n %{name}-%{version}

%build
%{__make} -C /lib/modules/%{uname}/build M=$(pwd) modules

%install
%{__make} -C /lib/modules/%{uname}/build M=$(pwd) INSTALL_MOD_PATH=%{buildroot} INSTALL_MOD_DIR=%{module_dir} DEPMOD=/bin/true modules_install

# remove extra files modules_install copies in
rm -f %{buildroot}/lib/modules/%{uname}/modules.*

# mark modules executable so that strip-to-file can strip them
find %{buildroot}/lib/modules/%{uname} -name "*.ko" -type f | xargs chmod u+x

%post
/sbin/depmod %{kernel_version}
%{regenerate_initrd_post}

%postun
/sbin/depmod %{kernel_version}
%{regenerate_initrd_postun}

%posttrans
%{regenerate_initrd_posttrans}

%files
%defattr(-,root,root,-)
/lib/modules/%{uname}/*/*.ko
%doc

%changelog
* Sat Jan 26 2019 Rushikesh Jadhav <rushikesh7@gmail.com> - 1.0
- Added example driver hello-world-1.0
