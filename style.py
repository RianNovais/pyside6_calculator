import qdarktheme
from variables import DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR, PRIMARY_COLOR

#here is configured, the theme that will be applied to our project window, and its settings


#applying specific colors to some special buttons (operations buttons, etc.) and hover behaviors
qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: "#FFF";
        background: #FF007F;
    }}
    QPushButton[cssClass="specialButton"]:hover {{ 
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{ 
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""

#here we create a function that will configure the qdarktheme function, which will apply the theme to our application.
def setup_theme():
    qdarktheme.setup_theme(
        theme='dark', #the name of the theme can be light or dark
        corner_shape='rounded', #establishing rounded corners for all the elements of our application
        custom_colors={ #setting the default colors of our theme to dark and light mode
            "[dark]": {
                "primary": f"{PRIMARY_COLOR}",
            },
            "[light]": {
                "primary": f"#FF007F",
            },
        },
        #adding the string "QSS" that defines special colors for special buttons to the function that defines the theme
        additional_qss = qss
    )