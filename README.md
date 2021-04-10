Work-in-Progress RPM Packages of Sequoia PGP for Fedora
=======================================================

This repository contains RPM spec files and patches for the [sequoia-openpgp]
crate, the [sequoia-octopus-librnp] extension for thunderbird, and all their
dependencies that are not yet available from the official Fedora repositories.

[sequoia-openpgp]: https://crates.io/crates/sequoia-openpgp
[sequoia-octopus-librnp]: https://gitlab.com/sequoia-pgp/sequoia-octopus-librnp

Package Review Tickets
----------------------

| package                           | ticket link       |
| --------------------------------- | ----------------- |
| rust-ascii-canvas                 | [RHBZ#1948128]    |
| rust-buffered-reader              | N/A |
| rust-capnp                        | N/A |
| rust-capnp-futures                | N/A |
| rust-capnp-rpc                    | N/A |
| rust-configparser                 | N/A |
| rust-dyn-clone                    | N/A |
| rust-ena                          | N/A |
| rust-fallible-streaming-iterator  | N/A |
| rust-hashlink                     | N/A |
| rust-lalrpop                      | N/A |
| rust-lalrpop-util                 | N/A |
| rust-memsec                       | N/A |
| rust-nettle                       | N/A |
| rust-nettle-sys                   | N/A |
| rust-rusqlite                     | N/A |
| rust-sequoia-autocrypt            | N/A |
| rust-sequoia-ipc                  | N/A |
| rust-sequoia-keyring-linter       | N/A |
| rust-sequoia-net                  | N/A |
| rust-sequoia-octopus-librnp       | N/A |
| rust-sequpoa-openpgp              | N/A |
| rust-sequoia-sop                  | N/A |
| rust-sequoia-sq                   | N/A |
| rust-sequoia-sqv                  | N/A |
| rust-sha1collisiondetection       | N/A |
| rust-zbase32                      | N/A |

[RHBZ#1948128]: https://bugzilla.redhat.com/show_bug.cgi?id=1948128

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

