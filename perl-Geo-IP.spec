#
# Conditional build:
# _without_tests - do not perform "make test"
#
# ToDo:
# - make the package build even with tests
# - summary / descriptions
%include	/usr/lib/rpm/macros.perl
%define	pdir	Geo
%define	pnam	IP
Summary:	-
Summary(pl):	-
Name:		perl-%{pdir}-%{pnam}
Version:	1.15
Release:	0.1
License:	GPL	
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
# Don't use pipes here: they generally don't work. Apply a patch.
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	LIBS="-L/usr/lib" \
	INC='-I/usr/include'
%{__make}
# if module isn't noarch, use:
# %{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
# use macros:
#%%{perl_vendorlib}/...
%{perl_vendorarch}/*
%{_mandir}/man3/*
