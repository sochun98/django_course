function getCookie(name) {
    var cookieName = name + "=";
    var decodeCookie = decodeURIComponent(document.cookie);
    var cookieArray = decodeCookie.split(';');

    for (var i = 0; i < cookieArray.length; i++) {
        var cookie = cookieArray[i];
        while (cookie.charAt(0) == ' ') {
            cookie = cookie.substring(1);
        }

        if (cookie.indexOf(cookieName) == 0) {
            return cookie.substring(cookieName.length, cookie.length);
        }
    }

    return "";
}