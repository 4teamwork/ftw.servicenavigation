from Products.CMFPlone.utils import getFSVersionTuple
from ftw.upgrade import UpgradeStep


class Plone5Upgrade(UpgradeStep):
    """Plone5 upgrade.
    """

    def __call__(self):
        # replace plone.formwidget.contenttree using ftw.referencewidget
        self.ensure_profile_installed('profile-ftw.referencewidget:default')

        # if Plone 5 additionally upgrade profile contained in the upgrade step.
        if getFSVersionTuple() > (5, ):
            self.install_upgrade_profile()
