from nose.tools import assert_equals, with_setup
from dronekit.sitl import SITL

sitl = SITL('copter', '3.3-rc5')
sitl_args = ['-I0', '-S', '--model', 'quad', '--home=-35.363261,149.165230,584,353']

def setup_sitl():
    sitl.launch(sitl_args, await_ready=True, restart=True)

def teardown_sitl():
    sitl.stop()

def with_sitl(fn):
    @with_setup(setup_sitl, teardown_sitl)
    def test(*args, **kargs):
        return fn(*args, **kargs)
    return test