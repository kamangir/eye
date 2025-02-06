from abcli.tests.test_env import test_abcli_env
from blue_objects.tests.test_env import test_blue_objects_env

from blue_sbc import env


def test_required_env():
    test_abcli_env()
    test_blue_objects_env()


def test_blue_plugin_env():
    assert isinstance(env.BLUE_SBC_APPLICATION, str)

    assert isinstance(env.BLUE_SBC_CAMERA_HI_RES, bool)
    assert isinstance(env.BLUE_SBC_CAMERA_WIDTH, int)
    assert isinstance(env.BLUE_SBC_CAMERA_HEIGHT, int)
    assert isinstance(env.BLUE_SBC_CAMERA_ROTATION, int)

    assert isinstance(env.BLUE_SBC_DISPLAY_FULLSCREEN, bool)

    assert env.BLUE_SBC_HARDWARE_KIND

    assert isinstance(env.BLUE_SBC_SESSION_PLUGIN, str)

    assert isinstance(env.BLUE_SBC_SESSION_IMAGER, str)

    assert isinstance(env.BLUE_SBC_SESSION_IMAGER_DIFF, float)
    assert isinstance(env.BLUE_SBC_SESSION_IMAGER_ENABLED, bool)
    assert isinstance(env.BLUE_SBC_SESSION_MONITOR_ENABLED, bool)

    assert isinstance(env.BLUE_SBC_SESSION_OBJECT_TAGS, str)

    assert isinstance(env.BLUE_SBC_SESSION_OUTBOUND_QUEUE, str)

    assert isinstance(env.BLUE_SBC_SESSION_AUTO_UPLOAD, bool)

    assert isinstance(env.BLUE_SBC_SESSION_IMAGER_PERIOD, int)
    assert isinstance(env.BLUE_SBC_SESSION_MESSENGER_PERIOD, int)
    assert isinstance(env.BLUE_SBC_SESSION_REBOOT_PERIOD, int)
    assert isinstance(env.BLUE_SBC_SESSION_SCREEN_PERIOD, int)
    assert isinstance(env.BLUE_SBC_SESSION_TEMPERATURE_PERIOD, int)
