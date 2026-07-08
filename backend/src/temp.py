from urllib.parse import urlsplit

print(
    urlsplit(
        "https://witcher.fandom.com/api.php?action=parse&format=json&page=The_Witcher_3:_Wild_Hunt"
    )
)
print(urlsplit("/wiki/REDengine"))
