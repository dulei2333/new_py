function md5(t) {
    function e(t, e, n, r, o, i) {
        return a((s = a(a(e, t), a(r, i))) << (c = o) | s >>> 32 - c, n);
        var s, c
    }

    function n(t, n, r, o, i, a, s) {
        return e(n & r | ~n & o, t, n, i, a, s)
    }

    function r(t, n, r, o, i, a, s) {
        return e(n & o | r & ~o, t, n, i, a, s)
    }

    function o(t, n, r, o, i, a, s) {
        return e(n ^ r ^ o, t, n, i, a, s)
    }

    function i(t, n, r, o, i, a, s) {
        return e(r ^ (n | ~o), t, n, i, a, s)
    }

    function a(t, e) {
        var n = (65535 & t) + (65535 & e);
        return (t >> 16) + (e >> 16) + (n >> 16) << 16 | 65535 & n
    }

    var s;
    return function (t) {
        for (var e = "0123456789abcdef", n = "", r = 0; r < 4 * t.length; r++)
            n += e.charAt(t[r >> 2] >> r % 4 * 8 + 4 & 15) + e.charAt(t[r >> 2] >> r % 4 * 8 & 15);
        return n
    }(function (t, e) {
        t[e >> 5] |= 128 << e % 32,
            t[14 + (e + 64 >>> 9 << 4)] = e;
        for (var s = 1732584193, c = -271733879, u = -1732584194, l = 271733878, d = 0; d < t.length; d += 16) {
            var p = s
                , f = c
                , h = u
                , m = l;
            s = n(s, c, u, l, t[d + 0], 7, -680876936),
                l = n(l, s, c, u, t[d + 1], 12, -389564586),
                u = n(u, l, s, c, t[d + 2], 17, 606105819),
                c = n(c, u, l, s, t[d + 3], 22, -1044525330),
                s = n(s, c, u, l, t[d + 4], 7, -176418897),
                l = n(l, s, c, u, t[d + 5], 12, 1200080426),
                u = n(u, l, s, c, t[d + 6], 17, -1473231341),
                c = n(c, u, l, s, t[d + 7], 22, -45705983),
                s = n(s, c, u, l, t[d + 8], 7, 1770035416),
                l = n(l, s, c, u, t[d + 9], 12, -1958414417),
                u = n(u, l, s, c, t[d + 10], 17, -42063),
                c = n(c, u, l, s, t[d + 11], 22, -1990404162),
                s = n(s, c, u, l, t[d + 12], 7, 1804603682),
                l = n(l, s, c, u, t[d + 13], 12, -40341101),
                u = n(u, l, s, c, t[d + 14], 17, -1502002290),
                s = r(s, c = n(c, u, l, s, t[d + 15], 22, 1236535329), u, l, t[d + 1], 5, -165796510),
                l = r(l, s, c, u, t[d + 6], 9, -1069501632),
                u = r(u, l, s, c, t[d + 11], 14, 643717713),
                c = r(c, u, l, s, t[d + 0], 20, -373897302),
                s = r(s, c, u, l, t[d + 5], 5, -701558691),
                l = r(l, s, c, u, t[d + 10], 9, 38016083),
                u = r(u, l, s, c, t[d + 15], 14, -660478335),
                c = r(c, u, l, s, t[d + 4], 20, -405537848),
                s = r(s, c, u, l, t[d + 9], 5, 568446438),
                l = r(l, s, c, u, t[d + 14], 9, -1019803690),
                u = r(u, l, s, c, t[d + 3], 14, -187363961),
                c = r(c, u, l, s, t[d + 8], 20, 1163531501),
                s = r(s, c, u, l, t[d + 13], 5, -1444681467),
                l = r(l, s, c, u, t[d + 2], 9, -51403784),
                u = r(u, l, s, c, t[d + 7], 14, 1735328473),
                s = o(s, c = r(c, u, l, s, t[d + 12], 20, -1926607734), u, l, t[d + 5], 4, -378558),
                l = o(l, s, c, u, t[d + 8], 11, -2022574463),
                u = o(u, l, s, c, t[d + 11], 16, 1839030562),
                c = o(c, u, l, s, t[d + 14], 23, -35309556),
                s = o(s, c, u, l, t[d + 1], 4, -1530992060),
                l = o(l, s, c, u, t[d + 4], 11, 1272893353),
                u = o(u, l, s, c, t[d + 7], 16, -155497632),
                c = o(c, u, l, s, t[d + 10], 23, -1094730640),
                s = o(s, c, u, l, t[d + 13], 4, 681279174),
                l = o(l, s, c, u, t[d + 0], 11, -358537222),
                u = o(u, l, s, c, t[d + 3], 16, -722521979),
                c = o(c, u, l, s, t[d + 6], 23, 76029189),
                s = o(s, c, u, l, t[d + 9], 4, -640364487),
                l = o(l, s, c, u, t[d + 12], 11, -421815835),
                u = o(u, l, s, c, t[d + 15], 16, 530742520),
                s = i(s, c = o(c, u, l, s, t[d + 2], 23, -995338651), u, l, t[d + 0], 6, -198630844),
                l = i(l, s, c, u, t[d + 7], 10, 1126891415),
                u = i(u, l, s, c, t[d + 14], 15, -1416354905),
                c = i(c, u, l, s, t[d + 5], 21, -57434055),
                s = i(s, c, u, l, t[d + 12], 6, 1700485571),
                l = i(l, s, c, u, t[d + 3], 10, -1894986606),
                u = i(u, l, s, c, t[d + 10], 15, -1051523),
                c = i(c, u, l, s, t[d + 1], 21, -2054922799),
                s = i(s, c, u, l, t[d + 8], 6, 1873313359),
                l = i(l, s, c, u, t[d + 15], 10, -30611744),
                u = i(u, l, s, c, t[d + 6], 15, -1560198380),
                c = i(c, u, l, s, t[d + 13], 21, 1309151649),
                s = i(s, c, u, l, t[d + 4], 6, -145523070),
                l = i(l, s, c, u, t[d + 11], 10, -1120210379),
                u = i(u, l, s, c, t[d + 2], 15, 718787259),
                c = i(c, u, l, s, t[d + 9], 21, -343485551),
                s = a(s, p),
                c = a(c, f),
                u = a(u, h),
                l = a(l, m)
        }
        return Array(s, c, u, l)
    }(function (t) {
        for (var e = Array(), n = 0; n < 8 * t.length; n += 8)
            e[n >> 5] |= (255 & t.charCodeAt(n / 8)) << n % 32;
        return e
    }(s = t), 8 * s.length))
}

function get_sign(t) {
    e = "/youzy.dms.basiclib.api.v1.label.get"
    var r, i = "9SASji5OWnG41iRKiSvTJHlXHmRySRp1", o = "", a = t || {}, s = (e = e || "").split("?");
    if (s.length > 0 && (r = s[1]),
        r) {
        var u = r.split("&")
            , c = "";
        u.forEach((function (e) {
                var t = e.split("=");
                c += "".concat(t[0], "=").concat(encodeURI(t[1]), "&")
            }
        )),
            o = "".concat(_.trimEnd(c, "&"), "&").concat(i)
    } else
        o = Object.keys(a).length > 0 ? "".concat(JSON.stringify(a), "&").concat(i) : "&".concat(i);
    return o = o.toLowerCase(),
        md5(o)
}

// e = "/youzy.dms.basiclib.api.v1.label.get"
// t = {
//     "keyword": "",
//     "provinceNames": [],
//     "natureTypes": [],
//     "eduLevel": "",
//     "categories": [],
//     "features": [],
//     "pageIndex": 3,
//     "pageSize": 20,
//     "sort": 11
// }
// s = get_sign(e, t)
// console.log(s)
