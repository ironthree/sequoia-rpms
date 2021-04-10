Work-in-Progress RPM Packages of Sequoia PGP for Fedora
=======================================================

This repository contains RPM spec files and patches for the [sequoia-openpgp]
crate, the [sequoia-octopus-librnp] extension for thunderbird, and all their
dependencies that are not yet available from the official Fedora repositories.

[sequoia-openpgp]: https://crates.io/crates/sequoia-openpgp
[sequoia-octopus-librnp]: https://gitlab.com/sequoia-pgp/sequoia-octopus-librnp

Package Review Tickets
----------------------

| package                           | ticket link       | required by                   |
| --------------------------------- | ----------------- | ----------------------------- |
| rust-ascii-canvas                 | [RHBZ#1948128]    | lalrpop                       |
| rust-buffered-reader              | [RHBZ#1948130]    | sequoia-openpgp               |
| rust-capnp                        | [RHBZ#1948135]    | capnp-futures                 |
| rust-capnp-futures                | [RHBZ#1948147]    | capnp-rpc                     |
| rust-capnp-rpc                    | [RHBZ#1948148]    | sequoia-ipc                   |
| rust-configparser                 | [RHBZ#1948133]    | sequoia-octopus-librnp        |
| rust-dyn-clone                    | [RHBZ#1948134]    | sequoia-openpgp               |
| rust-ena                          | [RHBZ#1948152]    | lalrpop                       |
| rust-fallible-streaming-iterator  | [RHBZ#1948136]    | rusqlite                      |
| rust-hashlink                     | [RHBZ#1948138]    | rusqlite                      |
| rust-lalrpop                      | [RHBZ#1948150]    | sequoia-openpgp               |
| rust-lalrpop-util                 | [RHBZ#1948140]    | lalrpop                       |
| rust-memsec                       | [RHBZ#1948142]    | sequoia-openpgp               |
| rust-nettle                       | [RHBZ#1948151]    | sequoia-openpgp               |
| rust-nettle-sys                   | [RHBZ#1948145]    | nettle                        |
| rust-rusqlite                     | [RHBZ#1948153]    | sequoia-octopus-librnp        |
| rust-sequoia-autocrypt            | [RHBZ#1948156]    | sequoia-{octopus-librnp,sq}   |
| rust-sequoia-ipc                  | [RHBZ#1948157]    | sequoia-octopus-librnp        |
| rust-sequoia-keyring-linter       | [RHBZ#1948165]    | N/A                           |
| rust-sequoia-net                  | [RHBZ#1948158]    | sequoia-{octopus-librnp,sq}   |
| rust-sequoia-octopus-librnp       | [RHBZ#1948159]    | N/A                           |
| rust-sequpoa-openpgp              | [RHBZ#1948154]    | sequoia-*                     |
| rust-sequoia-sop                  | [RHBZ#1948166]    | N/A                           |
| rust-sequoia-sq                   | [RHBZ#1948161]    | N/A                           |
| rust-sequoia-sqv                  | [RHBZ#1948163]    | N/A                           |
| rust-sha1collisiondetection       | [RHBZ#1948144]    | sequoia-openpgp               |
| rust-zbase32                      | [RHBZ#1948143]    | sequoia-net                   |

[RHBZ#1948128]: https://bugzilla.redhat.com/show_bug.cgi?id=1948128
[RHBZ#1948130]: https://bugzilla.redhat.com/show_bug.cgi?id=1948130
[RHBZ#1948135]: https://bugzilla.redhat.com/show_bug.cgi?id=1948135
[RHBZ#1948133]: https://bugzilla.redhat.com/show_bug.cgi?id=1948133
[RHBZ#1948134]: https://bugzilla.redhat.com/show_bug.cgi?id=1948134
[RHBZ#1948136]: https://bugzilla.redhat.com/show_bug.cgi?id=1948136
[RHBZ#1948138]: https://bugzilla.redhat.com/show_bug.cgi?id=1948138
[RHBZ#1948140]: https://bugzilla.redhat.com/show_bug.cgi?id=1948140
[RHBZ#1948142]: https://bugzilla.redhat.com/show_bug.cgi?id=1948142
[RHBZ#1948145]: https://bugzilla.redhat.com/show_bug.cgi?id=1948145
[RHBZ#1948144]: https://bugzilla.redhat.com/show_bug.cgi?id=1948144
[RHBZ#1948143]: https://bugzilla.redhat.com/show_bug.cgi?id=1948143
[RHBZ#1948147]: https://bugzilla.redhat.com/show_bug.cgi?id=1948147
[RHBZ#1948148]: https://bugzilla.redhat.com/show_bug.cgi?id=1948148
[RHBZ#1948150]: https://bugzilla.redhat.com/show_bug.cgi?id=1948150
[RHBZ#1948151]: https://bugzilla.redhat.com/show_bug.cgi?id=1948151
[RHBZ#1948152]: https://bugzilla.redhat.com/show_bug.cgi?id=1948152
[RHBZ#1948153]: https://bugzilla.redhat.com/show_bug.cgi?id=1948153
[RHBZ#1948154]: https://bugzilla.redhat.com/show_bug.cgi?id=1948154
[RHBZ#1948156]: https://bugzilla.redhat.com/show_bug.cgi?id=1948156
[RHBZ#1948157]: https://bugzilla.redhat.com/show_bug.cgi?id=1948157
[RHBZ#1948158]: https://bugzilla.redhat.com/show_bug.cgi?id=1948158
[RHBZ#1948159]: https://bugzilla.redhat.com/show_bug.cgi?id=1948159
[RHBZ#1948161]: https://bugzilla.redhat.com/show_bug.cgi?id=1948161
[RHBZ#1948163]: https://bugzilla.redhat.com/show_bug.cgi?id=1948163
[RHBZ#1948165]: https://bugzilla.redhat.com/show_bug.cgi?id=1948165
[RHBZ#1948166]: https://bugzilla.redhat.com/show_bug.cgi?id=1948166

Pending Package Updates
-----------------------

- pico-args 0.4.0: [RHBZ#1912117]
- rand_distr 0.4.0: [RHBZ#1909357]

[RHBZ#1912117]: https://bugzilla.redhat.com/show_bug.cgi?id=1912117
[RHBZ#1909357]: https://bugzilla.redhat.com/show_bug.cgi?id=1909357

Pending Thunderbird Pull Request
--------------------------------

<https://src.fedoraproject.org/rpms/thunderbird/pull-request/11>

License
-------

All published downstream code (.spec and .diff / .patch) is made available
under the terms of the default software license for Fedora packages according
to the Fedora Project Contributor Agreement / "FPCA" (the **MIT** license) [¹],
since all RPM packages maintained in this repository will eventually become
official Fedora packages.

[¹]: https://fedoraproject.org/wiki/Legal:Fedora_Project_Contributor_Agreement

