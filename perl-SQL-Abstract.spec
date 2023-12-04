#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-SQL-Abstract
Version  : 2.000001
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/M/MS/MSTROUT/SQL-Abstract-2.000001.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MS/MSTROUT/SQL-Abstract-2.000001.tar.gz
Summary  : 'Generate SQL from Perl data structures'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-SQL-Abstract-license = %{version}-%{release}
Requires: perl-SQL-Abstract-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Clone::Choose)
BuildRequires : perl(Data::Dumper::Concise)
BuildRequires : perl(Hash::Merge)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Moo)
BuildRequires : perl(Role::Tiny)
BuildRequires : perl(Sub::Quote)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(Test::Exception)
BuildRequires : perl(Test::Warn)

%description
NAME
SQL::Abstract - Generate SQL from Perl data structures
SYNOPSIS
use SQL::Abstract;

%package dev
Summary: dev components for the perl-SQL-Abstract package.
Group: Development
Provides: perl-SQL-Abstract-devel = %{version}-%{release}
Requires: perl-SQL-Abstract = %{version}-%{release}

%description dev
dev components for the perl-SQL-Abstract package.


%package license
Summary: license components for the perl-SQL-Abstract package.
Group: Default

%description license
license components for the perl-SQL-Abstract package.


%package perl
Summary: perl components for the perl-SQL-Abstract package.
Group: Default
Requires: perl-SQL-Abstract = %{version}-%{release}

%description perl
perl components for the perl-SQL-Abstract package.


%prep
%setup -q -n SQL-Abstract-2.000001
cd %{_builddir}/SQL-Abstract-2.000001

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-SQL-Abstract
cp %{_builddir}/SQL-Abstract-2.000001/LICENSE %{buildroot}/usr/share/package-licenses/perl-SQL-Abstract/4916d9655816ca1e14f8edc60f7869f011ba5238
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DBIx::Class::SQLMaker::Role::SQLA2Passthrough.3
/usr/share/man/man3/DBIx::Class::Storage::Debug::PrettyPrint.3
/usr/share/man/man3/SQL::Abstract.3
/usr/share/man/man3/SQL::Abstract::Plugin::BangOverrides.3
/usr/share/man/man3/SQL::Abstract::Plugin::ExtraClauses.3
/usr/share/man/man3/SQL::Abstract::Reference.3
/usr/share/man/man3/SQL::Abstract::Role::Plugin.3
/usr/share/man/man3/SQL::Abstract::Test.3
/usr/share/man/man3/SQL::Abstract::Tree.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-SQL-Abstract/4916d9655816ca1e14f8edc60f7869f011ba5238

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
