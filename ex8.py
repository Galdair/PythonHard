formatter = "%r %r %r %r"

print formatter %(1,2,3,4)
print formatter %("one","two","three","four")
print formatter %(True,False,True,False)
print formatter %(formatter,formatter,formatter,formatter)
print formatter %("i had this thing","that you could type up rigth","but it didn't sing","So i said goodnigth")