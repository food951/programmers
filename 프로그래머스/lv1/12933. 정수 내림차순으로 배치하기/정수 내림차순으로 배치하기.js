function solution(n) {
    let a = String(n);
    b = a.split("").sort().reverse().join("");
    c = parseInt(b)
    return c;
}