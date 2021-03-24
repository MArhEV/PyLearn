def describe_city(city, country='Poland'):
    text = f"{city}, {country}"
    return text.title()

text = describe_city('Kielce')
print(text)
text2 = describe_city('Moscow', 'Russia')
print(text2)
