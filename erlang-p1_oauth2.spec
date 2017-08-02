%global srcname p1_oauth2
# Erlang packages do not provide debug subpackages.
%global debug_package %{nil}


Name:       erlang-%{srcname}
Version:    0.6.1
Release:    %mkrel 1

Group:      Development/Erlang

License:    MIT
Summary:    An Oauth2 implementation for Erlang
URL:        https://github.com/processone/%{srcname}
Source0:    https://github.com/processone/%{srcname}/archive/%{version}.tar.gz

BuildRequires: erlang-meck
BuildRequires: erlang-proper
BuildRequires: erlang-rebar


%description
This library is designed to simplify the implementation of the server side of
OAuth2. It is a fork of erlang-oauth2 by processone, and is needed by ejabberd.


%prep
%autosetup -n %{srcname}-%{version}


%build
%{rebar_compile}


%check
%{rebar_eunit}


%install
%{erlang_install}


%files
%license LICENSE
%doc README.md
%{erlang_appdir}



%changelog
* Thu Nov 17 2016 neoclust <neoclust> 0.6.1-1.mga6
+ Revision: 1068049
- imported package erlang-p1_oauth2

