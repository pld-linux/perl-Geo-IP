#
# Conditional build:
%bcond_with	tests	# perform "make test" 
			# (requires working DNS - but may fail anyway, because of some NXDOMAIN)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Geo
%define		pnam	IP
Summary:	Geo::IP - look up country by IP Address
Summary(pl):	Geo::IP - odszukanie kraju po adresie IP
Name:		perl-Geo-IP
Version:	1.23
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	01b924df6c6e0b8b468d3f8df7275160
BuildRequires:	GeoIP-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module uses a file based database. This database simply contains
IP blocks as keys, and countries as values. This database should be
more complete and accurate than reverse DNS lookups.

This module can be used to automatically select the geographically
closest mirror, to analyze your web server logs to determine the
countries of your visitors, for credit card fraud detection, and for
software export controls.

%description -l pl
Ten modu³ u¿ywa bazy danych w postaci pliku. W bazie tej adresy IP s±
kluczami, a pañstwa warto¶ciami. Powinna ona byæ dok³adniejsza ni¿
sprawdzanie odwrotnego DNS.

Ta biblioteka mo¿e byæ u¿ywana do automatycznego wyboru najbli¿szego
geograficznie mirrora, analizy logów serwera WWW w celu okre¶lenia
kraju, z którego pochodz± odwiedzaj±cy, do wykrywania oszustw
dotycz±cych kart kredytowych oraz kontroli eksportu oprogramowania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/Geo
%{perl_vendorarch}/Geo/*.pm
%dir %{perl_vendorarch}/Geo/IP
%{perl_vendorarch}/Geo/IP/*.pm
%dir %{perl_vendorarch}/auto/Geo
%dir %{perl_vendorarch}/auto/Geo/IP
%{perl_vendorarch}/auto/Geo/IP/IP.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Geo/IP/IP.so
%{_mandir}/man3/*
