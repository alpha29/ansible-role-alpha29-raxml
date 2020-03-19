def test_raxml(host):
    """
    Check raxml version.
    """
    cmd = "raxml -v"
    cmd_result = host.run(cmd)
    assert cmd_result.rc == 0, "'{}' returned status {}.".format(cmd, cmd_result.rc)
    assert "RAxML version 8.2.12" in cmd_result.stdout, f"'{cmd}' returned stdout '{cmd_result.stdout}', stderr '{cmd_result.stderr}'"
