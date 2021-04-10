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
| rust-capnp-futures                | N/A               | capnp-rpc                     |
| rust-capnp-rpc                    | N/A               | sequoia-ipc                   |
| rust-configparser                 | [RHBZ#1948133]    | sequoia-octopus-librnp        |
| rust-dyn-clone                    | [RHBZ#1948134]    | sequoia-openpgp               |
| rust-ena                          | N/A               | lalrpop                       |
| rust-fallible-streaming-iterator  | [RHBZ#1948136]    | rusqlite                      |
| rust-hashlink                     | [RHBZ#1948138]    | rusqlite                      |
| rust-lalrpop                      | N/A               | sequoia-openpgp               |
| rust-lalrpop-util                 | [RHBZ#1948140]    | lalrpop                       |
| rust-memsec                       | [RHBZ#1948142]    | sequoia-openpgp               |
| rust-nettle                       | N/A               | sequoia-openpgp               |
| rust-nettle-sys                   | [RHBZ#1948145]    | nettle                        |
| rust-rusqlite                     | N/A               | sequoia-octopus-librnp        |
| rust-sequoia-autocrypt            | N/A               | sequoia-{octopus-librnp,sq}   |
| rust-sequoia-ipc                  | N/A               | sequoia-octopus-librnp        |
| rust-sequoia-keyring-linter       | N/A               | N/A                           |
| rust-sequoia-net                  | N/A               | sequoia-{octopus-librnp,sq}   |
| rust-sequoia-octopus-librnp       | N/A               | N/A                           |
| rust-sequpoa-openpgp              | N/A               | sequoia-*                     |
| rust-sequoia-sop                  | N/A               | N/A                           |
| rust-sequoia-sq                   | N/A               | N/A                           |
| rust-sequoia-sqv                  | N/A               | N/A                           |
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

Pending Package Updates
-----------------------

- pico-args 0.4.0: [RHBZ#1912117]
- rand_distr 0.4.0: [RHBZ#1909357]

[RHBZ#1912117]: https://bugzilla.redhat.com/show_bug.cgi?id=1912117
[RHBZ#1909357]: https://bugzilla.redhat.com/show_bug.cgi?id=1909357

License
-------

All published downstream code (.spec and .diff / .patch) is made available
under the terms of the default software license for Fedora packages according
to the Fedora Project Contributor Agreement / "FPCA" (the **MIT** license) [¹],
since all RPM packages maintained in this repository will eventually become
official Fedora packages.

[¹]: https://fedoraproject.org/wiki/Legal:Fedora_Project_Contributor_Agreement

