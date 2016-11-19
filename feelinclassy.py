######################### feelinclassy: a class containing functions to print various messages #########################
###################################### Maryam Ahmed, University of Oxford, 2016 ####################################

##### We define the class here ####
class feelinClassy(object):

    # The 'init' function (or METHOD) is the first thing that runs whenever the class is called
    def __init__(self):
        self.howclassy = raw_input("How classy are you feeling? ")
        print "You're feeling "+ self.howclassy + " classy!"

    # Other functions, or methods, are also defined inside the class
    def superclassy(self):
        print "I AM FEELING SUPER CLASSY"
####################################

# We can create an instance of the 'feelinClassy' class which makes the 'init' function inside the class run
myclass = feelinClassy()

# We can also call other methods  or functions inside the class like this
myclass.superclassy()

