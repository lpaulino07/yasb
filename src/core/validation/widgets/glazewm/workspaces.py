DEFAULTS = {
    "offline_label": "GlazeWM Offline",
    "populated_label": None,
    "empty_label": None,
    "hide_empty_workspaces": True,
    "hide_if_offline": False,
    "glazewm_server_uri": "ws://localhost:6123",
    "default_shadow": {
        "enabled": False,
        "color": "black",
        "offset": [1, 1],
        "radius": 3,
    },
}

VALIDATION_SCHEMA = {
    "offline_label": {
        "type": "string",
        "default": DEFAULTS["offline_label"],
    },
    "populated_label": {
        "type": "string",
        "default": DEFAULTS["populated_label"],
        "nullable": True,
    },
    "empty_label": {
        "type": "string",
        "default": DEFAULTS["empty_label"],
        "nullable": True,
    },
    "hide_empty_workspaces": {
        "type": "boolean",
        "default": DEFAULTS["hide_empty_workspaces"],
    },
    "hide_if_offline": {
        "type": "boolean",
        "default": DEFAULTS["hide_if_offline"],
    },
    "glazewm_server_uri": {
        "type": "string",
        "default": DEFAULTS["glazewm_server_uri"],
    },
    "container_shadow": {
        "type": "dict",
        "required": False,
        "schema": {
            "enabled": {"type": "boolean", "default": False},
            "color": {"type": "string", "default": "black"},
            "offset": {"type": "list", "default": [1, 1]},
            "radius": {"type": "integer", "default": 3},
        },
        "default": DEFAULTS["default_shadow"],
    },
    "btn_shadow": {
        "type": "dict",
        "required": False,
        "schema": {
            "enabled": {"type": "boolean", "default": False},
            "color": {"type": "string", "default": "black"},
            "offset": {"type": "list", "default": [1, 1]},
            "radius": {"type": "integer", "default": 3},
        },
        "default": DEFAULTS["default_shadow"],
    },
}
