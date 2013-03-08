This is a simple Content Management System made in Django.
The template design is entirely fluid.

To add a page, simply login to /admin and click add in front of "Pages Content".
To add a menu, click add in front of "Menus"

Be default two menus named "main" and "side" are already incorporated in the template.
If more menus are needed to be added, simply put following code at the place you want menu to be:

    <div class="main">

        <ul>

        {% for menu in menus %}

            {% if menu.menu.class_name = "main" %}

                    {% if menu.link = "home" %}

                         <li><a href="/">{{menu.name}}</a></li>

                    {% else %}

                        <li><a href="/{{menu.link}}">{{menu.name}}</a></li>

                    {% endif %}

            {% endif %}

        {% endfor %}

        </ul>

    </div>
and replace "menu_class" with the class name of new menu. Define CSS styles for the menu and you are ready to go!

Sample data is also available
If you start with given sample data, then
Username : mayank
Password : mayank