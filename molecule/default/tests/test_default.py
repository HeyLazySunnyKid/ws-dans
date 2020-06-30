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
    f = host.file('/etc/systemd/system/test.service')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_root_service_started(host):
    f = host.file('/var/log/root_test.log')

    assert f.content_string == 'Hello, Root World'

def test_user_configfile(host):
    f = host.file('/root/.config/system/test.service')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_user_service_started(host):
    f = host.file('/var/log/user_test.log')

    assert f.content_string == 'Hello, User World'

def test_user_configfile(host):
    f = host.file('/root/.config/system/user_test.service')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
