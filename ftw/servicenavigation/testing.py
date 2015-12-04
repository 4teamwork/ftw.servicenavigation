from ftw.builder.testing import BUILDER_LAYER
from ftw.builder.testing import functional_session_factory
from ftw.builder.testing import set_builder_session_factory
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from zope.configuration import xmlconfig


class ServicenavigationLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE, BUILDER_LAYER, )

    def setUpZope(self, app, configurationContext):
        xmlconfig.string(
            '<configure xmlns="http://namespaces.zope.org/zope">'
            '  <include package="z3c.autoinclude" file="meta.zcml" />'
            '  <includePlugins package="plone" />'
            '  <includePluginsOverrides package="plone" />'
            '</configure>',
            context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ftw.servicenavigation:default')

    def tearDownZope(self, app):
        super(ServicenavigationLayer, self).tearDownZope(app)


SERVICENAVIGATION_FIXTURE = ServicenavigationLayer()
SERVICENAVIGATION_FUNCTIONAL = FunctionalTesting(
    bases=(
        SERVICENAVIGATION_FIXTURE,
        set_builder_session_factory(functional_session_factory),
    ),
    name='ftw.servicenavigation:functional',
)
