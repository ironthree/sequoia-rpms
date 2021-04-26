RPM Packages of Sequoia PGP for Fedora
======================================

This repository **used** to contain RPM spec files and patches for:

- the [sequoia-openpgp] crate,
- the [sequoia-octopus-librnp] extension for thunderbird,
- all their dependencies that were not available from the official Fedora
repositories, and
- all available sequoia command line tools.

[sequoia-openpgp]: https://crates.io/crates/sequoia-openpgp
[sequoia-octopus-librnp]: https://gitlab.com/sequoia-pgp/sequoia-octopus-librnp

All packages are now available from official Fedora repositories, starting with
Fedora 34:

- <https://bodhi.fedoraproject.org/updates/FEDORA-2021-c1fecf829f>
- <https://bodhi.fedoraproject.org/updates/FEDORA-2021-c9eb437a0c>
- <https://bodhi.fedoraproject.org/updates/FEDORA-2021-9916b8aab7>
- <https://bodhi.fedoraproject.org/updates/FEDORA-2021-68d7387594>

Until either the thunderbird package in Fedora is [adapted] to support a
different librnp backend or the [upstream] project adds support for switching
the backend, using the "Octopus" backend involves manually copying the file
in place of the "official" binary (**beware**: any future thunderbird package
update will undo that).

[adapted]: https://src.fedoraproject.org/rpms/thunderbird/pull-request/11
[upstream]: https://bugzilla.mozilla.org/show_bug.cgi?id=1698540

Until that is the case, I will continue to provide thunderbird builds with
the support for switching librnp backends in [copr].

[copr]: https://copr.fedorainfracloud.org/coprs/decathorpe/sequoia/monitor/

License
-------

All published downstream code (.spec and .diff / .patch) is made available
under the terms of the default software license for Fedora packages according
to the Fedora Project Contributor Agreement / "FPCA" (the **MIT** license) [¹],
since all RPM packages maintained in this repository will eventually become
official Fedora packages.

[¹]: https://fedoraproject.org/wiki/Legal:Fedora_Project_Contributor_Agreement

