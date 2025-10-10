function comb(e, t) {
    var n = "".concat(e, "|").concat(t);
    return btoa(n)
}

function encryptTime(e) {
    s = 1111111111111;
    var t = (1 * e + s).toString().split("")
        , n = parseInt(10 * Math.random(), 10)
        , r = parseInt(10 * Math.random(), 10)
        , i = parseInt(10 * Math.random(), 10);
    return t.concat([n, r, i]).join("")
}

function encryptApiKey() {
    var e = "a2c903cc-b31e-4547-9299-b6d07b7631ab"
        , t = e.split("")
        , n = t.splice(0, 8);
    return e = t.concat(n).join("")
}

function getApiKey() {
    var e = (new Date).getTime()
        , t = encryptApiKey();
    return e = encryptTime(e),
        comb(t, e)
}

api = getApiKey()
console.log(api)