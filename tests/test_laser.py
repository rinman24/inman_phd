import chamber.laser as laser

class TestLaser(object):
    """Unit testing of laser.py."""

    def test_laser_constructor(self):
        """Check that a laser can be instanciated properly."""
        co2_laser = laser.GaussianBeam()
        assert co2_laser.lam == 10.59e-6
        assert co2_laser.power == 20
        assert co2_laser.radius == 0.9e-3

    def test_laser_constructor_custom(self):
        """Check that a laser can be instanciated with a custom parameters."""
        co2_laser = laser.GaussianBeam(lam=635e-9, power=5e-3, radius=4e-3)
        assert co2_laser.lam == 635e-9
        assert co2_laser.power == 5e-3
        assert co2_laser.radius == 4e-3