#New assignment File
#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.

def computepay(h,r):
    h = float(h)
    r = float(r)
    if h >40:
        ovh = (h-40) #extra hours
        reg = (40*r) # regular pay upto 40 hours
        ovr = ovh * (r*1.5) # extra cash for more than 40hours
        actp = ovr+reg # calcualte actualpay
        #Pay = (((h-40)*1.5)+40*r)
        print(actp)
    else:
        actp = h*r
    return actp

hrs = input("Enter Hours:")
rph = input("Enter Rate:")
p = computepay(hrs,rph)
print("Pay",p)
