import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_root_configfile(host):
    f = host.file('/etc/systemd/system/root_test.service')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_root_service_started(host):
    f = host.file('/var/log/root_test.log')

    assert f.content_string == 'Hello, Root World\n'

def test_user_configfile(host):
    f = host.file('/root/.config/systemd/user/user_test.service')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
