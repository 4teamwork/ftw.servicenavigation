from ftw.upgrade import UpgradeStep


class AddCustomBrowserLayer(UpgradeStep):
    """Add custom browser layer.
    """

    def __call__(self):
        self.install_upgrade_profile()
