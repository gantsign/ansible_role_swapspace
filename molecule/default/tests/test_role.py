def test_swapspace(host):
    cmd = host.run('. /etc/profile && swapspace --version')
    assert cmd.rc == 0
