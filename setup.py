from setuptools import setup

""" few notes on how setup.py can be used.
    
    * entry_points: determines the name of the installed cmd on the os & what is launched
        * entry_points="[console_scripts] my_callable_name=pckgname.pyfile:main_function"
        
        or as from the doc below: 
            setup(
                # other arguments here...
                entry_points={
                    "setuptools.installation": [
                        "eggsecutable = my_package.some_module:main_func",
                    ]
                }
            )
            
    * name="pip_recognized_name_in_piplist"
"""

pip_name    = "appname"
app_name    = "appname"


setup(
    name=pip_name,
    version="1.0",
    packages=["click_code", "click_code.commands"],
    include_package_data=True,
    install_requires=["click"],
    entry_points={"console_scripts":[
        f"{app_name}=cli_main:cli"
    ]},

)
