from os import system
from os.path import exists
import requests
import datetime
import tkinter as tk
from pytube import Search


def SearchSocials(username):
    # INSTAGRAM
    instagram = f"https://www.instagram.com/{username}"

    # FACEBOOK
    facebook = f"https://www.facebook.com/{username}"

    # TWITTER
    twitter = f"https://www.twitter.com/{username}"

    # YOUTUBE
    youtube = f"https://www.youtube.com/{username}"

    # BLOGGER
    blogger = f"https://{username}.blogspot.com"

    # GOOGLE+
    google_plus = f"https://plus.google.com/s/{username}/top"

    # REDDIT
    reddit = f"https://www.reddit.com/user/{username}"

    # WORDPRESS
    wordpress = f"https://{username}.wordpress.com"

    # PINTEREST
    pinterest = f"https://www.pinterest.com/{username}"

    # GITHUB
    github = f"https://www.github.com/{username}"

    # TUMBLR
    tumblr = f"https://{username}.tumblr.com"

    # FLICKR
    flickr = f"https://www.flickr.com/people/{username}"

    # STEAM
    steam = f"https://steamcommunity.com/id/{username}"

    # VIMEO
    vimeo = f"https://vimeo.com/{username}"

    # SOUNDCLOUD
    soundcloud = f"https://soundcloud.com/{username}"

    # DISQUS
    disqus = f"https://disqus.com/by/{username}"

    # MEDIUM
    medium = f"https://medium.com/@{username}"

    # DEVIANTART
    deviantart = f"https://{username}.deviantart.com"

    # VK
    vk = f"https://vk.com/{username}"

    # ABOUT.ME
    aboutme = f"https://about.me/{username}"

    # IMGUR
    imgur = f"https://imgur.com/user/{username}"

    # FLIPBOARD
    flipboard = f"https://flipboard.com/@{username}"

    # SLIDESHARE
    slideshare = f"https://slideshare.net/{username}"

    # FOTOLOG
    fotolog = f"https://fotolog.com/{username}"

    # SPOTIFY
    spotify = f"https://open.spotify.com/user/{username}"

    # MIXCLOUD
    mixcloud = f"https://www.mixcloud.com/{username}"

    # SCRIBD
    scribd = f"https://www.scribd.com/{username}"

    # BADOO
    badoo = f"https://www.badoo.com/en/{username}"

    # PATREON
    patreon = f"https://www.patreon.com/{username}"

    # BITBUCKET
    bitbucket = f"https://bitbucket.org/{username}"

    # DAILYMOTION
    dailymotion = f"https://www.dailymotion.com/{username}"

    # ETSY
    etsy = f"https://www.etsy.com/shop/{username}"

    # CASHME
    cashme = f"https://cash.me/{username}"

    # BEHANCE
    behance = f"https://www.behance.net/{username}"

    # GOODREADS
    goodreads = f"https://www.goodreads.com/{username}"

    # INSTRUCTABLES
    instructables = f"https://www.instructables.com/member/{username}"

    # KEYBASE
    keybase = f"https://keybase.io/{username}"

    # KONGREGATE
    kongregate = f"https://kongregate.com/accounts/{username}"

    # LIVEJOURNAL
    livejournal = f"https://{username}.livejournal.com"

    # ANGELLIST
    angellist = f"https://angel.co/{username}"

    # LAST.FM
    last_fm = f"https://last.fm/user/{username}"

    # DRIBBBLE
    dribbble = f"https://dribbble.com/{username}"

    # CODECADEMY
    codecademy = f"https://www.codecademy.com/{username}"

    # GRAVATAR
    gravatar = f"https://en.gravatar.com/{username}"

    # PASTEBIN
    pastebin = f"https://pastebin.com/u/{username}"

    # FOURSQUARE
    foursquare = f"https://foursquare.com/{username}"

    # ROBLOX
    roblox = f"https://www.roblox.com/user.aspx?username={username}"

    # GUMROAD
    gumroad = f"https://www.gumroad.com/{username}"

    # NEWSGROUND
    newsground = f"https://{username}.newgrounds.com"

    # WATTPAD
    wattpad = f"https://www.wattpad.com/user/{username}"

    # CANVA
    canva = f"https://www.canva.com/{username}"

    # CREATIVEMARKET
    creative_market = f"https://creativemarket.com/{username}"

    # TRAKT
    trakt = f"https://www.trakt.tv/users/{username}"

    # 500PX
    five_hundred_px = f"https://500px.com/{username}"

    # BUZZFEED
    buzzfeed = f"https://buzzfeed.com/{username}"

    # TRIPADVISOR
    tripadvisor = f"https://tripadvisor.com/members/{username}"

    # HUBPAGES
    hubpages = f"https://{username}.hubpages.com"

    # CONTENTLY
    contently = f"https://{username}.contently.com"

    # HOUZZ
    houzz = f"https://houzz.com/user/{username}"

    # BLIP.FM
    blipfm = f"https://blip.fm/{username}"

    # WIKIPEDIA
    wikipedia = f"https://www.wikipedia.org/wiki/User:{username}"

    # HACKERNEWS
    hackernews = f"https://news.ycombinator.com/user?id={username}"

    # CODEMENTOR
    codementor = f"https://www.codementor.io/{username}"

    # REVERBNATION
    reverb_nation = f"https://www.reverbnation.com/{username}"

    # DESIGNSPIRATION
    designspiration = f"https://www.designspiration.net/{username}"

    # BANDCAMP
    bandcamp = f"https://www.bandcamp.com/{username}"

    # COLOURLOVERS
    colourlovers = f"https://www.colourlovers.com/love/{username}"

    # IFTTT
    ifttt = f"https://www.ifttt.com/p/{username}"

    # EBAY
    ebay = f"https://www.ebay.com/usr/{username}"

    # SLACK
    slack = f"https://{username}.slack.com"

    # OKCUPID
    okcupid = f"https://www.okcupid.com/profile/{username}"

    # TRIP
    trip = f"https://www.trip.skyscanner.com/user/{username}"

    # ELLO
    ello = f"https://ello.co/{username}"

    # TRACKY
    tracky = f"https://tracky.com/user/~{username}"

    # BASECAMP
    basecamp = f"https://{username}.basecamphq.com/login"

    """ WEBSITE LIST - USE FOR SEARCHING OF USERNAME """
    WEBSITES = [
        instagram,
        facebook,
        twitter,
        youtube,
        blogger,
        google_plus,
        reddit,
        wordpress,
        pinterest,
        github,
        tumblr,
        flickr,
        steam,
        vimeo,
        soundcloud,
        disqus,
        medium,
        deviantart,
        vk,
        aboutme,
        imgur,
        flipboard,
        slideshare,
        fotolog,
        spotify,
        mixcloud,
        scribd,
        badoo,
        patreon,
        bitbucket,
        dailymotion,
        etsy,
        cashme,
        behance,
        goodreads,
        instructables,
        keybase,
        kongregate,
        livejournal,
        angellist,
        last_fm,
        dribbble,
        codecademy,
        gravatar,
        pastebin,
        foursquare,
        roblox,
        gumroad,
        newsground,
        wattpad,
        canva,
        creative_market,
        trakt,
        five_hundred_px,
        buzzfeed,
        tripadvisor,
        hubpages,
        contently,
        houzz,
        blipfm,
        wikipedia,
        hackernews,
        reverb_nation,
        designspiration,
        bandcamp,
        colourlovers,
        ifttt,
        ebay,
        slack,
        okcupid,
        trip,
        ello,
        tracky,
        basecamp,
    ]

    AllWebsites = []
    for url in WEBSITES:
        r = requests.get(url)
        if r.status_code == 200:
            if username.lower() in r.text.lower():
                AllWebsites.append(url)
    return AllWebsites


def GetMonth(month: int):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    return months[month - 1]


class roAPI:
    def GetID(Username: str) -> int:
        requestPayload = {
            "usernames": [Username],
            "excludeBannedUsers": True,  # Whether to include banned users within the request, change this as you wish
        }

        responseData = requests.post(
            "https://users.roblox.com/v1/usernames/users", json=requestPayload
        )
        if responseData.status_code != 200:
            return 0

        userId = responseData.json()["data"][0]["id"]
        return userId

    def GetAge(UserID: int) -> str:
        response = requests.get("https://users.roblox.com/v1/users/" + str(UserID))
        try:
            CreationDate = response.json()["created"]
            CreationDate = CreationDate.split("T")
            CreationDate = CreationDate[0].split("-")
            CreationDate = datetime.date(
                int(CreationDate[0]), int(CreationDate[1]), int(CreationDate[2])
            )
            Days = (datetime.date.today()) - (CreationDate)
            Days = str(Days).split(" ")
            return Days[0]
        except:
            return "https://users.roblox.com/v1/users/" + str(UserID)

    def GetLimiteds(UserID: int) -> tuple:
        """
        Returns the total list of a users limiteds

        Please be aware this function can take some time to run depending on internet speed and how many limiteds a user owns
        """
        Limiteds = []
        IDs = []
        Cursor = ""
        Done = False
        while Done == False:
            try:
                response = requests.get(
                    "https://inventory.roblox.com/v1/users/"
                    + f"/{UserID}/assets/collectibles?sortOrder=Asc&limit=100&cursor={Cursor}"
                )
                Items = response.json()
                if (response.json()["nextPageCursor"] == "null") or response.json()[
                    "nextPageCursor"
                ] == None:
                    Done = True
                else:
                    Done = False
                    Cursor = response.json()["nextPageCursor"]
                for Item in Items["data"]:
                    try:
                        Limited = Item["name"]
                        ID = Item["assetId"]
                        Limiteds.append(Limited)
                        IDs.append(ID)
                    except:
                        Limiteds = Limiteds
                        IDs = IDs
                if response.json()["nextPageCursor"] == "None":
                    Done = True

            except Exception as ex:
                Done = True
        return (Limiteds, IDs)

    def CreationDate(UserID: int) -> str:
        response = requests.get("https://users.roblox.com/v1/users/" + str(UserID))
        try:
            CreationDate = response.json()["created"]
            CreationDate = CreationDate.split("T")
            CreationDate = CreationDate[0].split("-")

            return (
                str(CreationDate[1])
                + "/"
                + str(CreationDate[2])
                + "/"
                + str(CreationDate[0])
            )  # DD/MM/YYYY -- The Correct Format
        except:
            return response.json()["errors"][0]["message"]

    def GetDescription(UserID: int) -> str:
        response = requests.get("https://users.roblox.com/v1/users/" + str(UserID))
        try:
            return response.json()["description"]
        except:
            return "User not found"

    def UsernameHistory(UserID: int) -> list[list, str]:
        Cursor = ""
        Done = False
        PastNames = []
        while Done == False:
            response = requests.get(
                "https://users.roblox.com/v1/users/"
                + f"{UserID}/username-history?limit=100&sortOrder=Asc&cursor={Cursor}"
            )
            Names = response.json()["data"]
            if (response.json()["nextPageCursor"] == "null") or response.json()[
                "nextPageCursor"
            ] == None:
                Done = True
            else:
                Done = False
                Cursor = response.json()["nextPageCursor"]
            for Name in Names:
                PastNames.append(Name["name"])
            if response.json()["nextPageCursor"] == "None":
                Done = True
        return PastNames


def GetPlayerInfo():
    Username = username_entry.get()
    try:
        UserID = roAPI.GetID(Username)
        Description = "Description: " + roAPI.GetDescription(UserID)
        CreationDate = roAPI.CreationDate(UserID)
        CreationMonth = "Creation Month: " + GetMonth(int(CreationDate[:2]))
        CreationDate = "Creation Date: " + CreationDate
        AccountAge = "Account Age: " + str(roAPI.GetAge(UserID)) + " Days"
        UserHistory = "Username History: " + str(roAPI.UsernameHistory(UserID)).replace(
            '"', ""
        ).replace("[", "").replace("]", "")
        Limiteds = roAPI.GetLimiteds(UserID)
        LimitedStr = "Limiteds: \n"
        for i in Limiteds[0]:
            ID = Limiteds[1][Limiteds[0].index(i)]
            LimitedStr += i + ": " + str(ID) + "\n"
        # Check for socials
        Socials = SearchSocials(Username)
        # Change Log Box
        new_text = (
            "UserID: "
            + str(UserID)
            + "\n"
            + Description
            + "\n"
            + CreationDate
            + "\n"
            + CreationMonth
            + "\n"
            + AccountAge
            + "\n"
            + UserHistory
            + "\n"
            + LimitedStr
            + "\n"
            + "Socials"
            + "\n"
            + "\n".join(Socials)
        )
    except Exception as e:
        new_text = f"Invalid User {Username} (Make sure your using their @ not display) or there was an error {e}"

    log_box.config(state=tk.NORMAL)  # Enable the text box to modify its content
    log_box.delete("1.0", tk.END)  # Clear the existing text
    log_box.insert(tk.END, new_text)  # Insert the new text
    log_box.config(state=tk.DISABLED)  # Disable the text box again


# Main tkinter window
root = tk.Tk()
root.title("RoFinder")

# Username Entry
username_label = tk.Label(root, text="Username:")
username_label.pack(anchor="w")

username_entry = tk.Entry(root, width=40)
username_entry.pack()

# Find button
send_button = tk.Button(root, text="Find Player", command=GetPlayerInfo)
send_button.pack()

# Log Box
log_box = tk.Text(root, height=10, width=50, wrap=tk.WORD, state=tk.DISABLED)
log_box.pack()

root.mainloop()
