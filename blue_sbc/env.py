from blue_options.env import load_config, load_env, get_env

load_config(__name__)
load_env(__name__)

BLUE_SBC_CAMERA_HI_RES = get_env("BLUE_SBC_CAMERA_HI_RES", True)
BLUE_SBC_CAMERA_WIDTH = get_env("BLUE_SBC_CAMERA_WIDTH", 728)
BLUE_SBC_CAMERA_HEIGHT = get_env("BLUE_SBC_CAMERA_HEIGHT", 600)
BLUE_SBC_CAMERA_ROTATION = get_env("BLUE_SBC_CAMERA_ROTATION", 0)

BLUE_SBC_DISPLAY_FULLSCREEN = get_env("BLUE_SBC_DISPLAY_FULLSCREEN", True)

BLUE_SBC_HARDWARE_KIND = get_env("BLUE_SBC_HARDWARE_KIND")

BLUE_SBC_SESSION_PLUGIN = get_env("BLUE_SBC_SESSION_PLUGIN")

BLUE_SBC_SESSION_IMAGER = get_env("BLUE_SBC_SESSION_IMAGER")
BLUE_SBC_SESSION_IMAGER_DIFF = get_env("BLUE_SBC_SESSION_IMAGER_DIFF", 0.1)
BLUE_SBC_SESSION_IMAGER_ENABLED = get_env("BLUE_SBC_SESSION_IMAGER_ENABLED", True)

BLUE_SBC_SESSION_MONITOR_ENABLED = get_env("BLUE_SBC_SESSION_MONITOR_ENABLED", True)

BLUE_SBC_SESSION_OBJECT_TAGS = get_env("BLUE_SBC_SESSION_OBJECT_TAGS")

BLUE_SBC_SESSION_OUTBOUND_QUEUE = get_env("BLUE_SBC_SESSION_OUTBOUND_QUEUE")

BLUE_SBC_SESSION_AUTO_UPLOAD = get_env("BLUE_SBC_SESSION_AUTO_UPLOAD", True)

BLUE_SBC_SESSION_IMAGER_PERIOD = get_env("BLUE_SBC_SESSION_IMAGER_PERIOD", 300)
BLUE_SBC_SESSION_MESSENGER_PERIOD = get_env("BLUE_SBC_SESSION_MESSENGER_PERIOD", 60)
BLUE_SBC_SESSION_REBOOT_PERIOD = get_env("BLUE_SBC_SESSION_REBOOT_PERIOD", 14400)
BLUE_SBC_SESSION_SCREEN_PERIOD = get_env("BLUE_SBC_SESSION_SCREEN_PERIOD", 4)
BLUE_SBC_SESSION_TEMPERATURE_PERIOD = get_env(
    "BLUE_SBC_SESSION_TEMPERATURE_PERIOD", 300
)
