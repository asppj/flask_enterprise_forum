from flask_nav.elements import Navbar, View, Subgroup
from flask_nav import Nav

nav = Nav()


@nav.navigation()
def homeNavBar():
    return Navbar('集采论坛',
                  View('主页', 'home.index'),
                  View('服务', 'home.service'),
                  Subgroup('个人中心',
                           View('登录', 'home.login'),
                           View('项目一', 'home.about1'),
                           ),
                  )
