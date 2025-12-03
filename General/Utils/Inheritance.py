# Global variable (outside any class)
global_var = "Global"

class Parent:
    # Static (class) variable - shared among all instances of the class
    static_var = "Parent-Static"

    def __init__(self, obj_var):
        # Object/instance variable - unique to each instance
        self.obj_var = obj_var

    def show_vars(self):
        print("=====PARENT=====")
        print("Global variable:", global_var)
        print("Parent static/class variable:", Parent.static_var)
        print("Parent object/instance variable:", self.obj_var)
        print("===============")

    def update_global(self, val: str):
        global global_var
        global_var = val

    def print_global_without_global(self) -> str:
        return global_var

    def print_global_without_global_print_and_return(self) -> str:
        print(f"parent-without |{global_var}|")
        return global_var

    def print_global_with_global(self) -> str:
        global global_var
        return global_var

class Child1(Parent):
    def __init__(self, obj_var, extra_var):
        super().__init__(obj_var)  # Inherit initialization from Parent
        self.extra_var = extra_var

    def show_all(self):
        self.show_vars()
        print("=====CHILD1=====")
        print("Child1 extra variable:", self.extra_var)
        print("===============")

    def update_global(self, val: str):
        global global_var
        global_var = val

    def print_global_without_global(self) -> str:
        return global_var

    def print_global_without_global_print_and_return(self) -> str:
        print(f"child1-without |{global_var}|")
        return global_var

    def print_global_with_global(self) -> str:
        global global_var
        return global_var

class Child2(Parent):
    def __init__(self, obj_var, extra_var):
        super().__init__(obj_var)  # Inherit initialization from Parent
        self.extra_var = extra_var

    def show_all(self):
        self.show_vars()
        print("=====CHILD2=====")
        print("Child2 extra variable:", self.extra_var)
        print("===============")

    def update_global(self, val: str):
        global global_var
        global_var = val

    def print_global_without_global(self) -> str:
        return global_var

    def print_global_without_global_print_and_return(self) -> str:
        print(f"child2-without |{global_var}|")
        return global_var

    def print_global_with_global(self) -> str:
        global global_var
        return global_var


# Creating an object of Child class
parent_obj = Parent("Parent-object")
child_obj1 = Child1("Child1-object", "Child1-object-extra")
child_obj2 = Child2("Child2-object", "Child2-object-extra")

# Access variables and demonstrate inheritance
parent_obj.show_vars()
child_obj1.show_all()
child_obj2.show_all()

# Access static/class variable using class name and instance
print(Parent.static_var)       # via class
print(child_obj1.static_var)    # via instance

# Modify class variable (static_var) via class name
Parent.static_var = "Parent-Static-UPDATED"
# reflects changed made to static variable for both parent and child objects
print(f"accessing parent static with child1 object |{child_obj1.static_var}|")
print(f"accessing parent static with child2 object |{child_obj2.static_var}|")

# Modify instance variable - only affects object of specific class
child_obj1.obj_var = "Child1-object-UPDATED" # only modifies child1 object
parent_obj.show_vars() # NO changes to parent object
child_obj1.show_all()
child_obj2.show_all() # NO changes to child2 object

######
###### Modify Parent Static variable with Child ######
######

# modify with Child2 CLASS
Child2.static_var = "Parent-Static-UPDATED-BY-CHILD2-CLASS"
# changes for Child2 CLASS and OBJECT both.
# does NOT change for Parent and other child classes and objects.

print(f"accessing parent static with parent class |{Parent.static_var}|")
print(f"accessing parent static with parent object |{parent_obj.static_var}|")
print(f"accessing parent static with child1 class |{Child1.static_var}|")
print(f"accessing parent static with child1 object |{child_obj1.static_var}|")
print(f"accessing parent static with child2 class |{Child2.static_var}|")
print(f"accessing parent static with child2 object |{child_obj2.static_var}|")

# modify with Child2 OBJECT
# changes only for Child2 OBJECT.
# does NOT change for Child2 CLASS.
# does NOT change it for Parent or other child classes or child objects.
child_obj2.static_var = "Parent-Static-UPDATED-BY-CHILD2-OBJECT"
print(f"accessing parent static with parent class |{Parent.static_var}|")
print(f"accessing parent static with parent object |{parent_obj.static_var}|")
print(f"accessing parent static with child1 class |{Child1.static_var}|")
print(f"accessing parent static with child1 object |{child_obj1.static_var}|")
print(f"accessing parent static with child2 class |{Child2.static_var}|")
print(f"accessing parent static with child2 object |{child_obj2.static_var}|")

######
###### Modify Global variable with Parent ######
######
parent_obj.update_global(val="Global-UPDATED-BY-PARENT-OBJECT")

print("===============")
print("===============")
print(f"global after updating by PARENT |{global_var}|")
print("===============")
print(f"parent without global |{parent_obj.print_global_without_global()}|")
print(f"parent with global|{parent_obj.print_global_with_global()}|")
print(f"parent without global |{parent_obj.print_global_without_global_print_and_return()}|")
print("===============")
print(f"child1 without global |{child_obj1.print_global_without_global()}|")
print(f"child1 with global |{child_obj1.print_global_with_global()}|")
print(f"child1 without global |{child_obj1.print_global_without_global_print_and_return()}|")
print("===============")
print(f"child2 without global |{child_obj2.print_global_without_global()}|")
print(f"child2 with global |{child_obj2.print_global_with_global()}|")
print(f"child2 without global |{child_obj2.print_global_without_global_print_and_return()}|")
######
###### Modify Global variable with Child1 ######
######
child_obj1.update_global(val="Global-UPDATED-BY-CHILD1-OBJECT")

print("===============")
print("===============")
print(f"global after updating by CHILD1  |{global_var}|")
print("===============")
print(f"parent without global |{parent_obj.print_global_without_global()}|")
print(f"parent with global|{parent_obj.print_global_with_global()}|")
print(f"parent without global |{parent_obj.print_global_without_global_print_and_return()}|")
print("===============")
print(f"child1 without global |{child_obj1.print_global_without_global()}|")
print(f"child1 with global |{child_obj1.print_global_with_global()}|")
print(f"child1 without global |{child_obj1.print_global_without_global_print_and_return()}|")
print("===============")
print(f"child2 without global |{child_obj2.print_global_without_global()}|")
print(f"child2 with global |{child_obj2.print_global_with_global()}|")
print(f"child2 without global |{child_obj2.print_global_without_global_print_and_return()}|")

######
###### Modify Global variable with Child2 ######
######
child_obj2.update_global(val="Global-UPDATED-BY-CHILD2-OBJECT")

print("===============")
print("===============")
print(f"global after updating by CHILD2  |{global_var}|")
print("===============")
print(f"parent without global |{parent_obj.print_global_without_global()}|")
print(f"parent with global|{parent_obj.print_global_with_global()}|")
print(f"parent without global |{parent_obj.print_global_without_global_print_and_return()}|")
print("===============")
print(f"child1 without global |{child_obj1.print_global_without_global()}|")
print(f"child1 with global |{child_obj1.print_global_with_global()}|")
print(f"child1 without global |{child_obj1.print_global_without_global_print_and_return()}|")
print("===============")
print(f"child2 without global |{child_obj2.print_global_without_global()}|")
print(f"child2 with global |{child_obj2.print_global_with_global()}|")
print(f"child2 without global |{child_obj2.print_global_without_global_print_and_return()}|")