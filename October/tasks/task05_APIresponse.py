
API_responce = int(input("Fetch API response: "))

if API_responce == 200:
    print("Passed API response")
else:
    if API_responce == 404:
        print("Sorry, API response failed")
