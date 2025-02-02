from homehub_interface.homehubsession import HomeHubSession


def test_guest_auth():
    session = HomeHubSession(timeout=1)
    session.authenticate_guest()
    assert True


def test_admin_auth():
    session = HomeHubSession(timeout=1)
    session.authenticate_admin()
    assert True
