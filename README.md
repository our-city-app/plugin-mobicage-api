
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/99f4ec663f24488db772c8900d2d08ec)](https://www.codacy.com/app/lucas-vanhalst/plugin-rogerthat-api?utm_source=github.com&utm_medium=referral&utm_content=rogerthat-platform/plugin-rogerthat-api&utm_campaign=badger)

To receive callbacks from rogerthat you need to setup your rogerthat settings:

You can find API_KEY, SIK_KEY in the service panels of your service.
Before running the code below in the 'interactive_explorer' you will need to correct your callback configuration to YOUR_IP/plugins/rogerthat_api/callback_api 

```python
def setup_settings():
    from plugins.rogerthat_api.plugin_bizz import create_app_settings
    create_app_settings("API_KEY", "SIK_KEY", "REFERENCE")

def setup_callbacks():
    from plugins.rogerthat_api.api.system import put_callback
    functions = ["friend.register", "friend.register_result"]
    for f in functions:
        put_callback(U'API_KEY', f)
                        
```
