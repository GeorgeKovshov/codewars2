import logging
import math
'''
Levels:
debug - 10
info - 20
warning - 30
error - 40
critical - 50
'''


#create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "N:\Git\codewars\lumberjack.log",
                    level = logging.DEBUG, format = LOG_FORMAT, filemode = 'w')
         #level = logging.DEBUG - show everything, logging.ERROR - only error and critical
        # filemode = 'w' - log is re-written each time
logger = logging.getLogger()

#test the logger
logger.info("our first message.")

def quadratic_formula(a, b, c):
    #Return the solutions to the equation ax^2 + bx + c = 0
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    #compute the discriminant
    logger.debug("# Compute the discriminant")
    discriminant = b**2 - 4*a*c

    #compute the two roots
    logger.debug("#compute the two roots")
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)

    #return the two roots
    logger.debug("#return the roots")
    return(root1, root2)

roots = quadratic_formula(1, 0, -4)
print(roots)

