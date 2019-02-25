import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_installed_packages(host):
    pkg_list = [
        'libselinux-python',
        'libsemanage-python',
        'policycoreutils-python']

    for package_name in pkg_list:
        assert host.package(package_name).is_installed
