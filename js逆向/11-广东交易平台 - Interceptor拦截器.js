CryptoJS = require('crypto-js')

function qF(e) {
    let t = "";
    return typeof e == "object" ? t = Object.keys(e).map(n => `${n}=${e[n]}`).sort().join("&") : typeof e == "string" && (t = e.split("&").sort().join("&")),
    t
}

function D1(e={}) {
    const {p: t, t: n, n: u, k: o} = e
      , r = qF(t);
    return CryptoJS.SHA256(u + o + decodeURIComponent(r) + n).toString()
}

function Signature(page,times){
    p = D1({
        p: 'type=trading-type&openConvert=false&keyword=&siteCode=44&secondType=A&tradingProcess=&thirdType=%5B%5D&projectType=&publishStartTime=&publishEndTime=&pageNo='+ page +'&pageSize=10',
        t: times,
        n: 'RXI4FhJhMRbwQ7FJ',
        k: 'k8tUyS$m'
    });
    return p
}