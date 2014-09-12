#
# Conditional build:
%bcond_with	tests	# perform "make test" 
			# (requires working DNS - but may fail anyway, because of some NXDOMAIN)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Geo
%define		pnam	IP
Summary:	Geo::IP - look up country by IP Address
Summary(pl.UTF-8):	Geo::IP - odszukanie kraju po adresie IP
Name:		perl-Geo-IP
Version:	1.40
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Geo/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f2e0ebe860052edf250ae02da81af1a5
URL:		http://search.cpan.org/dist/Geo-IP/
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

%description -l pl.UTF-8
Ten moduł używa bazy danych w postaci pliku. W bazie tej adresy IP są
kluczami, a państwa wartościami. Powinna ona być dokładniejsza niż
sprawdzanie odwrotnego DNS.

Ta biblioteka może być używana do automatycznego wyboru najbliższego
geograficznie mirrora, analizy logów serwera WWW w celu określenia
kraju, z którego pochodzą odwiedzający, do wykrywania oszustw
dotyczących kart kredytowych oraz kontroli eksportu oprogramowania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
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
%attr(755,root,root) %{perl_vendorarch}/auto/Geo/IP/IP.so
%{_mandir}/man3/*
