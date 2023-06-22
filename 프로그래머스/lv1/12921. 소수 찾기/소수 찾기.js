function solution(n) {
    let primes = new Array(n+1).fill(true);
    primes[0] = primes[1] = false;

    let p = 2;
    while (p * p <= n) {
        if (primes[p]) {
            for (let i = p * p; i <= n; i += p) {
                primes[i] = false;
            }
        }
        p++;
    }

    let count = primes.reduce((sum, isPrime) => sum + (isPrime ? 1 : 0), 0);
    return count;
}
