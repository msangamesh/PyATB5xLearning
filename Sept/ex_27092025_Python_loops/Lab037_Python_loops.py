
browser_name = input("Enter your browser name: ")
match browser_name :
    case "Firefox" :
        print("Execute the Firefox code")
    case "Chrome" :
        print("Execute the Chrome code")
    case "Safari" :
        print("Execute the Safari code")
    case "Edge" :
        print("Execute the Edge code")
    case _:
        print("Invalid browser name")