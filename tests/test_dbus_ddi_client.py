import gbulb
from rauc_hawkbit.rauc_dbus_ddi_client import RaucDBUSDDIClient

def test_create(tmpdir):
    d = tmpdir.mkdir("bundles").join("bundle.raucb")

    session = None
    HOST = '127.0.0.1'
    SSL = False
    CA_FILE = None
    TENANT_ID = 'DEFAULT'
    TARGET_NAME = 'test-target'
    AUTH_TOKEN = None
    ATTRIBUTES = {'MAC':'11:22:33:44:55:66'}
    BUNDLE_DL_LOCATION = str(d)
    gbulb.install()
    #loop = asyncio.get_event_loop()
    client = RaucDBUSDDIClient(session, HOST, SSL, TENANT_ID, TARGET_NAME,
                                   AUTH_TOKEN, ATTRIBUTES, BUNDLE_DL_LOCATION,
                                   None)
