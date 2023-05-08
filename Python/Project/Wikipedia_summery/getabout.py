import wikipedia
import re

# set language to English
wikipedia.set_lang("en")
while True:
    # search for a page
    print("="*100)
    query = input("Enter the Wikipedia page to retrieve: ")
    if query.lower() == "exit()":
        exit()
    try:
        page = wikipedia.page(query)
    except wikipedia.exceptions.PageError:
        # if the page doesn't exist, suggest related pages to the user
        related_pages = wikipedia.search(query)
        if related_pages:
            print(f"Did you mean one of the following pages?\n Please try again with one of these suggestions: ")
            for related in related_pages:
                print("\t● ",related)
        else:
            print("Sorry, no suggestions found. Please try again with a different search query.")

    else:
        # page = wikipedia.page(query)

        print(page.title)
        print("="*len(page.title))
        # print the full text of the page
        # print(page.content)

        patten1 = "==+ [a-zA-Z]*[^=]*=+\n\n\n"
        match1 = re.sub(patten1,"",page.content)
        patten2 = """(?<==\n)\n|== External links ==[a-zA-Z0-9\n ()':,.+"–]*"""
        match2 = re.sub(patten2,'',match1)
        patten3 = "\n\n\n"
        match = re.sub(patten3,"",match2)
        print(match)