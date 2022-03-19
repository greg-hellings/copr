# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/vmware/vic
%global goipath         github.com/vmware/vic
Version:                1.5.7

%gometa

%global common_description %{expand:
VSphere Integrated Containers Engine is a container runtime for vSphere.}

%global golicenses      LICENSE doc/bundle/NOTICE
%global godocs          doc CONTRIBUTING.md OWNERS.md README.md\\\
                        infra/machines/devbox/README.md\\\
                        infra/scripts/README.md infra/util/vendor-manifest-\\\
                        parser/README.md infra/dlv/README.md\\\
                        infra/integration-image/scripts/README.md\\\
                        isos/base/repos/README.md\\\
                        lib/migration/plugins/plugins.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        VSphere Integrated Containers Engine is a container runtime for vSphere

License:        # FIXME

URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/cenkalti/backoff)
BuildRequires:  golang(github.com/d2g/dhcp4)
BuildRequires:  golang(github.com/d2g/dhcp4client)
BuildRequires:  golang(github.com/dchest/siphash)
BuildRequires:  golang(github.com/docker/distribution)
BuildRequires:  golang(github.com/docker/distribution/digest)
BuildRequires:  golang(github.com/docker/distribution/manifest/schema1)
BuildRequires:  golang(github.com/docker/distribution/manifest/schema2)
BuildRequires:  golang(github.com/docker/distribution/reference)
BuildRequires:  golang(github.com/docker/docker/api/errors)
BuildRequires:  golang(github.com/docker/docker/api/server)
BuildRequires:  golang(github.com/docker/docker/api/server/middleware)
BuildRequires:  golang(github.com/docker/docker/api/server/router)
BuildRequires:  golang(github.com/docker/docker/api/server/router/checkpoint)
BuildRequires:  golang(github.com/docker/docker/api/server/router/container)
BuildRequires:  golang(github.com/docker/docker/api/server/router/image)
BuildRequires:  golang(github.com/docker/docker/api/server/router/network)
BuildRequires:  golang(github.com/docker/docker/api/server/router/plugin)
BuildRequires:  golang(github.com/docker/docker/api/server/router/swarm)
BuildRequires:  golang(github.com/docker/docker/api/server/router/system)
BuildRequires:  golang(github.com/docker/docker/api/server/router/volume)
BuildRequires:  golang(github.com/docker/docker/api/types)
BuildRequires:  golang(github.com/docker/docker/api/types/backend)
BuildRequires:  golang(github.com/docker/docker/api/types/container)
BuildRequires:  golang(github.com/docker/docker/api/types/events)
BuildRequires:  golang(github.com/docker/docker/api/types/filters)
BuildRequires:  golang(github.com/docker/docker/api/types/mount)
BuildRequires:  golang(github.com/docker/docker/api/types/network)
BuildRequires:  golang(github.com/docker/docker/api/types/registry)
BuildRequires:  golang(github.com/docker/docker/api/types/strslice)
BuildRequires:  golang(github.com/docker/docker/api/types/swarm)
BuildRequires:  golang(github.com/docker/docker/api/types/time)
BuildRequires:  golang(github.com/docker/docker/builder/dockerfile)
BuildRequires:  golang(github.com/docker/docker/daemon/cluster)
BuildRequires:  golang(github.com/docker/docker/daemon/cluster/provider)
BuildRequires:  golang(github.com/docker/docker/daemon/events)
BuildRequires:  golang(github.com/docker/docker/distribution/xfer)
BuildRequires:  golang(github.com/docker/docker/image)
BuildRequires:  golang(github.com/docker/docker/layer)
BuildRequires:  golang(github.com/docker/docker/opts)
BuildRequires:  golang(github.com/docker/docker/pkg/archive)
BuildRequires:  golang(github.com/docker/docker/pkg/ioutils)
BuildRequires:  golang(github.com/docker/docker/pkg/listeners)
BuildRequires:  golang(github.com/docker/docker/pkg/mount)
BuildRequires:  golang(github.com/docker/docker/pkg/namesgenerator)
BuildRequires:  golang(github.com/docker/docker/pkg/platform)
BuildRequires:  golang(github.com/docker/docker/pkg/progress)
BuildRequires:  golang(github.com/docker/docker/pkg/pubsub)
BuildRequires:  golang(github.com/docker/docker/pkg/signal)
BuildRequires:  golang(github.com/docker/docker/pkg/stdcopy)
BuildRequires:  golang(github.com/docker/docker/pkg/streamformatter)
BuildRequires:  golang(github.com/docker/docker/pkg/stringid)
BuildRequires:  golang(github.com/docker/docker/pkg/stringutils)
BuildRequires:  golang(github.com/docker/docker/pkg/system)
BuildRequires:  golang(github.com/docker/docker/pkg/term)
BuildRequires:  golang(github.com/docker/docker/pkg/truncindex)
BuildRequires:  golang(github.com/docker/docker/plugin)
BuildRequires:  golang(github.com/docker/docker/reference)
BuildRequires:  golang(github.com/docker/docker/registry)
BuildRequires:  golang(github.com/docker/docker/runconfig)
BuildRequires:  golang(github.com/docker/docker/utils)
BuildRequires:  golang(github.com/docker/go-connections/nat)
BuildRequires:  golang(github.com/docker/go-connections/tlsconfig)
BuildRequires:  golang(github.com/docker/go-units)
BuildRequires:  golang(github.com/docker/libnetwork)
BuildRequires:  golang(github.com/docker/libnetwork/cluster)
BuildRequires:  golang(github.com/docker/libnetwork/iptables)
BuildRequires:  golang(github.com/docker/libnetwork/networkdb)
BuildRequires:  golang(github.com/docker/libnetwork/portallocator)
BuildRequires:  golang(github.com/docker/libnetwork/types)
BuildRequires:  golang(github.com/docker/libtrust)
BuildRequires:  golang(github.com/docker/swarmkit/agent/exec)
BuildRequires:  golang(github.com/go-openapi/errors)
BuildRequires:  golang(github.com/go-openapi/loads)
BuildRequires:  golang(github.com/go-openapi/runtime)
BuildRequires:  golang(github.com/go-openapi/runtime/client)
BuildRequires:  golang(github.com/go-openapi/runtime/middleware)
BuildRequires:  golang(github.com/go-openapi/strfmt)
BuildRequires:  golang(github.com/go-openapi/swag)
BuildRequires:  golang(github.com/golang/groupcache/lru)
BuildRequires:  golang(github.com/google/go-github/github)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/gorilla/context)
BuildRequires:  golang(github.com/gorilla/securecookie)
BuildRequires:  golang(github.com/gorilla/sessions)
BuildRequires:  golang(github.com/hpcloud/tail)
BuildRequires:  golang(github.com/jessevdk/go-flags)
BuildRequires:  golang(github.com/kr/pty)
BuildRequires:  golang(github.com/matryer/resync)
BuildRequires:  golang(github.com/mdlayher/arp)
BuildRequires:  golang(github.com/mdlayher/ethernet)
BuildRequires:  golang(github.com/miekg/dns)
BuildRequires:  golang(github.com/mitchellh/mapstructure)
BuildRequires:  golang(github.com/nlopes/slack)
BuildRequires:  golang(github.com/opencontainers/runc/libcontainer/user)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/pkg/profile)
BuildRequires:  golang(github.com/rs/cors)
BuildRequires:  golang(github.com/ryanuber/go-glob)
BuildRequires:  golang(github.com/sethgrid/multibar)
BuildRequires:  golang(github.com/Sirupsen/logrus)
BuildRequires:  golang(github.com/stretchr/testify/mock)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/tchap/go-patricia/patricia)
BuildRequires:  golang(github.com/tylerb/graceful)
BuildRequires:  golang(github.com/vishvananda/netlink)
BuildRequires:  golang(github.com/vmware/go-nfs-client/nfs)
BuildRequires:  golang(github.com/vmware/go-nfs-client/nfs/rpc)
BuildRequires:  golang(github.com/vmware/govmomi)
BuildRequires:  golang(github.com/vmware/govmomi/event)
BuildRequires:  golang(github.com/vmware/govmomi/find)
BuildRequires:  golang(github.com/vmware/govmomi/govc/host/esxcli)
BuildRequires:  golang(github.com/vmware/govmomi/guest)
BuildRequires:  golang(github.com/vmware/govmomi/guest/toolbox)
BuildRequires:  golang(github.com/vmware/govmomi/license)
BuildRequires:  golang(github.com/vmware/govmomi/list)
BuildRequires:  golang(github.com/vmware/govmomi/object)
BuildRequires:  golang(github.com/vmware/govmomi/performance)
BuildRequires:  golang(github.com/vmware/govmomi/property)
BuildRequires:  golang(github.com/vmware/govmomi/session)
BuildRequires:  golang(github.com/vmware/govmomi/simulator)
BuildRequires:  golang(github.com/vmware/govmomi/task)
BuildRequires:  golang(github.com/vmware/govmomi/toolbox)
BuildRequires:  golang(github.com/vmware/govmomi/toolbox/hgfs)
BuildRequires:  golang(github.com/vmware/govmomi/toolbox/vix)
BuildRequires:  golang(github.com/vmware/govmomi/view)
BuildRequires:  golang(github.com/vmware/govmomi/vim25)
BuildRequires:  golang(github.com/vmware/govmomi/vim25/methods)
BuildRequires:  golang(github.com/vmware/govmomi/vim25/mo)
BuildRequires:  golang(github.com/vmware/govmomi/vim25/progress)
BuildRequires:  golang(github.com/vmware/govmomi/vim25/soap)
BuildRequires:  golang(github.com/vmware/govmomi/vim25/types)
BuildRequires:  golang(github.com/vmware/vmw-guestinfo/rpcout)
BuildRequires:  golang(github.com/vmware/vmw-guestinfo/rpcvmx)
BuildRequires:  golang(github.com/vmware/vmw-guestinfo/vmcheck)
BuildRequires:  golang(golang.org/x/crypto/nacl/secretbox)
BuildRequires:  golang(golang.org/x/crypto/ssh)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(golang.org/x/net/context/ctxhttp)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(golang.org/x/sync/singleflight)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(golang.org/x/text/language)
BuildRequires:  golang(golang.org/x/text/message)
BuildRequires:  golang(gopkg.in/urfave/cli.v1)
BuildRequires:  golang(parser)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/vmware/govmomi/simulator/esx)
BuildRequires:  golang(golang.org/x/crypto/ssh/testdata)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
for cmd in lib/portlayer/exec2/remote/server infra/util/vendor-manifest-parser/tool; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE doc/bundle/NOTICE
%doc doc CONTRIBUTING.md OWNERS.md README.md infra/machines/devbox/README.md
%doc infra/scripts/README.md infra/util/vendor-manifest-parser/README.md
%doc infra/dlv/README.md infra/integration-image/scripts/README.md
%doc isos/base/repos/README.md lib/migration/plugins/plugins.md
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Oct 06 2021 Gregory Hellings <greg.hellings@gmail.com> - 1.5.8-rc1-1%{?dist}
- Initial package
