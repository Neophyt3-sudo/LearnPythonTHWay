#This one is like your scripts with argv
def print_two(*args):
#def = define
#args is bundled up.
#stretch into two 1 & 2 args = args
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#Main arg is connected by two args

#Ok, that *argsis actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#A lot more simple to understand. String for string.

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#Same as above.
    
# this one takes no arguments
def print_none():
    print "I got nothin'."

#No args.

print_two("Zed","Shaw")
#Defined.
print_two_again("Zed","Shaw")

print_one("Hi!")

print_none()

def test_in_three(*nums):
    num1, num2, num3 = nums
    print "Num 1: %r, num2: %r, num3: %r" % (num1, num2, num3)
#I string 3 nums into one = nums. 
#I then print in %r  by % ().

def test_in_two(num1, num2, num3):
    print "num1: %r, num2: %r, num3: %r" % (num1, num2, num3)
#I don't know whether to think this is more repetitive than the last or not.
#Last one I can see it being used because it is more organised.
#Whereas this one is a mess. Could be wrong!

def test_in_one(num1):
    print "Num1: %r" % (num1)
#Very basic idea on what def does.

def print_none():
    print "I'm too old for this shit"

test_in_three("1","2","3")
test_in_two("1.2","2.2","3.2")
test_in_one("Hi!")

#DO NOT FORGET DOUBLE DOTS (:). WITHOUT THESE, INVALID SYNTAX. 
#FOR GODS SAKE, YOU KEEP BLOODY FORGETTING %r. 






















    
    
    
