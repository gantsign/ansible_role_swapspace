import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_swapspace(host):
    cmd = host.run('. /etc/profile && swapspace --version')
    assert cmd.rc == 0
